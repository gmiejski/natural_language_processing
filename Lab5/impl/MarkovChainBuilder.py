import collections

from Lab5.impl.MarkovChain import MarkovChain


class MarkovChainBuilder():
    def __init__(self):
        pass

    def create_chain(self, ngrams):
        markov = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        ngrams_by_endings = collections.defaultdict(lambda: set())
        for ngram in ngrams:
            print(ngram)
            first_word, second_word = ngram.split()
            ngrams_by_endings[second_word].add(ngram)
            for w in ngrams_by_endings[first_word]:
                markov[w][ngram] += 1
        return MarkovChain(markov, ngrams_by_endings)
