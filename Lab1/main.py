#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from pyspark import SparkContext, SparkConf


def ngramFunc(word, n):
    return [word[i:i + n] for i in range(0, len(word))]


def containsDigit(ngram):
    _digits = re.compile('\d')
    return bool(_digits.search(ngram))


def havingSpecialCharacters(ngram):
    specialChars = re.compile('[~!@#$%^&*()_+{}":;\'-,.]+')
    return bool(specialChars.search(ngram))


def havingLengthOf(word, length):
    return len(word) == length

# tokenizer = RegexpTokenizer(u"[a-zA-ZąĄćĆęĘłŁńŃóÓśŚźŹżŻ]+")
# tokenizer = RegexpTokenizer(u'[^0-9!@#$%^&*()\]\[]+')
appName = u"n-gram"
conf = SparkConf().setAppName(appName)
sc = SparkContext(conf=conf)

n = 3

lines = sc.textFile(u"./texts/polski.txt")

words = lines.map(lambda s: s.lower().split()).flatMap(lambda words: words)
words = words.filter(lambda x: not containsDigit(x))
words = words.filter(lambda x: not havingSpecialCharacters(x))
words = words.filter(lambda x: not havingLengthOf(x, n))
ngram = words.map(lambda x: ngramFunc(x, n)).flatMap(lambda words: words)

# result = ngram.reduceByKey(lambda c1, c2: c1 + c2).collect()
result = ngram.map(lambda x: (x, 1)).countByKey()

# totalLength = words.reduce(lambda a, b: a + b)
# print totalLength.encode('unicode_escape')

print 1

