#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Lab3.impl.StatisticsCollector import StatisticsCollector

statistical_collector = StatisticsCollector()

print statistical_collector.probability_of_word(unicode("pupa", 'utf-8'))

while True:
    word = raw_input('Input a word :\n')
    print statistical_collector.probability_of_word(unicode(word, 'utf-8'))
