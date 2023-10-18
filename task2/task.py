def task(edges_csv: str):
    edges = edges_csv.split('\n')
    matrix = []

    for edge in edges:
        sup, inf = map(int, edge.split(','))
        sup -= 1
        inf -= 1
        while sup > len(matrix) - 1 or inf > len(matrix) - 1:
            matrix.append([0, 0, 0, 0, 0])

        matrix[sup][0] += 1
        matrix[inf][1] += 1

    for edge in edges:
        sup, inf = map(int, edge.split(','))
        sup -= 1
        inf -= 1
        matrix[sup][2] += matrix[inf][0]
        matrix[inf][3] += matrix[sup][1]
        matrix[inf][4] += matrix[sup][0] - 1

    result = ""
    for row in matrix:
        for col in row:
            result+= str(col)+","
        result = result[:-1]+"\n"

    return result[:-1]

# 1
#  \
#   2
#  /  \
#  3    6
#  |  \
#  4    5

if __name__ == "__main__":
    print(task("1,2\n2,3\n2,6\n3,4\n3,5"))
