#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

from Lab2.impl.LevensteinDistance import LevensteinDistance

from Lab3.impl.BestWordFinder import BestWordFinder


best_word_finder = BestWordFinder()
levenstein = LevensteinDistance()

good = 0
bad = 0
print 'Fix for | proper fix | fixes found'
for line in codecs.open('./../files/bledy.txt', 'rb', 'utf-8'):
    w1, w2 = line.split(";")
    found_fixes = best_word_finder.find_best_word(w1.replace("\n", ''))
    word_fixes = map(lambda x: x[1], found_fixes)
    print w1.replace("\n", '').replace("\r", '') + " -> " + w2.replace("\n", '').replace("\r", '') + " -> " + ', '.join(
        word_fixes)
    if w2.replace("\n", '') in word_fixes:
        good += 1
    else:
        bad += 1

print "Total god matches: " + str(good / (good + bad))
print "Total bad matches: " + str(bad / (good + bad))


