from Lab6.impl.FrequencyGraphDrawer import FrequencyGraphDrawer
from Lab6.impl.FrequencyReader import FrequencyReader
from Lab6.impl.WordsOccurrencesPercentageCalculator import WordsOccurrencesPercentageCalculator

frequency_reader = FrequencyReader()

sorted_words = frequency_reader.word_frequencies_sorted_by_occurrence()
FrequencyGraphDrawer().draw(sorted_words)
words_frequency_dict = frequency_reader.freq_dict()

print 'hapax legomena count = ' + str(min(words_frequency_dict['hapax'], words_frequency_dict['legomena']))

number_of_words, current_frequency_sum, all_words = WordsOccurrencesPercentageCalculator().occurrences(50, sorted_words)
print 'Number of words: ' + str(number_of_words)
print 'Current frequency sum: ' + str(current_frequency_sum)
print 'All words count: ' + str(all_words)
