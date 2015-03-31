#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SimiliarLetter():
    def __init__(self):
        self.mapping = {"a": [u"ą"], u"ą": ["a"], "c": [u"ć"], u"ć": ["c"],
                        "e": [u"ę"], u"ę": ["e"], "l": [u"ł"], u"ł": ["l"], "n": [u"ń"], u"ń": ["n"], "o": [u"ó"],
                        u"ó": ["o"], "s": [u"ś", "s"], u"ś": ["s", u"ś"], "z": ["z", u"ż", u"ź"],
                        u"ź": ["z", u"ż", u"ź"],
                        u"ż": ["z", u"ż", u"ź"]}

    def get_starting_letters(self, first_letter):
        if first_letter in self.mapping:
            result = list(self.mapping.get(first_letter))
            result.append(first_letter)
            return result
        else:
            return [first_letter]
