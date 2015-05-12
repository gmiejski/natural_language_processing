import codecs
import collections
import re
import math


class TfIdf():
    def __init__(self):
        self.basic_form_of_words = self.basic_form_of_words()
        self.words_in_each_note = self.words_frequency_in_each_note()
        self.N = len(self.words_in_each_note.keys())
        pass


    def basic_form_of_words(self):
        basic_forms_of_words = {}
        for line in codecs.open('./files/odm.txt', 'r', 'utf-8'):
            words = map(lambda x: x.strip().lower(), line.split(','))
            basic_word_form = words[0]
            for word in words:
                basic_forms_of_words[word] = basic_word_form
        return basic_forms_of_words


    def words_frequency_in_each_note(self):
        words_frequency_by_note = {}
        for line in codecs.open('./files/pap_short.txt', 'r', 'utf-8'):
            words_from_pap = map(lambda x: x.strip().lower(), line.split())
            if words_from_pap[0].startswith("#"):
                words_frequency = collections.defaultdict(lambda: 0)
                note_id = words_from_pap[0]
                words_frequency_by_note[note_id] = words_frequency
                current_note_dict = words_frequency
            else:
                for word in words_from_pap:
                    bare_word = re.sub('[~!?@#$%^&*()_+{}":;\'-,.\-`]+', '', word)
                    if bare_word in self.basic_form_of_words:
                        basic_word_form = self.basic_form_of_words[bare_word]
                        current_note_dict[basic_word_form] += 1
        return words_frequency_by_note


    def df(self, basic_term):
        documents_containing_term = 0
        for key, value in self.words_in_each_note.iteritems():
            if basic_term in value.keys():
                documents_containing_term += 1
        return documents_containing_term


    def tf_idf(self, term, document):
        basic_term = self.basic_form_of_words[term]
        weight = self.words_in_each_note[document][basic_term] * math.log(self.N / self.df(basic_term))
        return weight

    def idf_matrix(self):
        return self.words_in_each_note


