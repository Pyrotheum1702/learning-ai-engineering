# ### 8. Expense tracker with CSV export
# Log expenses (date, category, amount, note).
# - **Requirements:** add an expense; list all; show a total per category; export
#   to `expenses.csv`; amounts validated as positive numbers.
# - **You'll learn:** `csv` module, `datetime`, grouping/aggregation with dicts.
# - **Stretch:** filter by month; simple bar chart in the terminal (text bars).

import random
import string
from collections import Counter
from datetime import datetime
from helper import save_data, load_data, export_csv

DEV = True
state = {"expenses": []}


def validate_amount(value):
    if type(value) != float:
        return False
    if value <= 0:
        return False
    if value >= 1000000000000:
        return False
    return True


def input_name():
    while True:
        raw = input("  name: ")
        try:
            if not raw.isalpha():
                print(f"Invalid value: {raw}")
                continue

            return raw
        except ValueError as e:
            print(f"Invalid value: {raw}")


def input_amount():
    while True:
        raw = input("  amount: ")
        try:
            amount = float(raw)
            amount_valid = validate_amount(amount)
            if not amount_valid:
                print(f"Invalid value: {amount}")
                continue

            return amount
        except ValueError as e:
            print(f"Invalid value: {raw}")


def input_category():
    while True:
        raw = input("  category: ")
        try:
            if raw == "":
                return raw

            if not raw.isalpha():
                print(f"Invalid value: {raw}")
                continue

            return raw
        except ValueError as e:
            print(f"Invalid value: {raw}")


def get_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # return datetime.date.isoformat()


def input_note():
    raw = input("  note: ")
    return raw


def add(command_argument=""):
    # seg = command_argument.split(" ")
    expense = {}

    sequence_order = [
        ["name", input_name],
        ["category", input_category],
        ["amount", input_amount],
        ["note", input_note],
        ["date", get_date],
    ]

    for item in sequence_order:
        expense[item[0]] = item[1]()

    state["expenses"].append(expense)
    save_data("expense_tracker.json", state["expenses"])

    print(f"expense added: {expense}")

    if DEV:
        print(state["expenses"])

    return


def list(command_argument=""):
    list_data = state["expenses"]
    total_count = len(list_data)
    total_amount = sum(e.get("amount", 0) for e in list_data)

    print(f"=== total: expenses: {total_count} - amount: {total_amount}$ ===")
    sorted_list = sorted(list_data, key=lambda e: e["amount"], reverse=True)

    for i, item in enumerate(sorted_list):
        string = f"{i+1}"
        string += f" - name: {item['name']}"
        string += f" - category: {item['category']}"
        string += f" - amount: {item['amount']}$"
        string += f" - date: {item['date']}"

        print(string)

    sorted_by_category = sorted(list_data, key=lambda e: e["category"], reverse=True)
    last_category = None

    print(f"=== expenses by category ===")

    i = 0
    block_count = 30

    for item in sorted_by_category:
        if item["category"] != last_category:
            cat = item["category"]
            items = [e for e in sorted_by_category if e["category"] == cat]
            amount = sum(e["amount"] for e in items)

            block = ""
            for x in range(max(1, round(amount / total_amount * block_count))):
                block += "█"

            print(f"  {cat:12} {block:{block_count}}  ${amount:.2f}")
            last_category = cat
            i += 1

    return


def export(command_argument=""):
    export_succeed = export_csv(
        "expense_tracker.csv",
        state["expenses"],
        ["name", "category", "amount", "note", "date"],
        True,
    )

    print(f"Export {'success.' if export_succeed else 'failed.'}")
    return


def quit(command_argument=""):
    save_data("expense_tracker.json", state["expenses"])
    print("Saved. Bye.\n")
    exit()
    return


commands = {
    "add": add,
    "list": list,
    "export": export,
    "quit": quit,
}

comments = {
    "add": "Add new expense.",
    "list": "List all expenses.",
    "export": "Export to expenses.scv",
    "quit": "Quit the program.",
}


def loop():
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
            commands[seg[0]](command_value)
        else:
            commands[seg[0]]()
    except Exception as e:
        print(f"Error: {e}")
        # if DEV:
        #     print(f"Cause: {e.args}")
        print("======")
        return loop()

    loop()


def main():
    print("Expense tracker program.")
    print("Commands:")

    state["expenses"] = load_data("expense_tracker.json", DEV) or []

    for key, value in commands.items():
        print(f"{key}: {comments[key]}")

    loop()


main()
