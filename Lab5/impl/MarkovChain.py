import itertools

from numpy import random


class MarkovChain():
    def possible_starting_words(self, markov_path, ngrams_by_start):
        starting_ngrams = filter(lambda x: '#' in x[0], markov_path.keys())
        possible_sentence_starting_words = map(lambda x: x.split(' ')[1], starting_ngrams)
        return list(set(itertools.chain(*map(lambda x: ngrams_by_start[x], possible_sentence_starting_words))))

    def __init__(self, markov_path, ngrams_by_start):
        self.markov_path = markov_path
        self.possible_starting_words = self.possible_starting_words(markov_path, ngrams_by_start)
        pass

    def generate_sentence(self, count):
        sentences = []
        for i in range(0, count):
            last_ngram = self.get_random_start()
            sentence = last_ngram
            while '#' not in last_ngram or ('#' in last_ngram and len(sentence.split()) < 5):
                next_ngram = self.next_sentence_part(last_ngram)
                last_ngram = next_ngram
                sentence = sentence + ' ' + next_ngram.split()[1]
            sentences.append(sentence)
        return sentences

    def get_random_start(self):
        return self.possible_starting_words[random.randint(0, len(self.possible_starting_words))]

    def next_sentence_part(self, last_ngram):
        return self.markov_path[last_ngram][random.randint(0, len(self.markov_path[last_ngram]))]
