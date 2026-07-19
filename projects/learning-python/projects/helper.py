import os
import json

SAVE_FILE_DIR = os.path.curdir + "/data"


def input_y_or_n(pre_input) -> bool:
    try:
        raw = input(pre_input).strip().lower()
    except EOFError:
        return False

    if raw == "y":
        return True
    elif raw == "n":
        return False
    else:
        return input_y_or_n(pre_input)


def save_data(filename, data) -> None:
    os.makedirs(SAVE_FILE_DIR, 0o777, True)

    with open(SAVE_FILE_DIR + f"/{filename}", "w") as f:
        return json.dump(data, f)


def load_data(filename) -> dict:
    if os.path.exists(SAVE_FILE_DIR + f"/{filename}"):
        with open(SAVE_FILE_DIR + f"/{filename}", "r") as f:
            return json.load(f)
    return None
