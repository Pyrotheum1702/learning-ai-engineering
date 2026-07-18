# ### 6. Contact book with JSON persistence
# Store contacts (name, phone, email) that survive between runs.
# - **Requirements:** add / search / edit / delete; data saved to `contacts.json`
#   and reloaded on startup; searching is case-insensitive substring match.
# - **You'll learn:** `json` load/dump, dicts of records, CRUD design, atomic-ish saves.
# - **Stretch:** validate email/phone with `re`; export to CSV.

import json
import os
import re
import csv

contact_data = {}


NAME = "name"
PHONE = "phone"
EMAIL = "email"
SAVE_FILE_DIR = os.path.curdir + "/data"
SAVE_FILE_PATH = SAVE_FILE_DIR + "/contacts.json"


def is_valid_phone(phone: str) -> bool:
    digits = re.sub(r"[\s\-]", "", phone)
    return re.fullmatch(r"\+?\d{7,15}", digits) is not None


def is_valid_email(email: str) -> bool:
    return re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email) is not None


def save_contact_data() -> None:
    os.makedirs(SAVE_FILE_DIR, 0o777, True)

    with open(SAVE_FILE_PATH, "w") as f:
        return json.dump(contact_data, f)


def load_contact_data() -> dict:
    if os.path.exists(SAVE_FILE_PATH):
        with open(SAVE_FILE_PATH, "r") as f:
            return json.load(f)
    return {}


def add(command_argument="") -> None:
    if not command_argument:
        return print("Contact name is required.")

    name = command_argument.lower()

    if name in contact_data:
        print(f"This contact is already exist.")
        return

    phone = input("  phone: ").strip()
    if not is_valid_phone(phone):
        return print("Invalid phone number (7-15 digits, optional +).")
    phone = phone.replace(" ", "-")

    email = input("  email: ").strip()
    if email and not is_valid_email(email):
        return print("Invalid email address.")

    contact_data[name] = {NAME: command_argument, PHONE: phone, EMAIL: email}
    save_contact_data()

    print(f"Contact added.")
    return


def search(command_argument="") -> any:
    if not command_argument:
        return print("Contact name is required.")

    name = command_argument.lower()

    if name in contact_data:
        item = contact_data[name]
        print(f"{item[NAME]} - {item[PHONE]} - {item[EMAIL]}")
        return

    print("\nContact not found.\n")
    sim_count = 0
    for key in contact_data.keys():
        if name in key:
            if sim_count == 0:
                print("Similar contacts:")

            item = contact_data[key]
            print(f"{item[NAME]} - {item[PHONE]} - {item[EMAIL]}")
            sim_count += 1

        if sim_count >= 10:
            break

    return


def edit(command_argument="") -> None:
    if not command_argument:
        return print("Contact name is required.")

    name = command_argument.lower()

    if not name in contact_data:
        return print("Contact not found.")

    item = contact_data[name]

    def save_item():
        contact_data[name] = item
        save_contact_data()

    phone = input(" phone:").strip()

    if len(phone) > 0:
        if not is_valid_phone(phone):
            return print("Invalid phone number (7-15 digits, optional +).")
        item[PHONE] = phone.replace(" ", "-")
        save_item()

    email = input(" email:").strip()

    if len(email) > 0:
        if not is_valid_email(email):
            return print("Invalid email address.")
        item[EMAIL] = email
        save_item()

    print(f"Contact saved.")

    save_contact_data()
    return


def remove(command_argument="") -> None:
    if not command_argument:
        return print("Contact name is required.")

    name = command_argument.lower()

    if not name in contact_data:
        return print("Contact not found.")

    del contact_data[name]

    print(f"Contact removed.")

    save_contact_data()
    return


def list(command_argument="") -> None:
    item_keys = contact_data.keys()

    if len(contact_data) < 1:
        print("\nContact list is empty.")

    print("\nContact list:")

    for key in item_keys:
        item = contact_data[key]
        print(f"  {item[NAME]} - {item[PHONE]} - {item[EMAIL]}")

    return


def export_csv(command_argument="") -> None:
    filename = command_argument.strip() or "contacts.csv"
    filepath = os.path.join(SAVE_FILE_DIR, filename)

    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[NAME, PHONE, EMAIL])
        writer.writeheader()
        for key in contact_data:
            writer.writerow(contact_data[key])

    print(f"Exported {len(contact_data)} contacts to {filepath}")


def quit(command_argument="") -> None:
    save_contact_data()
    print("Saved. Bye.\n")
    return exit()


commands = {
    "add": add,
    "search": search,
    "edit": edit,
    "remove": remove,
    "list": list,
    "quit": quit,
}

comments = {
    "add": "Add a contact",
    "search": "Find contacts by name",
    "edit": "Change a contact's phone/email",
    "remove": "Delete a contact",
    "list": "Show all contacts",
    "quit": "Save and exit",
}

# stretch
commands["export"] = export_csv
comments["export"] = "Export all contacts to a CSV file"


def loop() -> None:
    command = input(">")
    seg = command.split(" ")

    try:
        if seg[0] == "":
            return loop()

        if seg[0] not in commands.keys():
            print("Unknown command.")
            return loop()

        if len(seg) > 1:
            command_value = ""
            for s in seg[1:]:
                command_value += s + " "

            command_value = command_value.strip()

            # print(f"call {seg[0]} : {command_value}")

            commands[seg[0]](command_value)
        else:
            commands[seg[0]]()
    except Exception as e:
        print(f"Error: {e}")
        # print(f"Error: {e} - {e.with_traceback()}")
        return loop()

    loop()


def main() -> None:
    global contact_data

    contact_data = load_contact_data()

    print("Commands:")

    for key, value in commands.items():
        print(f"{key}: {comments[key]}")

    loop()


main()
