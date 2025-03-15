# 14. Handle Multiple Exceptions
def handle_multiple_exceptions(filename):
    try:
        with open(filename, 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return "File not found!"
    except ValueError:
        return "Invalid data in file!"
