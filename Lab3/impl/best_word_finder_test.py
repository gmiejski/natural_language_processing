#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Lab3.impl.BestWordFinder import BestWordFinder

best_word_finder = BestWordFinder()

while True:
    word = raw_input('Input a word :\n')
    print best_word_finder.find_best_word(unicode(word, 'utf-8'))
