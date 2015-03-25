#!/usr/bin/env python
# -*- coding: utf-8 -*-

from impl.LevensteinDistance import LevensteinDistance
from impl.SimiliarWordFinder import SimiliarWordFinder

string1 = "kura"
string2 = "kurka"

levenstein_distance = LevensteinDistance()
print levenstein_distance.create_matrix(string2, string1)
print levenstein_distance.create_matrix(u"stęchły", u"stechły")

similiarWordFinder = SimiliarWordFinder()

while True:
    word = raw_input('Input a word for search:\n')
    'Looking for word: ' + word
    similiarWordFinder.find_similar_word_fast(unicode(word))



