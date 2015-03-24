import unittest

from impl.LevensteinDistance import LevensteinDistance


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.levenstein = LevensteinDistance()

    def test_same_words(self):
        word = "kura"
        self.assertEqual(self.levenstein.word_distance(word, word), 0)

    def test_single_letter_diff(self):
        self.assertEqual(self.levenstein.word_distance("kura", "kurka"), 1)
        self.assertEqual(self.levenstein.word_distance("kurka", "kura"), 1)
        self.assertEqual(self.levenstein.word_distance("kurka", "kurma"), 1)

    def test_not_similiar_words(self):
        self.assertEqual(self.levenstein.word_distance("auto", "automobil"), 5)
        self.assertEqual(self.levenstein.word_distance("kieszeniowka", "kreskowka"), 5)


if __name__ == '__main__':
    unittest.main()