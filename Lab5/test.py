#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Lab5.impl.MarkovChainBuilder import MarkovChainBuilder
from Lab5.impl.Ngramer import Ngramer


s = u'Ala ma kota i psa. Zenek ma kota imieniem Filemon. Zenek bardzo lubi psa Ali i też chciałby mieć takiego psa.'

ngrams = Ngramer().make_ngrams(['./files/pap_small.txt'], 2)
markov_chain = MarkovChainBuilder().create_chain(ngrams)

while True:
    number_of_sentences = raw_input("number of sentences\n")
    sentences = markov_chain.generate_sentence(int(number_of_sentences))
    print '\n'.join(sentences)