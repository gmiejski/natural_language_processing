#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

from pyspark import SparkContext, SparkConf


class NgramSummaryReader:
    def __init__(self, strict=True, text_files_path="./texts/"):
        self.file_extension = ".txt"
        self.text_files_path = text_files_path
        self.results_files_path = "./ngram_results/"
        self.strict = strict

    def ngram_func(self, word, n):
        return [word[i:i + n] for i in range(0, len(word))]

    def contains_digit(self, ngram):
        _digits = re.compile('\d')
        return bool(_digits.search(ngram))

    def having_special_characters(self, ngram):
        special_chars = re.compile('[~!?@#$%^&*()_+{}":;\'-,.\-`]+')
        return bool(special_chars.search(ngram))

    def having_length_of(self, word, length):
        return len(word) == length

    def file_words_rdd(self, spark_context, filename):
        lines = spark_context.textFile(self.text_files_path + filename + self.file_extension, use_unicode=False)
        file_words = lines.map(lambda s: s.lower().split()).flatMap(lambda words: words)
        file_words = file_words.filter(lambda x: not self.contains_digit(x))
        file_words = file_words.filter(lambda x: not self.having_special_characters(x))

        file_words = file_words.map(lambda x: x.decode('utf-8'))
        file_words = file_words.map(lambda x: x.replace(u'\ufffd', ''))
        return file_words

    def make_ngram(self, files, n):
        conf = SparkConf().setAppName("n-gram")
        spark_context = SparkContext(conf=conf)
        lines = spark_context.parallelize([])
        for filename in files:
            lines = lines.union(self.file_words_rdd(spark_context, filename))
        ngram = lines.map(lambda x: self.ngram_func(x, n)).flatMap(lambda words: words)
        if self.strict:
            ngram = ngram.filter(lambda x: self.having_length_of(x, n))
        result = ngram.map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b).collect()
        spark_context.stop()
        return result

    def make_ngram_and_save(self, language, files, n):

        ngram = self.make_ngram(files, n)
        d = dict(ngram)
        with codecs.open(self.results_files_path + language + '.csv', 'wb', "utf-8") as target_file:
            ngram_max = max(d.values())
            ngram_min = min(d.values())
            for ngram_tuple in ngram:
                ngram_val = float(float(ngram_tuple[1] - ngram_min) / float(ngram_max - ngram_min))
                target_file.write(ngram_tuple[0] + "," + str(ngram_val) + "\n")
        pass