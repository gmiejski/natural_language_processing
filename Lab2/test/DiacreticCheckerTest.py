#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
from impl.DiacreticChecker import DiacreticChecker


class DiacreticCheckerTest(unittest.TestCase):
    def setUp(self):
        self.diacretic = DiacreticChecker()

    def test_diacretic(self):
        self.assertTrue(self.diacretic.is_diacretic_error(u"a", u"ą"), True)
        self.assertTrue(self.diacretic.is_diacretic_error(u"ą", u"a"), True)
        self.assertTrue(self.diacretic.is_diacretic_error(u"c", u"ć"), True)
        self.assertTrue(self.diacretic.is_diacretic_error(u"z", u"ż"), True)
        self.assertTrue(self.diacretic.is_diacretic_error(u"z", u"ź"), True)
        self.assertTrue(self.diacretic.is_diacretic_error(u"ż", u"z"), True)
        self.assertTrue(self.diacretic.is_diacretic_error(u"ź", u"z"), True)

    def test_not_diacretic(self):
        self.assertFalse(self.diacretic.is_diacretic_error("a", "a"), True)
        self.assertFalse(self.diacretic.is_diacretic_error("d", "c"), True)
        self.assertFalse(self.diacretic.is_diacretic_error("d", "c"), True)


if __name__ == '__main__':
    unittest.main()