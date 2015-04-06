#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from Lab2.impl.LevensteinDistance import LevensteinDistance


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

    def test_diacretic_errors(self):
        self.assertEqual(self.levenstein.word_distance(u"ćma", u"cmą"), 1)

    def test_czech_errors(self):
        self.assertEqual(self.levenstein.word_distance("rzeka", "zreka"), 1.5)
        self.assertEqual(self.levenstein.word_distance("reka", u"ręak"), 1.5)

    def test_should_ignore_ortographic_errors(self):
        self.assertEqual(self.levenstein.word_distance("rzeka", u"żeka"), 0)

if __name__ == '__main__':
    unittest.main()