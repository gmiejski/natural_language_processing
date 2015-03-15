import operator
from math import sqrt
from os import listdir
from os.path import isfile, join

import codecs


class NgramComparator():
    def __init__(self):
        self.directory = "./ngram_results/"
        self.known_languages = None
        pass

    def find_language(self, ngram):
        known_languages = self.get_known_languages()
        diff_values = dict()

        ngram_copy = dict(ngram)
        for language, language_dict in known_languages.iteritems():
            keys_diff = ngram_copy.viewkeys() ^ language_dict.viewkeys()
            for key in keys_diff:
                if key not in ngram_copy:
                    ngram_copy[key] = 0
                if key not in language_dict:
                    language_dict[key] = 0

            a = sorted(ngram_copy.items(), key=operator.itemgetter(0))
            b = sorted(language_dict.items(), key=operator.itemgetter(0))
            a_values = map(lambda x: x[1], a)
            b_values = map(lambda x: x[1], b)
            diff_value = self.ngram_diff(self.euklidesowa, a_values, b_values)
            diff_values[language] = diff_value
            pass
        return min(diff_values, key=diff_values.get)

    def ngram_diff(self, method, ngram1, ngram2):
        return method(ngram1, ngram2)

    def euklidesowa(self, ngram1, ngram2):
        sum = 0.0
        for i in range(0, len(ngram1)):
            sum += float((ngram1[i] - ngram2[i]) ** 2)
        return sqrt(sum)

    def get_known_languages(self):
        if self.known_languages is None:
            all_ngrams = dict()
            only_files = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
            for filename in only_files:
                lines = []
                with codecs.open(self.directory + filename, 'rb', 'utf-8') as csvfile:
                    for line in csvfile:
                        lines.append(line.split(','))
                language_summary = dict((rows[0], float(rows[1])) for rows in lines)
                all_ngrams[filename] = language_summary
            self.known_languages = all_ngrams
        return self.known_languages