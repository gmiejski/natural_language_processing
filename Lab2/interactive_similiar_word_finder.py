#!/usr/bin/env python
# -*- coding: utf-8 -*-

from impl.SimiliarWordFinder import SimiliarWordFinder

similiarWordFinder = SimiliarWordFinder()

while True:
    word = raw_input('Input a word for search:\n')
    print 'Looking for word: ' + word
    similiarWordFinder.find_similar_word_fast(unicode(word, 'utf-8'))



