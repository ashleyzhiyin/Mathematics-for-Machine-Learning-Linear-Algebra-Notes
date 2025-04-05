import re

def clean_inline_math(content: str) -> str:
    # Just strip leading/trailing space inside inline math
    return f"${content.strip()}$"

def clean_display_math(content: str) -> str:
    # Fix only the \\ that are not followed by a newline
    def fix_backslashes(match):
        # If already followed by newline, leave it
        if match.group(0).endswith('\n'):
            return match.group(0)
        return '\\\\\n'

    # Fix only those \\ that are NOT followed by a newline already
    content = re.sub(r'\\\\(?!\s*\n)', fix_backslashes, content)

    # Trim spaces at start/end of the entire block (but NOT per line)
    return f"$${content.strip()}$$"

def clean_math_blocks(text: str) -> str:
    result = []
    last_pos = 0

    # Match inline ($...$) and display ($$...$$) math blocks
    pattern = re.compile(
        r"(?P<display>\$\$(?:.|\n)*?\$\$)|(?P<inline>\$(?!\$)(?:\\\$|[^\n\$])+\$)"
    )

    for match in pattern.finditer(text):
        result.append(text[last_pos:match.start()])
        raw = match.group(0)

        if match.group("display"):
            inner = raw[2:-2]
            cleaned = clean_display_math(inner)
            result.append(cleaned)
        elif match.group("inline"):
            inner = raw[1:-1]
            cleaned = clean_inline_math(inner)
            result.append(cleaned)

        last_pos = match.end()

    result.append(text[last_pos:])
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
