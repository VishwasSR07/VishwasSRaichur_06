# 1. Read a File
def read_file(filename):
    with open(filename, 'r') as file:
        print(file.read())
