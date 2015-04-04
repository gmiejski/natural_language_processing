#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import collections

alphabet = 'abcdefghijklmnopqrstuvwxyząćęłńóśżź'


def words(filename):
    all_words = []
    for line in codecs.open("./files/" + filename, 'r', 'utf-8'):
        for word in line.lower().split():
            all_words.append(word)
    return all_words


def train(all_words):
    model = collections.defaultdict(lambda: 1)
    for single_word in all_words:
        model[single_word] += 1
    return model


def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


NWORDS = train(words("formy.txt"))


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)


def known(words): return set(w for w in words if w in NWORDS)


def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

while True:
    word = input('What is your name?')
    print(correct(word))