import re

def fix_inline_latex_spacing(markdown_text):
    # This regex matches anything like $ something $ (with optional whitespace inside)
    pattern = r"\$(\s+[^$]+?\s+)\$"

    # This function trims the spaces between the dollar signs and the content
    def replacer(match):
        content = match.group(1).strip()
        return f"${content}$"

    return re.sub(pattern, replacer, markdown_text)


# Example usage
if __name__ == "__main__":
    file = "Linear_Algebra_Notes.md"

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    fixed_content = fix_inline_latex_spacing(content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(fixed_content)

    print(f"Fixed Markdown written to {file}.")
