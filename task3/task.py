from task2.task import task as t2
import numpy as np

def task(matrix_csv: str):
    matrix = []
    lines = matrix_csv.split("\n")
    for line in lines:
        matrix.append(list(map(int, line.split(","))))

    n = len(matrix)
    H = 0
    for row in matrix:
        for num in row:
            p = num / (n-1)
            if p>0: H -= p * np.log2(p)

    return H

if __name__ == "__main__":
    result2 = t2("1,2\n2,3\n2,6\n3,4\n3,5")
    result3 = task(result2)
    print(result3)