import re

def clean_math_blocks(text):
    # Step 1: Fix display math blocks $$...$$
    def fix_display_math(match):
        content = match.group(1)

        # Normalize all \\ to have exactly one newline after them
        content = re.sub(r"\\\\[ \t]*(?:\r?\n)*", r"\\\\\n", content)

        # Strip leading/trailing spaces per line
        lines = content.splitlines()
        cleaned_lines = [line.strip() for line in lines]

        return "\n$$\n" + "\n".join(cleaned_lines).strip() + "\n$$"

    # Replace all $$...$$ blocks (multiline)
    text = re.sub(
        r"\$\$(.*?)\$\$", fix_display_math, text, flags=re.DOTALL
    )

    # Step 2: Fix inline math $...$
    def fix_inline_math(match):
        content = match.group(1)
        return f"${content.strip()}$"

    text = re.sub(r"\$(?!\$)\s*(.+?)\s*\$", fix_inline_math, text)

    return text

# Example usage
if __name__ == "__main__":
    file = "Linear_Algebra_Notes.md"

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    content = clean_math_blocks(content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fixed Markdown written to {file}.")
