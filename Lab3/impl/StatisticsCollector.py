#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import collections
import os
import re


class StatisticsCollector:
    def __init__(self, files_names=[]):
        print os.getcwd()
        print os.path.dirname(os.path.abspath(__file__))
        self.default_files = ["popul.iso.utf8", 'dramat.iso.utf8', 'proza.iso.utf8', 'publ.iso.utf8', 'wp.iso.utf8']
        if len(files_names) == 0:
            files_parsed = self.default_files
        else:
            files_parsed = files_names

        self.statistics, self.words_count = self.gather_statistics(files_parsed)
        self.proper_forms_count = self.get_all_forms_count()

    def probability_of_word(self, word):
        occurences_number = self.statistics[word]
        print 'Occurances = ' + str(occurences_number)
        return (float(occurences_number))/(self.words_count + self.proper_forms_count)

    def collect_statistics(self):
        pass

    def gather_statistics(self, all_files_names):
        statistics = collections.defaultdict(lambda: 1)
        words_count = 0
        for filename in all_files_names:
            for line in codecs.open("./../files/" + filename, 'r', 'utf-8'):
                for word in line.lower().split():
                    if not self.contains_digit(word) and not self.having_special_characters(word):
                        words_count += 1
                        statistics[word] += 1
        return statistics, words_count

    def contains_digit(self, word):
        _digits = re.compile('\d')
        return bool(_digits.search(word))


    def having_special_characters(self, word):
        special_chars = re.compile('[~!?@#$%^&*()_+{}":;\'-,.\-`]+')
        return bool(special_chars.search(word))

    def get_all_forms_count(self):
        lines_count = 0
        for line in codecs.open("./../files/formy.txt", 'r', 'utf-8'):
            lines_count += 1
        return lines_count