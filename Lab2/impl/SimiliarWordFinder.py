import codecs
import time

from impl.LevensteinDistance import LevensteinDistance


class SimiliarWordFinder():
    def __init__(self):
        self.mapping = self.create_mapping()
        self.levenstein = LevensteinDistance()

    def find_similiar_word_by_all(self, word):
        print 'Searching by all words:'
        self.print_time()
        lastTuple = (1000000, "")
        for k, v in self.mapping.iteritems():
            for candidate in v:
                if len(candidate) >= len(word) + lastTuple[0]:
                    pass
                else:
                    candidate_difference = self.levenstein.word_distance(word, candidate)
                    if candidate_difference == 0:
                        print "Word exists in language: " + str(word)
                        self.print_time()
                        return
                    elif candidate_difference < lastTuple[0]:
                        lastTuple = (candidate_difference, candidate)

        print "Did you mean : " + lastTuple[1] + " ?"
        self.print_time()
        pass


    def find_similiar_word(self, word):
        print 'Search by first letter'
        candidates = self.mapping[word[0]]
        lastTuple = (1000000, "")
        for candidate in candidates:
            if len(candidate) >= len(word) + lastTuple[0]:
                pass
            else:
                candidate_difference = self.levenstein.word_distance(word, candidate)
                if candidate_difference == 0:
                    print "Word exists in language: " + str(word)
                    self.print_time()
                    return
                elif candidate_difference < lastTuple[0]:
                    lastTuple = (candidate_difference, candidate)
        print "Did you mean : " + lastTuple[1] + " ?"
        self.print_time()
        pass

    def create_mapping(self):
        mapping = {}
        for word in codecs.open('./description/formy.txt', 'r', 'utf-8'):
            word = word.rstrip()
            print word
            if word[0] not in mapping:
                mapping[word[0]] = []
            mapping[word[0]].append(word)
        return mapping

    def print_time(self):
        print time.strftime("%H:%M:%S")

