import re

def fix_inline_latex_spacing(markdown_text):
    # Match things like $ A $ but not $$ A $$
    pattern = r"(?<!\$)\$(\s*[^$\n]*?\s*)\$(?!\$)"

    def replacer(match):
        inner = match.group(1)
        fixed = inner.strip()
        return f"${fixed}$"

    return re.sub(pattern, replacer, markdown_text)

def fix_inline_double_dollar_spacing(markdown_text):
    # Match $$ ... $$ on a single line, with optional inner spaces
    pattern = re.compile(r"\$\$\s*([^$\n]+?)\s*\$\$")

    def replacer(match):
        inner = match.group(1).strip()
        return f"$${inner}$$"

    return pattern.sub(replacer, markdown_text)

def fix_indented_math_blocks(markdown_text):
    # Remove leading spaces before lines that contain only $$ or $$...$$
    return re.sub(r"^[ \t]+(\$\$)", r"\1", markdown_text, flags=re.MULTILINE)

# Example usage
if __name__ == "__main__":
    file = "Linear_Algebra_Notes.md"

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    content = fix_inline_latex_spacing(content)
    content = fix_inline_double_dollar_spacing(content)
    content = fix_indented_math_blocks(content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fixed Markdown written to {file}.")
