from itertools import chain

from NgramSummaryReader import NgramSummaryReader
from NgramComparator import NgramComparator

ngramSummaryReader = NgramSummaryReader(False, "./texts_for_test/")
n = 3
unknownFilesByLanguage = dict(polish=['polski', 'polski2'])

unknown_files = list(chain.from_iterable(unknownFilesByLanguage.values()))

d = dict()
ngramComparator = NgramComparator()

for filename in unknown_files:
    ngram = ngramSummaryReader.make_ngram([filename], n)
    language = ngramComparator.find_language(ngram)
    d[filename] = language

for filename, language in d.iteritems():
    print filename + " -> " + language

