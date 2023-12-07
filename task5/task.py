import json

import numpy as np


def get_clusters_from_str(str_json):
    str_json = str(str_json[1:-1])
    str_split = str_json.split(",")
    clusters = []
    cluster_read = False
    for substr in str_split:
        current_cluster = cluster_read
        if '[' in substr:
            substr = substr[1:]
            cluster_read = True
        if ']' in substr:
            substr = substr[:-1]
            cluster_read = False

        if not current_cluster:
            clusters.append([int(substr)])
        else:
            clusters[-1].append(int(substr))
    return clusters


def get_matrix_from_expert(str_json: str):
    matrix = []
    n = 0

    clusters = get_clusters_from_str(str_json)
    # clusters = json.loads(str_json)["str"]
    for cluster in clusters:
        n += len(cluster)
    for i in range(n):
        matrix.append([1] * n)

    worse = []
    for cluster in clusters:
        for worse_elem in worse:
            for elem in cluster:
                matrix[elem - 1][worse_elem - 1] = 0
        for elem in cluster:
            worse.append(int(elem))

    return np.array(matrix)


def get_AND_matrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    matrix = []
    for row in range(rows):
        matrix.append([0] * cols)

    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = matrix1[row][col] * matrix2[row][col]

    return np.array(matrix)


def get_OR_matrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    matrix = []
    for row in range(rows):
        matrix.append([0] * cols)

    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = max(matrix1[row][col], matrix2[row][col])

    return matrix


def get_clusters(matrix, est1, est2):
    clusters = {}

    rows = len(matrix)
    cols = len(matrix[0])
    exclude=[]
    for row in range(rows):
        if row+1 in exclude:
            continue
        clusters[row + 1] = [row + 1]
        for col in range(row+1, cols):
            if matrix[row][col] == 0:
                clusters[row + 1].append(col + 1)
                exclude.append(col+1)

    result = []
    for k in clusters:
        if not result:
            result.append(clusters[k])
            continue
        # если сумма единичек меньше, а справа стоит объект с меньшей, значит объект левее
        for i, elem in enumerate(result):
            # если объекты неразличимы в обоих оценках, то добавляяем в кластер вершины
            if np.sum(est1[elem[0] - 1]) == np.sum(est1[k - 1]) and np.sum(est2[elem[0] - 1]) == np.sum(est2[k - 1]):
                for c in clusters[k]:
                    result[i].append(c)
                    break

            if np.sum(est1[elem[0] - 1]) < np.sum(est1[k - 1]) or np.sum(est2[elem[0] - 1]) < np.sum(est2[k - 1]):
                result = result[:i] + clusters[k] + result[i:]
                break
        result.append(clusters[k])

    final = []
    for r in result:
        if len(r) == 1:
            final.append(r[0])
        else:
            final.append(r)
    return str(final)


def task(string1, string2):
    mx1 = get_matrix_from_expert(string1)
    mx2 = get_matrix_from_expert(string2)

    mxAND = get_AND_matrix(mx1, mx2)
    mxAND_T = get_AND_matrix(np.transpose(mx1), np.transpose(mx2))

    mxOR = get_OR_matrix(mxAND, mxAND_T)
    clusters = get_clusters(mxOR, mx1, mx2)
    return clusters


if __name__ == "__main__":
    string1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    string2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'
    results = task(string1, string2)
    print(results)

