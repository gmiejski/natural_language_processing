#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from Lab2.impl.OrtographicErrorChecker import OrtographicErrorChecker


class OrtographicConverterTest(unittest.TestCase):
    def setUp(self):
        self.ortographic = OrtographicErrorChecker()

    def test_ortographic1(self):
        new_word = self.ortographic.convert_error(unicode("burza", 'utf-8'))
        self.assertEqual(new_word, unicode("bóża", 'utf-8'))
        new_word = self.ortographic.convert_error(u"buża")
        self.assertEqual(new_word, u"bóża")
        new_word = self.ortographic.convert_error(u"bóża")
        self.assertEqual(new_word, u"bóża")


if __name__ == '__main__':
    unittest.main()