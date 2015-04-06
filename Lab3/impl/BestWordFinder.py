#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import collections
import os

from Lab2.impl.LevensteinDistance import LevensteinDistance
from Lab3.impl.BestResultList import BestResultList

from Lab3.impl.StatisticsCollector import StatisticsCollector
from Lab3.impl.pwodc import PWODC
from Lab3.impl.utils.echo_decorator import echo


class BestWordFinder():
    def __init__(self):
        self.forms_by_length_filename = "./../files/foms_by_length.iso.utf8"
        self.pwodc = PWODC()
        self.statistics = StatisticsCollector()
        self.forms_by_length = self.gather_forms_by_length()
        self.levenstein = LevensteinDistance()

    def find_best_word(self, word_to_fix):
        print 'Finding best fix for word: ' + word_to_fix
        best_result_list = BestResultList()
        # best_so_far = (0, '')
        for length, words in self.forms_by_length.iteritems():
            if abs(length - len(word_to_fix)) < 2:
                for fixing_word in words:
                    real_distance = self.levenstein.word_distance(word_to_fix, fixing_word)
                    if real_distance < 5:
                        pwodc = self.pwodc.pwodc(word_to_fix, fixing_word)
                        prob_of_fix = self.statistics.probability_of_word(fixing_word)
                        new_prob = pwodc.probability * prob_of_fix
                        best_result_list.append(new_prob, fixing_word)
                        # if new_prob > best_so_far[0]:
                        # best_so_far = (new_prob, fixing_word)
        return best_result_list.get_results()

    @echo
    def gather_forms_by_length(self):
        if os.path.isfile(self.forms_by_length_filename):
            forms_by_length = self.read_forms_by_length_from_file()
        else:
            forms_by_length = collections.defaultdict(lambda: [])
            for word in codecs.open("./../files/formy.txt", 'rb', 'utf-8'):
                word = word.replace('\n', '')
                forms_by_length[len(word)].append(word)
            self.save_forms_by_length(forms_by_length)
        return forms_by_length

    @echo
    def read_forms_by_length_from_file(self):
        forms_by_length = dict()
        for word in codecs.open(self.forms_by_length_filename, 'rb', 'utf-8'):
            count, all_words = word.split(":")
            forms_by_length[int(count)] = all_words.replace('\n', '').split(",")
        return forms_by_length

    @echo
    def save_forms_by_length(self, forms_by_length):
        with codecs.open(self.forms_by_length_filename, 'wb', 'utf-8') as target_file:
            for length, words in forms_by_length.iteritems():
                target_file.write(str(length) + ":" + ','.join(words) + "\n")


