import re
import sys

def process_inline_math(text):
    """
    Process inline math blocks:
      - Remove spaces inside the math (only inside the $…$ delimiters).
      - If the math contains a \begin{...} environment, convert it to a display math block.
    """
    # Regex to match a single-dollar block that is not preceded or followed by another $
    pattern = re.compile(r'(?<!\$)\$(?!\$)(.*?)\$(?!\$)', re.DOTALL)

    def repl(match):
        content = match.group(1)
        # Remove leading/trailing spaces within the math delimiters
        new_content = content.strip()
        # If a \begin{…} environment is found, convert to a display math block.
        if r'\begin{' in new_content:
            # Force display mode: put $$ on separate lines.
            return "\n$$\n" + new_content + "\n$$\n"
        else:
            return "$" + new_content + "$"

    return pattern.sub(repl, text)

def process_display_math(text):
    """
    Process display math blocks (delimited by $$):
      - Unindent the block (remove leading whitespace from each line).
      - Remove extra linebreaks inside the block.
      - Ensure that the $$ markers are on their own lines.
    """
    # Match anything between $$ and $$
    pattern = re.compile(r'\$\$(.*?)\$\$', re.DOTALL)

    def repl(match):
        content = match.group(1)
        # Split into lines and remove leading spaces from each line.
        lines = [line.lstrip() for line in content.splitlines()]
        # Remove extra blank lines: keep only nonempty lines.
        lines = [line for line in lines if line.strip() != '']
        new_content = "\n".join(lines)
        # Reformat with $$ on its own lines.
        return "\n$$\n" + new_content + "\n$$\n"

    return pattern.sub(repl, text)

def adjust_blank_lines_around_display_math(text):
    """
    Adjusts blank lines around display math blocks (i.e. the $$ delimiter lines)
    so that there is exactly one blank line before the starting $$ and one after
    the ending $$.
    """
    lines = text.splitlines()
    output_lines = []
    in_math_block = False  # Flag to track if we're inside a display math block

    i = 0
    while i < len(lines):
        line = lines[i]
        # Detect a line that contains only "$$" (possibly with surrounding whitespace)
        if line.strip() == "$$":
            if not in_math_block:
                # Start of a math block:
                # If the previous line exists and is not blank, insert a blank line.
                if output_lines and output_lines[-1].strip() != "":
                    output_lines.append("")
                output_lines.append("$$")
                in_math_block = True
            else:
                # End of a math block:
                output_lines.append("$$")
                # If there is a next line and it's not blank, insert a blank line.
                if i + 1 < len(lines) and lines[i + 1].strip() != "":
                    output_lines.append("")
                in_math_block = False
        else:
            output_lines.append(line)
        i += 1

    return "\n".join(output_lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py filename.md")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        sys.exit(1)

    # Process inline math blocks
    text = process_inline_math(text)
    # Process display math blocks (unindent, reformat, remove extra linebreaks)
    text = process_display_math(text)
    # Adjust blank lines around display math blocks
    text = adjust_blank_lines_around_display_math(text)

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
