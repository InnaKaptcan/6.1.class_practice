import math


class TfidfTransformer:

    def __init__(self):
        self.tf_result = None
        self.idf_result = None

    def tf_transform(self, count_matrix: list) -> list:
        total_nmb_of_words = sum(count_matrix[0])
        answ = []
        for i in count_matrix:
            answ.append(list(map(lambda x: round(x / total_nmb_of_words, 3), i)))
        self.tf_result = answ
        return self.tf_result

    def idf_transform(self, count_matrix: list) -> list:
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
                           math.log((total_nmb_of_docs + 1) / (x + 1)) + 1,
                           1),
                       res))
        self.idf_result = idf
        return self.idf_result

    def fit_transform(self, count_matrix: list) -> list:
        if self.tf_result is None:
            self.tf_transform(count_matrix)
        if self.idf_result is None:
            self.idf_transform(count_matrix)
        td_idf_matrix = []
        for row in self.tf_result:
            td_idf_matrix.append([round(x * y, 3) for x, y in zip(row, self.idf_result)])
        return td_idf_matrix


if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)

    print(tfidf_matrix)
