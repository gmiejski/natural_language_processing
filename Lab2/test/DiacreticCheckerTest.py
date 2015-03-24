#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from impl.DiacreticChecker import DiacreticChecker


class DiacreticCheckerTest(unittest.TestCase):
    def setUp(self):
        self.diacretic = DiacreticChecker()

    def test_diacretic(self):
        self.assertTrue(self.diacretic.is_diacretic_error("a", "ą"), True)
        self.assertTrue(self.diacretic.is_diacretic_error("ą", "a"), True)
        self.assertTrue(self.diacretic.is_diacretic_error("c", "ć"), True)
        self.assertTrue(self.diacretic.is_diacretic_error("z", "ż"), True)
        self.assertTrue(self.diacretic.is_diacretic_error("z", "ź"), True)
        self.assertTrue(self.diacretic.is_diacretic_error("ż", "z"), True)
        self.assertTrue(self.diacretic.is_diacretic_error("ź", "z"), True)

    def test_not_diacretic(self):
        self.assertFalse(self.diacretic.is_diacretic_error("a", "a"), True)
        self.assertFalse(self.diacretic.is_diacretic_error("d", "c"), True)
        self.assertFalse(self.diacretic.is_diacretic_error("d", "c"), True)


if __name__ == '__main__':
    unittest.main()