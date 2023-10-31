import re
from os import path

re_stub = re.compile(r'([ \t]*)(\{{{\s*(.*?)\s*}}})')

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_template(indent, var, file):
    return (indent, indent + var, read_file(f"prompts/{file}.md") )

def compile_stub_with_content(file):
    stub = read_file(f'stubs/{file}.stub')

    for indent, tag, content in [get_template(*m.groups()) for m in re_stub.finditer(stub)]:
        indented_content = '\n'.join(indent+line for line in content.splitlines())
        stub = stub.replace(tag, indented_content)
    with open(f'{file}.md', 'w') as f:
        f.write(stub)

if __name__ == "__main__":
    compile_stub_with_content("instructions")
    compile_stub_with_content("coding")
    compile_stub_with_content("prompts")
    compile_stub_with_content("README")
