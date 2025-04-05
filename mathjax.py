import re

def fix_inline_latex_spacing(markdown_text):
    # Match things like $ A $ but not $$ A $$
    pattern = r"(?<!\$)\$(\s*[^$\n]*?\s*)\$(?!\$)"

    def replacer(match):
        inner = match.group(1)
        fixed = inner.strip()
        return f"${fixed}$"

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
