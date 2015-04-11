#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Lab2.impl.LevensteinDistance import LevensteinDistance

from Lab3.impl.BestWordFinder import BestWordFinder


best_word_finder = BestWordFinder()
levenstein = LevensteinDistance()

good = 0
bad = 0
print 'Fix for | proper fix | fixes found'
while True:
    word = raw_input('A word to fix:\n')
    found_fixes = best_word_finder.find_best_word(unicode(word, 'utf-8'))
    word_fixes = map(lambda x: x[1], found_fixes)
    print ', '.join(word_fixes)



