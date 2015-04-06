#!/usr/bin/env python
# -*- coding: utf-8 -*-

from impl.LevensteinDistance import LevensteinDistance

string1 = "kura"
string2 = "kurka"

levenstein_distance = LevensteinDistance()
print levenstein_distance.create_matrix(string2, string1)
print levenstein_distance.create_matrix(u"stęchły", u"stechły")
print levenstein_distance.create_matrix(u"rywik", u"wyśik")
print levenstein_distance.create_matrix(u"rysik", u"ryśik")

while True:
    word = raw_input('First word:\n')
    word2 = raw_input('Second word:\n')
    print levenstein_distance.create_matrix(unicode(word, 'utf-8'), unicode(word2, 'utf-8'))




