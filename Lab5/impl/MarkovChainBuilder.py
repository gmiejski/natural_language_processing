import collections

from Lab5.impl.MarkovChain import MarkovChain


class MarkovChainBuilder():
    def __init__(self):
        pass

    def create_chain(self, ngrams):
        markov = collections.defaultdict(lambda: [])
        ngrams_by_endings = collections.defaultdict(lambda: set())
        ngrams_by_start = collections.defaultdict(lambda: set())

        for ngram in ngrams:
            k = ngram.split()
            if len(k) == 2:
                first_word, second_word = ngram.split()
            else:
                first_word = k[0]
                second_word = '#'
                ngram = first_word + ' ' + second_word
            ngrams_by_endings[second_word].add(ngram)
            ngrams_by_start[first_word].add(ngram)
            for w in ngrams_by_endings[first_word]:
                markov[w].append(ngram)
        return MarkovChain(markov, ngrams_by_start)
