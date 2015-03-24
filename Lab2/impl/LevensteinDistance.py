import numpy

from impl.DiacreticChecker import DiacreticChecker


class LevensteinDistance():
    def __init__(self, czech=True):
        self.diacretic_checker = DiacreticChecker()
        self.czech_errors = czech

    def word_distance(self, word1, word2):
        matrix = self.create_matrix(word1, word2)
        return matrix[len(word2), len(word1)]

    def create_matrix(self, word1, word2):
        length1 = len(word1)
        length2 = len(word2)
        diff_matrix = numpy.zeros((length2 + 1, length1 + 1))

        diff_matrix[0] = range(0, length1 + 1)
        diff_matrix[:, 0] = range(0, length2 + 1)
        for i in range(1, length2 + 1):
            for j in range(1, length1 + 1):
                cost = 0
                if self.are_orthographic_errors(word1[j - 1], word2[i - 1]):
                    cost = 0.5
                elif word1[j - 1] != word2[i - 1]:
                    cost = 1
                diff_matrix[i, j] = min(diff_matrix[i - 1, j] + 1,
                                        diff_matrix[i, j - 1] + 1,
                                        diff_matrix[i - 1, j - 1] + cost)

                if self.czech_errors and i > 1 and j > 1 and (word1[j - 1] == word2[i - 2]) and \
                        (word1[j - 2] == word2[i - 1]):
                    diff_matrix[i, j] = min(diff_matrix[i, j], diff_matrix[i - 2, j - 2] + cost)
        return diff_matrix

    def are_orthographic_errors(self, l1, l2):
        return self.diacretic_checker.is_diacretic_error(l1, l2)


