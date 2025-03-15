# 9. Read File Line by Line
def read_line_by_line(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
