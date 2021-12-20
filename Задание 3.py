import math


def idf_transform(count_matrix: list) -> list:
    """Создадим матрицу word_appearance_matrix, в которой 1 означает, что слово
    присутствует в документе, а 0, что отсутствует. Затем посчитаем количество
    документов с каждым словом, сложив поэлементно внутренние списки
    списка word_appearance_matrix"""
    total_nmb_of_docs = len(count_matrix)
    total_nmb_of_distinct_words = len(count_matrix[0])

    word_appearance_matrix = count_matrix
    for i in word_appearance_matrix:
        for j, elem in enumerate(i):
            if elem != 0:
                i[j] = 1

    res = []
    for i in range(total_nmb_of_distinct_words):
        k = sum([elem[i] for elem in word_appearance_matrix])
        res.append(k)

    idf = list(map(lambda x:
                   round(
                       math.log((total_nmb_of_docs + 1)/(x + 1)) + 1,
                       1),
                   res))
    return idf


if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    print(idf_transform(count_matrix))

