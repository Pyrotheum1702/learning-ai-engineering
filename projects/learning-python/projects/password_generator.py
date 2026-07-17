# ### 4. Password generator
# Generate a random password of a requested length.
# - **Requirements:** let the user choose length and whether to include digits and
#   symbols; guarantee at least one of each requested category; never produce a
#   password shorter than requested.
# - **You'll learn:** `random.choice`/`secrets`, string constants, input validation.
# - **Stretch:** estimate and print entropy in bits; use `secrets` for real randomness.

import secrets
import string
import math

LENGTH_MIN = 4
LENGTH_MAX = 32


def input_length() -> int:
    raw = input("\nlength: ")

    pass_len = 0

    try:
        pass_len = int(raw)
    except ValueError:
        print("Please enter a whole number.")
        return input_length()

    if pass_len < LENGTH_MIN or pass_len > LENGTH_MAX:
        print(f"Out of range ({LENGTH_MIN}-{LENGTH_MAX}).")
        return input_length()

    return pass_len


def input_use_digits() -> bool:
    raw = input("include digits? (y/n): ")

    if raw == "y" or raw == "Y":
        return True
    elif raw == "n" or raw == "N":
        return False
    else:
        return input_use_digits()


def input_use_symbols() -> bool:
    raw = input("include symbols (y/n): ")

    if raw == "y" or raw == "Y":
        return True
    elif raw == "n" or raw == "N":
        return False
    else:
        return input_use_symbols()


def input_redo() -> bool:
    raw = input("Generate another one? (y/n): ")

    if raw == "y" or raw == "Y":
        return True
    elif raw == "n" or raw == "N":
        return False
    else:
        return input_redo()


def generate_random_password(rand_set, length):
    password = ""

    for i in range(length):
        password += secrets.choice(rand_set)

    return password


def get_entropy_bits(rand_set_length, length):
    return length * math.log2(rand_set_length)


def loop():
    try:
        random_set = string.ascii_letters

        length = input_length()
        use_digit = input_use_digits()
        use_symbols = input_use_symbols()

        if use_digit:
            random_set += string.digits
        if use_symbols:
            random_set += string.punctuation

        password = ""

        while True:
            password = generate_random_password(random_set, length)
            set_pass = set(password)

            if not set_pass & set(string.ascii_letters):
                continue
            if use_digit and not set_pass & set(string.digits):
                continue
            if use_symbols and not set_pass & set(string.punctuation):
                continue

            break

        entropy_bits = get_entropy_bits(len(random_set), length)

        print(f"\nEntropy bits: {entropy_bits:.1f}")
        print(f"Generated password: {password}\n\n")

        redo = input_redo()

        if redo:
            loop()
    except Exception as e:
        print(f"Error: {e}")
        return loop()


def main():
    print("\nProgram: Password Generator")
    print(
        f"Generate randomized ({LENGTH_MIN}-{LENGTH_MAX}) length password of characters, digits and symbols are optional.\n"
    )

    loop()


main()
