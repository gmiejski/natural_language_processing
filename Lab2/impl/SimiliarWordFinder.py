import codecs

from impl.LevensteinDistance import LevensteinDistance


class SimiliarWordFinder():
    def __init__(self):
        self.mapping = self.create_mapping()
        self.levenstein = LevensteinDistance()

    def find_similiar_word(self, word):
        candidates = self.mapping[word[0]]
        lastTuple = (1000000, "")
        for candidate in candidates:
            if len(candidate) >= len(word) + lastTuple[0]:
                pass
            else:
                candidate_difference = self.levenstein.word_distance(word, candidate)
                if candidate_difference == 0:
                    print "Word exists in language: " + str(word)
                    return
                elif candidate_difference < lastTuple[0]:
                    lastTuple = (candidate_difference, candidate)
        print "Did you mean : " + lastTuple[1] + " ?"
        pass

    def create_mapping(self):
        mapping = {}
        for word in codecs.open('./description/formy_short.txt', 'r', 'utf-8'):
            word = word.rstrip()
            print word
            if word[0] not in mapping:
                mapping[word[0]] = []
            mapping[word[0]].append(word)
        return mapping

