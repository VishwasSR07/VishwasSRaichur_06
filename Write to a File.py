# 2. Write to a File
def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
