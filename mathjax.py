import re

def clean_inline_math(content: str) -> str:
    # Trim leading/trailing spaces inside inline math
    return f"${content.strip()}$"

def clean_display_math(content: str) -> str:
    # Normalize `\\` to have exactly one newline after
    # BUT preserve existing line structure
    def fix_backslashes(line):
        # Only fix `\\` followed by anything that’s not a newline
        return re.sub(r'\\\\(?!\s*\n)', r'\\\\\n', line)

    # Split into lines and trim spaces (keep empty lines)
    lines = content.splitlines()
    cleaned_lines = [fix_backslashes(line.rstrip()) for line in lines]

    return "$$" + "\n".join(cleaned_lines) + "$$"

def clean_math_blocks(text: str) -> str:
    result = []
    pos = 0

    # Pattern matches either display or inline math
    pattern = re.compile(
        r"(?P<display>\$\$(?:.|\n)*?\$\$)|(?P<inline>\$(?!\$)(?:\\\$|[^\n\$])+\$)"
    )

    for match in pattern.finditer(text):
        result.append(text[pos:match.start()])
        raw = match.group(0)

        if match.group("display"):
            inner = raw[2:-2]
            cleaned = clean_display_math(inner)
            result.append(cleaned)
        elif match.group("inline"):
            inner = raw[1:-1]
            cleaned = clean_inline_math(inner)
            result.append(cleaned)

        pos = match.end()

    result.append(text[pos:])
    return ''.join(result)

# Example usage
if __name__ == "__main__":
    file = "Linear_Algebra_Notes.md"

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    content = clean_math_blocks(content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fixed Markdown written to {file}.")
