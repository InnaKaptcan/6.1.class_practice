def tf_transform(count_matrix: list) -> list:
    total_nmb_of_words = sum(count_matrix[0])
    answ = []
    for i in count_matrix:
        answ.append(list(map(lambda x: round(x/total_nmb_of_words, 3), i)))
    return answ


if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    tf_matrix = tf_transform(count_matrix)
    print(tf_matrix)