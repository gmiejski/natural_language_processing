from NgramSummaryReader import NgramSummaryReader

filesByLanguage = dict(polish=['polski', 'polski2', 'polski3'], spanish=['q', 'spanish', 'spanish1'],
                       finnish=['finnish', 'finnish1'], german=['2momm10', '4momm10', '5momm10', '8momm10'],
                       english=["Harry Potter 1 Sorcerer's_Stone", "Harry Potter 2 Chamber_of_Secrets",
                                "Harry Potter 3 Prisoner of Azkaban", "Harry Potter 4 and the Goblet of Fire"])

ngramSummaryReader = NgramSummaryReader(True)
n = 3

for language, files in filesByLanguage.iteritems():
    ngramSummaryReader.make_ngram_and_save(language, files, n)
