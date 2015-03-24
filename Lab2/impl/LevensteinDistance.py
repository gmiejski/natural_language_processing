import numpy


class LevensteinDistance():
    def __init__(self):
        pass

    def word_distance(self, word1, word2):
        matrix = self.create_matrix(word1, word2)
        return matrix[len(word2), len(word1)]

    def create_matrix(self, word1, word2):
        length1 = len(word1)
        length2 = len(word2)
        test = numpy.zeros((length2 + 1, length1 + 1))

        test[0] = range(0, length1 + 1)
        test[:, 0] = range(0, length2 + 1)
        for i in range(1, length2 + 1):
            for j in range(1, length1 + 1):
                cost = 0
                if word1[j - 1] != word2[i - 1]:
                    cost = 1
                test[i, j] = min(test[i - 1, j] + 1, test[i, j - 1] + 1, test[i - 1, j - 1] + cost)
        return test

