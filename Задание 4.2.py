import math


class CountVectorizer:
    def __init__(self):
        self.feature_names = []

    def build_feature_names(self, text):
        """Создание списка всех уникальных слов текста"""
        for paragraph in text:
            for word in paragraph.split(' '):
                word = word.lower()
                if word not in self.feature_names:
                    self.feature_names.append(word)

    def get_feature_names(self):
        return self.feature_names

    def cv_fit_transform(self, text):
        self.build_feature_names(text)

        words_with_seq_numbers = {}
        for i, elem in enumerate(self.feature_names):
            words_with_seq_numbers[elem] = i

        answ = []
        for paragraph in text:
            dict = {}
            for i in words_with_seq_numbers.values():
                dict[i] = 0
            for word in paragraph.split(' '):
                word = word.lower()
                dict[words_with_seq_numbers[word]] += 1
            answ.append(list(dict.values()))
        return answ


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

    def tf_idf_fit_transform(self, count_matrix: list) -> list:
        if self.tf_result is None:
            self.tf_transform(count_matrix)
        if self.idf_result is None:
            self.idf_transform(count_matrix)

        td_idf_matrix = []
        for row in self.tf_result:
            td_idf_matrix.append([round(x * y, 3) for x, y in zip(row, self.idf_result)])
        return td_idf_matrix


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tf_idf = TfidfTransformer()

    def fit_transform(self, text):
        count_matrix = self.cv_fit_transform(text)
        return self.tf_idf.tf_idf_fit_transform(count_matrix)

    #     tf_matrix = self.term_frequency(text)
    #     idf = self.idf_transform(tf_matrix)
    #     return self.tf_idf.fit_transform_idf(tf_matrix, idf)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(tfidf_matrix)
