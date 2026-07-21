# ### 9. Markdown → HTML converter (subset)
# Convert a small Markdown subset to HTML.
# - **Requirements:** support `#`/`##`/`###` headings, `**bold**`, `*italic*`,
#   unordered lists, and paragraphs; read `input.md`, write `output.html`.
# - **You'll learn:** line-by-line parsing, `re.sub`, state machines (in-list or not).
# - **Stretch:** support links `[text](url)` and fenced code blocks.


import sys
import re


def get_folder_path(full_path=""):
    i = full_path.rfind("/")
    folder_path = full_path[: i + 1]
    return folder_path


def inline(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text


def convert(lines):
    html = []
    in_list = False

    for line in lines:
        line = line.rstrip("\n")

        if line.startswith("- "):
            if not in_list:
                html.append("<ul>")
                in_list = True
            item = inline(line[2:].strip())
            html.append(f"<li>{item}</li>")
            continue

        if in_list:
            html.append("</ul>")
            in_list = False

        if line.strip() == "":
            continue

        if line.startswith("### "):
            html.append(f"<h3>{inline(line[4:].strip())}</h3>")
        elif line.startswith("## "):
            html.append(f"<h2>{inline(line[3:].strip())}</h2>")
        elif line.startswith("# "):
            html.append(f"<h1>{inline(line[2:].strip())}</h1>")
        else:
            html.append(f"<p>{inline(line.strip())}</p>")

    if in_list:
        html.append("</ul>")

    return "\n".join(html) + "\n"


def main():
    cli_arguments = sys.argv

    if len(cli_arguments) < 2:
        return print("Error: Empty file argument")

    file_argument = cli_arguments[1]

    print("\nMark down to HTML program:")
    print(f"\nfile: {file_argument}\n")

    try:
        with open(file_argument) as f:
            lines = f.readlines()

        html = convert(lines)

        folder_path = get_folder_path(file_argument)
        output_path = folder_path + "output.html"

        with open(output_path, "w") as f:
            f.write(html)

        print(f"Wrote: {output_path}")

    except FileNotFoundError:
        print(f"Error: file not found: {file_argument}")
    except Exception as e:
        print(f"Error: {e}")


main()
