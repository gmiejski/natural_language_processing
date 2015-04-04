#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Lab3.impl.pwodc import PWODC

pwdoc = PWODC()

pwdoc.pwodc(unicode("pupa", 'utf-8'), unicode("dupa", 'utf-8'))

while True:
    word = raw_input('Input a word :\n')
    word2 = raw_input('Input second word :\n')
    print 'Probablitity of error like this: ' + word + ", " + word2
    print pwdoc.pwodc(unicode(word, 'utf-8'), unicode(word2, 'utf-8'))
