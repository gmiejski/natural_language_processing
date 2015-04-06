#!/usr/bin/env python
# -*- coding: utf-8 -*-


class OrtographicErrorChecker:
    def __init__(self):
        self.ortographic_errors = {u"ch": "h", "rz": u"ż", "u": u"ó", }
        pass

    def convert_error(self, word):
        new_word = word
        for k, v in self.ortographic_errors.iteritems():
            new_word = new_word.replace(k, v)
        return new_word
