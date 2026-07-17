# Requirement:

### 3. Command-line to-do list (in-memory)
# Add, list, and remove tasks during a single run.
# - **Requirements:** commands `add <text>`, `list`, `done <n>`, `quit`; tasks stored
#   in a list; `list` shows numbered items with a ✓ for completed ones.
# - **You'll learn:** lists, string parsing (`str.split`), enumerate, program loop design.
# - **Stretch:** persist across runs (foreshadows #6).

import json
import os

list_data = {}

SAVE_FILE_DIR = os.path.curdir + "/data"
SAVE_FILE_PATH = SAVE_FILE_DIR + "/tasks.json"


def save_list_data() -> None:
    os.makedirs(SAVE_FILE_DIR, 0o777, True)

    with open(SAVE_FILE_PATH, "w") as f:
        return json.dump(list_data, f)


def load_list_data() -> dict:
    if os.path.exists(SAVE_FILE_PATH):
        with open(SAVE_FILE_PATH, "r") as f:
            return json.load(f)
    return {}


def add(item_name) -> None:
    if item_name in list_data.keys():
        raise KeyError("Task already exist.")

    list_data[item_name] = False


def remove(item_name) -> None:
    if item_name not in list_data.keys():
        raise KeyError("Task not found.")

    del list_data[item_name]


def clear() -> None:
    list_data.clear()


def list() -> None:
    if len(list_data) < 1:
        raise ValueError("To do list is empty.")

    for key, value in list_data.items():
        print(f"{key}: {'✔' if value is True else '✘'}")


def done(item_name) -> None:
    if item_name not in list_data.keys():
        raise KeyError("Task not found.")

    if list_data[item_name] is True:
        raise ValueError("Task is already done.")

    list_data[item_name] = True


def quit() -> None:
    return exit()


commands = {
    "add": add,
    "list": list,
    "done": done,
    "remove": remove,
    "clear": clear,
    "quit": quit,
}

comments = {
    "add": "Add task to the list.",
    "list": "Get the list.",
    "done": "Check done for the task.",
    "remove": "Remove task from the list.",
    "clear": "Clear the task list entirely.",
    "quit": "Quit the program.",
}


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
            commands[seg[0]](command_value)
        else:
            commands[seg[0]]()
    except Exception as e:
        print(f"Error: {e}")
        return loop()

    save_list_data()

    loop()


def main() -> None:
    global list_data

    list_data = load_list_data()

    print("Commands:")

    for key, value in commands.items():
        print(f"{key}: {comments[key]}")

    loop()


main()
