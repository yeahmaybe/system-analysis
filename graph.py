data = open("graph.csv", "r")

line = data.readline()
lineIdx = 0

while line != "":
    vertices = list(map(int, line.split(",")))
    print("Вершина {0}: ".format(lineIdx + 1), end="")
    for i, vertex in enumerate(vertices):
        if vertex == 1:
            print(i + 1, end=" ")

    print()
    lineIdx += 1
    line = data.readline()
