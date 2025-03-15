# 3. Append to a File
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)
