# 8. Find and Replace in a File
def find_replace(filename, old_word, new_word):
    with open(filename, 'r') as file:
        content = file.read().replace(old_word, new_word)
    with open(filename, 'w') as file:
        file.write(content)
