# 13. Handle ValueError in Input
def safe_input():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        return "Invalid input, expected a number!"
