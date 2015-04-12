#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs

import nltk
import nltk.data


class Ngramer:
    def __init__(self):
        self.file_extension = ".txt"
        self.results_files_path = "./results/"

    def ngram_func(self, word, n):
        return [word[i:i + n] for i in range(0, len(word))]

    def contains_digit(self, ngram):
        _digits = re.compile('\d')
        return bool(_digits.search(ngram))

    def having_special_characters(self, ngram):
        special_chars = re.compile('[~!?@#$%^&*()_+{}":;\'-,\-`]+')
        return bool(special_chars.search(ngram))

    def having_length_of(self, word, length):
        return len(word) == length

    def all_words(self, filepath):
        all_words = []
        with codecs.open(filepath, 'rb', 'utf-8') as file:
            text = file.read()
            sentences = nltk.sent_tokenize(text, language='polish')
            for sentence in sentences:
                words_in_line = sentence.lower().split()
                # words_in_line = map(lambda x: re.sub('[~!?@#$%^&*()_+{}":;\'-,\-`]+', "", x), words_in_line)
                words_in_line = map(lambda x: x.replace('\n', '').replace('\r', ''), words_in_line)
                words_in_line = filter(lambda x: '#' not in x, words_in_line)
                # words_in_line = filter(lambda x: not self.having_special_characters(x), words_in_line)
                all_words.append(words_in_line)
        return all_words

    def make_ngrams(self, files, n):
        all_sentences = []
        for filename in files:
            words = self.all_words(filename)
            all_sentences += words

        all_ngrams = []
        all_sentences = filter(lambda x: len(x) > 0, all_sentences)
        for sentence in all_sentences:
            sentence = filter(lambda x: len(x) > 0, sentence)
            ngrams = self.join_words(sentence, n)
            all_ngrams += ngrams

        return all_ngrams

    def join_words(self, sentence, n):
        # return [' '.join(sentence[i:i + n]) for i in range(0, len(sentence) - 2)] + [sentence[-1] + ' .']
        w = ['. ' + sentence[0]] + [' '.join(sentence[i:i + n]) for i in range(0, len(sentence) - 2)]
        if len(sentence) > 2:
            w += [sentence[-2] + ' ' + sentence[-1][:-1]]
        w += [sentence[-1][:-1] + ' ' + sentence[-1][-1]]
        return w


