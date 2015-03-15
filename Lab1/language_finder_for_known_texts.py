from itertools import chain

from NgramSummaryReader import NgramSummaryReader
from NgramComparator import NgramComparator


ngramSummaryForKnownTexts = NgramSummaryReader(False)
n = 3

filesByLanguage = dict(polish=['polski', 'polski2', 'polski3'], spanish=['q', 'spanish', 'spanish1'],
                       finnish=['finnish', 'finnish1'], german=['2momm10', '4momm10', '5momm10', '8momm10'],
                       english=["Harry Potter 1 Sorcerer's_Stone", "Harry Potter 2 Chamber_of_Secrets",
                                "Harry Potter 3 Prisoner of Azkaban", "Harry Potter 4 and the Goblet of Fire"])

all_known_files = list(chain.from_iterable(filesByLanguage.values()))

d = dict()
ngramComparator = NgramComparator()

for filename in all_known_files:
    ngram = ngramSummaryForKnownTexts.make_ngram([filename], n)
    language = ngramComparator.find_language(ngram)
    d[filename] = language

for filename, language in d.iteritems():
    print filename + " -> " + language

