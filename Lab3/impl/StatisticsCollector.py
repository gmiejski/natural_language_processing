#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import collections
import os
import re

from Lab3.impl.utils.echo_decorator import echo


class StatisticsCollector:
    def __init__(self, files_names=[]):
        self.default_files = ["popul.iso.utf8", 'dramat.iso.utf8', 'proza.iso.utf8', 'publ.iso.utf8', 'wp.iso.utf8']
        self.statistics_file_name = './../files/words_statistics.txt'
        if len(files_names) == 0:
            files_parsed = self.default_files
        else:
            files_parsed = files_names
        self.statistics, self.words_count = self.gather_statistics(files_parsed)
        self.proper_forms_count = self.get_all_forms_count()


    def probability_of_word(self, word):
        occurences_number = self.statistics[word]
        return (float(occurences_number)) / (self.words_count + self.proper_forms_count)

    @echo
    def gather_statistics(self, all_files_names):
        if os.path.isfile(self.statistics_file_name):
            return self.read_statistics_from_file()

        statistics = collections.defaultdict(lambda: 1)
        words_count = 0
        for filename in all_files_names:
            for line in codecs.open("./../files/" + filename, 'r', 'utf-8'):
                for word in line.lower().split():
                    if not self.contains_digit(word) and not self.having_special_characters(word):
                        words_count += 1
                        statistics[word] += 1

        self.save_statistics(statistics)
        return statistics, words_count

    @echo
    def read_statistics_from_file(self):
        statistics = collections.defaultdict(lambda: 1)
        words_count = 0
        for line in codecs.open(self.statistics_file_name, 'r', 'utf-8'):
            word, occurrences = line.split(',')
            statistics[word] = occurrences.replace('\n', '')
            words_count += float(occurrences.replace('\n', ''))
        return statistics, words_count

    def contains_digit(self, word):
        _digits = re.compile('\d')
        return bool(_digits.search(word))


    def having_special_characters(self, word):
        special_chars = re.compile('[~!?@#$%^&*()_+{}":;\'-,.\-`]+')
        return bool(special_chars.search(word))

    @echo
    def get_all_forms_count(self):
        if os.path.isfile("./../files/all_forms_count.txt"):
            for line in codecs.open("./../files/all_forms_count.txt", 'r', 'utf-8'):
                return int(line)
        else:
            lines_count = 0
            for line in codecs.open("./../files/formy.txt", 'r', 'utf-8'):
                lines_count += 1
            self.save_all_forms_count(lines_count)
            return lines_count

    @echo
    def save_statistics(self, statistics):
        with codecs.open(self.statistics_file_name, 'wb', "utf-8") as target_file:
            for key, value in statistics.iteritems():
                target_file.write(key + "," + str(value) + "\n")
        pass

    @echo
    def save_all_forms_count(self, lines_count):
        with codecs.open("./../files/all_forms_count.txt", 'wb', 'utf-8') as target_file:
            target_file.write(str(lines_count))
        pass
