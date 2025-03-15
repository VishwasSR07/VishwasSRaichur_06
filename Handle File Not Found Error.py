# 11. Handle File Not Found Error
def safe_read(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found!"
