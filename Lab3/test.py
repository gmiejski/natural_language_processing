#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import collections
import re
import os
from Lab3.impl.StatisticsCollector import StatisticsCollector


print os.getcwd()
print os.path.dirname(os.path.abspath(__file__))

statistic_collector = StatisticsCollector()

statistic_collector.collect_statistics()

all_files_names = ["popul.iso.utf8", 'dramat.iso.utf8', 'proza.iso.utf8', 'publ.iso.utf8', 'wp.iso.utf8']

statistics = collections.defaultdict(lambda: 0)


def contains_digit(word):
    _digits = re.compile('\d')
    return bool(_digits.search(word))


def having_special_characters(word):
    special_chars = re.compile('[~!?@#$%^&*()_+{}":;\'-,.\-`]+')
    return bool(special_chars.search(word))


for filename in all_files_names:
    for line in codecs.open("./files/" + filename, 'r', 'utf-8'):
        for word in line.lower().split():
            if not contains_digit(word) and not having_special_characters(word):
                statistics[word] += 1

var = 1
for key, val in statistics.iteritems():
    print key + " " + str(val)



