# ### 5. Word & character counter
# Read a text file and report statistics.
# - **Requirements:** take a filename as a CLI argument; print line count, word
#   count, char count, and the 5 most common words; handle "file not found".
# - **You'll learn:** file reading, `sys.argv`, `collections.Counter`, error handling.
# - **Stretch:** ignore stop-words; case-insensitive counting; strip punctuation.

import sys
import collections
import string

STOP_WORDS = {"the", "a", "an", "and", "or", "is", "was", "in", "of", "to", "it"}


def main():
    cli_arguments = sys.argv

    if len(cli_arguments) < 2:
        return print("Error: Empty file argument")

    file_argument = cli_arguments[1]

    print("\nWord and character counter program:")
    print(f"\nfile: {file_argument}\n")

    table = str.maketrans("", "", string.punctuation)

    try:

        with open(file_argument) as f:
            line_count = 0
            word_count = 0
            char_count = 0

            words = []

            for line in f:
                line_count += 1
                char_count += len(line)
                for word in line.split():
                    word = word.translate(table).lower()
                    if word and word not in STOP_WORDS:
                        word_count += 1
                        words.append(word)

            common_words = collections.Counter(words).most_common(5)

            print(f"line count: {line_count}")
            print(f"word count: {word_count}")
            print(f"char count: {char_count}")
            print(f"\n5 most common words:")

            count = 1
            for item in common_words:
                print(f"{count}: {item[0]} - {item[1]}")

                count += 1

            print("")

    except FileNotFoundError:
        print(f"Error: file not found: {file_argument}")
    except Exception as e:
        print(f"Error: {e}")


main()
