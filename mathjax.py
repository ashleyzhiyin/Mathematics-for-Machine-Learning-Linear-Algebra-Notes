import re


def clean_inline_math(content: str) -> str:
    return f"${content.strip()}$"

def clean_display_math(content: str) -> str:
    # Fix \\ not followed by newline
    def fix_backslashes(match):
        if match.group(0).endswith('\n'):
            return match.group(0)
        return '\\\\\n'

    content = re.sub(r'\\\\(?!\s*\n)', fix_backslashes, content)

    # Trim spaces at start and end (not per line)
    return f"$${content.strip()}$$"

def clean_math_blocks(text: str) -> str:
    result = []
    last_pos = 0

    # Matches inline ($...$) and display ($$...$$)
    pattern = re.compile(
        r"(?P<display>\$\$(?:.|\n)*?\$\$)|(?P<inline>\$(?!\$)(?:\\\$|[^\n\$])+\$)"
    )

    for match in pattern.finditer(text):
        # Text before this match
        before = text[last_pos:match.start()]

        raw = match.group(0)
        cleaned = raw

        # Handle the case when there's no newline before $$ (add one)
        if match.group("display"):
            if not before.endswith('\n'):
                before += '\n'  # Add linebreak before display math

            # Remove indent before display math if it follows a linebreak
            before = re.sub(r'([^\S\r\n]*)$', '', before)  # remove trailing spaces
            if before.endswith('\n'):
                before = re.sub(r'(\n)[ \t]+$', r'\1', before)  # remove indent after linebreak

            inner = raw[2:-2]
            cleaned = clean_display_math(inner)
        elif match.group("inline"):
            inner = raw[1:-1]
            cleaned = clean_inline_math(inner)

        result.append(before)
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
