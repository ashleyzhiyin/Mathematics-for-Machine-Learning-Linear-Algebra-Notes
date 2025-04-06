import re
from pathlib import Path

def fix_math_blocks(text):
    # Step 1 & 2: Normalize double dollar blocks
    def normalize_double_dollars(match):
        content = match.group(1)
        # Remove extra line breaks and leading/trailing whitespace from each line
        lines = content.strip().splitlines()
        cleaned_lines = [line.strip() for line in lines if line.strip() != '']
        return '$$\n' + '\n'.join(cleaned_lines) + '\n$$'

    # First ensure all double-dollar blocks are isolated on their own lines and unindented
    text = re.sub(r'^[ \t]*\$\$[ \t]*\n(.*?\n)[ \t]*\$\$[ \t]*$', lambda m: f'$$\n{m.group(1).strip()}\n$$', text, flags=re.DOTALL | re.MULTILINE)

    # Then normalize their contents
    text = re.sub(r'\$\$\n(.*?)\n\$\$', normalize_double_dollars, text, flags=re.DOTALL)

    # Step 3: Normalize inline math spacing
    def fix_inline_math(match):
        inner = match.group(1)
        return f'${inner.strip()}$'

    # Only modify spaces inside $...$ blocks, but avoid $$ blocks
    text = re.sub(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', fix_inline_math, text)

    return text

def process_markdown_file(filepath):
    path = Path(filepath)
    original_text = path.read_text(encoding='utf-8')
    fixed_text = fix_math_blocks(original_text)
    path.write_text(fixed_text, encoding='utf-8')
    print(f"Processed: {filepath}")

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python fix_mathjax.py <markdown_file.md>")
    else:
        process_markdown_file(sys.argv[1])