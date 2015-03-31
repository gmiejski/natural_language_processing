#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DiacreticChecker:
    def __init__(self):
        self.mapping = {"a": [u"ą"], u"ą": ["a"],
                        "c": [u"ć"], u"ć": ["c"],
                        "e": [u"ę"], u"ę": ["e"],
                        "l": [u"ł"], u"ł": ["l"],
                        "n": [u"ń"], u"ń": ["n"],
                        "o": [u"ó"], u"ó": ["o"],
                        "s": [u"ś"], u"ś": ["s"],
                        "z": [u"ż", u"ź"], u"ź": [u"ż", "z"], u"ż": [u"ź", "z"]}

    def is_diacretic_error(self, l1, l2):
        return l1 in self.mapping and l2 in self.mapping.get(l1)
