import sys

path = str(sys.argv[1])
lineIdx = int(sys.argv[2])
columnIdx = int(sys.argv[3])


def get_line(table, line_idx):
    i = 0
    line = table.readline()
    while i < line_idx:
        line = table.readline()
        i += 1
    if line is not None:
        split_line = line.split(",")
    else:
        split_line = None
    return split_line


def get_cell(split_line, column_idx):
    if len(split_line) > column_idx:
        value = split_line[columnIdx]
    else:
        value = None
    return value


if __name__ == '__main__':

    if columnIdx >= 0 and lineIdx >= 0:
        data = open(path, "r")
        cells = get_line(data, lineIdx)
        result = get_cell(cells, columnIdx)
    else:
        result = None

    print(result)
