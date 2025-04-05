import re

def clean_math_blocks(math_text):
    # Case 1: If the double dollar block is indented, unindent it.
    math_text = re.sub(r'^\s*\$\$(.*?)\$\$', r'$$\1$$', math_text, flags=re.DOTALL)

    # Case 2: If double dollar does not occupy its own line, make it do so.
    math_text = re.sub(r'\$\$(.*?)\$\$', r'\n$$\1$$\n', math_text, flags=re.DOTALL)

    # Case 3: If there are spaces between single dollar sign and the math, remove them.
    # Note: This won't interfere with spaces outside the math expressions
    math_text = re.sub(r'(\$) (\S.*?) (\$)', r'\1\2\3', math_text)

    # Case 4: If there are extra line breaks inside the double dollar block, remove them.
    math_text = re.sub(r'\$\$(.*?)\$\$', lambda m: '$$\n' + re.sub(r'\n+', '\n', m.group(1).strip()) + '\n$$', math_text, flags=re.DOTALL)

    return math_text

# Example usage
if __name__ == "__main__":
    file = "Linear_Algebra_Notes.md"

    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    content = clean_math_blocks(content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Fixed Markdown written to {file}.")
