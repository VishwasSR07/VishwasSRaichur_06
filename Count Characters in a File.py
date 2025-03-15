# 7. Count Characters in a File
def count_characters(filename):
    with open(filename, 'r') as file:
        return len(file.read())
