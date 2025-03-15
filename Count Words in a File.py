# 6. Count Words in a File
def count_words(filename):
    with open(filename, 'r') as file:
        return len(file.read().split())
