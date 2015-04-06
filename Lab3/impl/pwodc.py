#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import collections
from operator import attrgetter
import math

from Lab2.impl.LevensteinDistance import LevensteinDistance
from Lab3.impl.utils.echo_decorator import echo


class PWODC():
    def __init__(self):
        self.levenstein = LevensteinDistance()
        self.probability_statistics = self.receive_errors_statistics()

    def pwodc(self, w, c, real_distance=None):
        if real_distance is None:
            real_distance = self.levenstein.word_distance(w, c)
        # print 'real distance = ' + str(real_distance)
        # self.levenstein.print_matrix(w, c)
        if real_distance in self.probability_statistics.keys():
            probability_by_dist = DistanceProbability(real_distance, self.probability_statistics[real_distance])
        else:
            probability_by_dist = DistanceProbability.NONE()
            for distance, probability in self.probability_statistics.iteritems():
                if math.fabs(real_distance - probability_by_dist.get_distance()) > math.fabs(real_distance - distance):
                    probability_by_dist = DistanceProbability(distance, probability)
        return probability_by_dist

    @echo
    def receive_errors_statistics(self):
        error_statistics = collections.defaultdict(lambda: 0)
        total_errors = 0
        for line in codecs.open("../files/bledy.txt", 'r', 'utf-8'):
            word1, word2 = line.split(";")
            distance = self.levenstein.word_distance(word1, word2)
            error_statistics[distance] += 1
            total_errors += 1

        probability_errors = dict()
        for distance, count in error_statistics.iteritems():
            probability_errors[distance] = float(count) / total_errors
        return probability_errors


class DistanceProbability:
    def __init__(self, distance, probability):
        self.distance = distance
        self.probability = probability

    def better(self, another_one):
        return max([self, another_one], key=attrgetter('probability'))

    @staticmethod
    def NONE():
        return DistanceProbability(100000, 0)

    def get_distance(self):
        return self.distance

    def __str__(self):
        return "DistanceProbability : distance = {0}, probability = {1}".format(self.distance, self.probability)