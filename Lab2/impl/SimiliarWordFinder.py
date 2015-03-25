import codecs
import time

from impl.LevensteinDistance import LevensteinDistance
from impl.SimiliarLetters import SimiliarLetter


class SimiliarWordFinder():
    def __init__(self):
        self.mapping = self.create_mapping()
        self.levenstein = LevensteinDistance()
        self.similiar_letter = SimiliarLetter()

    def find_similiar_word_by_all(self, word):
        print 'Searching by all words:'
        self.print_time()
        best_tuple = (1000000, "")
        counter = 1
        for k, v in self.mapping.iteritems():
            print counter
            print 'Letter = ' + v[0][0]
            counter += 1
            last_tuple = self.find_best_tuple(word, v, best_tuple)
            if last_tuple[0] == 0:
                print "Word exists in language: " + str(word)
                self.print_time()
                return
            elif last_tuple[0] < best_tuple[0]:
                best_tuple = last_tuple
        print 'Distance: ' + str(best_tuple[0])
        print "Did you mean : " + best_tuple[1] + " ?"
        self.print_time()
        pass

    def find_similar_word_fast(self, word):
        print 'Search by first letter'
        self.print_time()
        starting_letter = word[0]
        starting_letters = self.similiar_letter.get_starting_letters(starting_letter)
        counter = 1
        best_tuple = (1000000, "")
        for possible_starting_letter in starting_letters:
            print counter
            print 'Letter = ' + possible_starting_letter
            counter += 1
            candidates = self.get_candidates_from_mapping(possible_starting_letter)
            last_tuple = self.find_best_tuple(word, candidates, best_tuple)
            if last_tuple[0] == 0:
                print "Word exists in language: " + word
                self.print_time()
                return
            elif last_tuple[0] < best_tuple[0]:
                best_tuple = last_tuple
        print 'Distance: ' + str(best_tuple[0])
        print "Did you mean : " + best_tuple[1] + " ?"
        self.print_time()
        pass

    def print_time(self):
        print time.strftime("%H:%M:%S")

    def find_best_tuple(self, word, candidates, previous_tuple):
        last_tuple = (previous_tuple[0], previous_tuple[1])
        for candidate in candidates:
            if len(candidate) >= len(word) + last_tuple[0]:
                pass
            else:
                candidate_distance = self.levenstein.word_distance(word, candidate, last_tuple[0])
                if candidate_distance == 0:
                    return candidate_distance, candidate
                elif candidate_distance < last_tuple[0]:
                    last_tuple = (candidate_distance, candidate)
        return last_tuple

    def create_mapping(self):
        mapping = {}
        print 'STARTING READING WORDS'
        for word in codecs.open('./description/formy.txt', 'r', 'utf-8'):
            word = word.rstrip()
            if word[0] not in mapping:
                mapping[word[0]] = []
            mapping[word[0]].append(word)
        print 'DONE READING WORDS'
        return mapping

    def get_candidates_from_mapping(self, possible_starting_letter):
        if possible_starting_letter in self.mapping:
            return self.mapping[possible_starting_letter]
        else:
            return []
