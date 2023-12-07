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
    #print(clusters)
    return clusters


def get_matrix_from_expert(str_json: str):
    matrix = []
    n = 0

    clusters = get_clusters_from_str(str_json)
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


def get_kendell(experts):
    m = len(experts)
    n = len(experts[0])

    rank_matrix = [[0 for _ in range(len(experts))] for _ in range(len(experts[0]))]
    for i, expert in enumerate(experts):
        for j, obj in enumerate(expert):
            rank_matrix[j][i] = len(obj) - np.sum(obj) + 1


    H=0
    for i in range(m):
        d = {}
        for obj in rank_matrix:
            if d.get(obj[i]) is None: d[obj[i]] = 0
            d[obj[i]] = d[obj[i]] + 1
        for k in d:
            H += d[k]**3 - d[k]
        for j, obj in enumerate(rank_matrix):
            rank_matrix[j][i] = rank_matrix[j][i] + (d[obj[i]]-1)/2


    Xmean = np.sum(rank_matrix) / n

    S = 0
    for obj_ranks in rank_matrix:
        Xi = np.sum(obj_ranks)
        S += (Xi - Xmean) ** 2

    Dmax = (m*m * (n**3 - n) - m*H) / 12

    #print("S: ", S)
    #print("Dmax: ", Dmax)
    return S / Dmax


def task(strA: str, strB: str):

    matrixF = get_matrix_from_expert(strA)
    matrixG = get_matrix_from_expert(strB)
    experts = [matrixG, matrixF]
    res = get_kendell(experts)
    return res


if __name__ == "__main__":
    print(
        task("[1,[2,3],4,[5,6,7],8,9,10]",
        "[[1,2],[3,4,5],6,7,9,[8,10]]")
    )
