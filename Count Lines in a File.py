# 5. Count Lines in a File
def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())
