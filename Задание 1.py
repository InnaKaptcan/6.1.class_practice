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

    def fit_transform(self, text):
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


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(vectorizer.fit_transform(corpus))
