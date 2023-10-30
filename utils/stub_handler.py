import re
import os

def extract_template_vars_with_indent(stub_content):
    templates = []
    for match in re.finditer(r'(.*?[^{])\{{{(.*?)\}}}', stub_content):
        before_content = match.group(1)
        template_name = match.group(2)
        templates.append([before_content, template_name, before_content + "{{{" + template_name + "}}}"])
    return templates


def compile_stub_with_content(file):
    with open(f'stubs/{file}.stub', 'r') as f:
        stub_content = f.read()

    templates = extract_template_vars_with_indent(stub_content)
    for indent, template_name, template_string in templates:
        content_path = os.path.join('prompts', f"{template_name}.md")
        if os.path.exists(content_path):
            with open(content_path, 'r') as f:
                content_data = f.read()

            indented_content = '\n'.join([indent + line for line in content_data.splitlines()])

            stub_content = stub_content.replace(template_string, indented_content)
        else:
            print(f"Warning: File {content_path} does not exist.")

    with open(f'{file}.md', 'w') as f:
        f.write(stub_content)

compile_stub_with_content("README")
