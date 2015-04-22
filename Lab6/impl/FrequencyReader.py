import codecs
import collections
import os
import re
import operator


class FrequencyReader():
    def __init__(self):
        self.frequency_txt = './files/frequency.txt'
        pass

    def read_frequencies_from_file(self):
        frequencies_read_from_file = []
        for frequency_line in codecs.open(self.frequency_txt, 'r', 'utf-8'):
            word, frequency = frequency_line.split(',')
            frequencies_read_from_file.append((word, int(frequency.replace('\n', ''))))
        return frequencies_read_from_file

    def read_frequency(self):
        if os.path.isfile(self.frequency_txt):
            return self.read_frequencies_from_file()
        else:
            basic_forms_of_words = {}
            for line in codecs.open('./files/odm.txt', 'r', 'utf-8'):
                words = map(lambda x: x.strip(), line.split(','))
                basic_word_form = words[0]
                for word in words:
                    basic_forms_of_words[word] = basic_word_form

            words_frequency = collections.defaultdict(lambda: 0)

            for line in codecs.open('./files/potop.txt', 'r', 'utf-8'):
                words_from_potop = map(lambda x: x.strip().lower(), line.split())
                for word in words_from_potop:
                    bare_word = re.sub('[~!?@#$%^&*()_+{}":;\'-,.\-`]+', '', word)
                    if bare_word in basic_forms_of_words:
                        basic_word_form = basic_forms_of_words[bare_word]
                        words_frequency[basic_word_form] += 1

            sorted_words = sorted(words_frequency.items(), key=operator.itemgetter(1), reverse=True)

            with codecs.open(self.frequency_txt, 'wb', 'utf-8') as target_file:
                for key, value in sorted_words:
                    target_file.write(key + "," + str(value) + "\n")
                pass
        return sorted_words