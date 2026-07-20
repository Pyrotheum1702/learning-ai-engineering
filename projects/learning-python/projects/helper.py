import os
import csv
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


def save_data(filename, data, log_failure=False) -> bool:
    filepath = os.path.join(SAVE_FILE_DIR, filename)
    temp_path = filepath + ".tmp"

    try:
        text = json.dumps(data)
    except (TypeError, ValueError) as e:
        print(f"Save failed ({filename}): data is not JSON-serializable - {e}")
        return False

    try:
        os.makedirs(SAVE_FILE_DIR, 0o777, True)

        with open(temp_path, "w") as f:
            f.write(text)

        os.replace(temp_path, filepath)
        return True
    except OSError as e:
        if log_failure:
            print(f"Save failed ({filename}): {e}")

        try:
            os.remove(temp_path)
        except OSError:
            pass

        return False


def load_data(filename, log_failure=False):
    filepath = os.path.join(SAVE_FILE_DIR, filename)

    if not os.path.exists(filepath):
        return None

    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        if log_failure:
            print(f"Load failed ({filename}): file is not valid JSON - {e}")
        return None
    except OSError as e:
        if log_failure:
            print(f"Load failed ({filename}): {e}")
        return None


def export_csv(filename, data, fieldnames, log_failure=False) -> bool:
    filepath = os.path.join(SAVE_FILE_DIR, filename)
    temp_path = filepath + ".tmp"

    if isinstance(data, dict):
        rows = list(data.values())
    else:
        rows = list(data)

    try:
        os.makedirs(SAVE_FILE_DIR, 0o777, True)

        with open(temp_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)

        os.replace(temp_path, filepath)
        return True
    except ValueError as e:
        if log_failure:
            print(f"Export failed ({filename}): row does not match fieldnames - {e}")
    except OSError as e:
        if log_failure:
            print(f"Export failed ({filename}): {e}")

    try:
        os.remove(temp_path)
    except OSError:
        pass

    return False
