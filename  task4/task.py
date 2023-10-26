import numpy as np


def get_probabilities(frequency_matrix):
    probabilities = []
    n = len(frequency_matrix[0])
    for line in frequency_matrix:
        result = []
        for cell in line:
            result.append(cell / n)
        probabilities.append(result)

    return probabilities


def get_entropies(frequency_matrix):
    probability_matrix = get_probabilities(frequency_matrix)
    entropy_matrix = []
    for i in range(len(frequency_matrix)):
        entropy_matrix.append([0] * len(frequency_matrix[0]))
    for l, line in enumerate(probability_matrix):
        for c, Plc in enumerate(line):
            Hlc = 0
            if Plc != 0: Hlc = - Plc * np.log2(Plc)
            entropy_matrix[l][c] = Hlc
    return entropy_matrix


def get_Ha(frequency_matrix):
    prob_matrix = get_probabilities(frequency_matrix)
    summ = 0
    for line in prob_matrix:
        p = np.sum(line)
        summ -= p * np.log2(p)
    return summ


def get_Hb(frequency_matrix):
    prob_matrix = get_probabilities(frequency_matrix)
    summ = 0
    prob_matrix_T = np.transpose(prob_matrix)
    for line in prob_matrix_T:
        p = np.sum(line)
        if p != 0: summ -= p * np.log2(p)
    return summ


def get_HAB(frequency_matrix):
    return np.sum(get_entropies(frequency_matrix))


def task():
    matrix = []
    for i in range(2, 13):
        matrix.append([0] * 36)

    for fst in range(1, 7):
        for snd in range(fst, 7):
            matrix[fst + snd - 2][fst * snd - 1] += 1 + int(fst != snd)
    Ha = get_Ha(matrix)
    Hb = get_Hb(matrix)
    HAB = get_HAB(matrix)
    HaB = HAB - Ha
    Iab = Hb - HaB
    return " Ha: {0}\n Hb: {1}\n HaB: {2}\n HAB: {3}\n Iab: {4}".format(Ha, Hb, HaB, HAB, Iab)


if __name__ == "__main__":
    print(task())
