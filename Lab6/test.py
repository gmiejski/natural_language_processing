from Lab6.impl.FrequencyGraphDrawer import FrequencyGraphDrawer
from Lab6.impl.FrequencyReader import FrequencyReader

frequency_reader = FrequencyReader()

sorted_words = frequency_reader.word_frequencies_sorted_by_occurrence()
FrequencyGraphDrawer().draw(sorted_words)
words_frequency_dict = frequency_reader.freq_dict()

print 'hapax legomena count = ' + str(min(words_frequency_dict['hapax'], words_frequency_dict['legomena']))

