#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DiacreticChecker:
    def __init__(self):
        self.mapping = {"a": [u"ą", "a"], u"ą": ["a", u"ą"],
                        "c": [u"ć", "c"], u"ć": ["c", u"ć"],
                        "e": [u"ę", "e"], u"ę": ["e", u"ę"],
                        "l": [u"ł", "l"], u"ł": ["l", u"ł"],
                        "n": [u"ń", "n"], u"ń": ["n", u"ń"],
                        "o": [u"ó", "o"], u"ó": ["o", u"ó"],
                        "s": [u"ś", "s"], u"ś": ["s", u"ś"],
                        "z": [u"ż", u"ź", "z"], u"ź": [u"ż", u"ź", "z"], u"ż": [u"ż", u"ź", "z"]}

    def is_diacretic_error(self, l1, l2):
        return l1 in self.mapping and l2 in self.mapping.get(l1)
