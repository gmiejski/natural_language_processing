class WordsOccurrencesPercentageCalculator:
    def __init__(self):
        pass

    def occurrences(self, percentage, sorted_words):
        all_words = 0
        for tuple in sorted_words:
            all_words += tuple[1]
        current_frequency_sum = 0
        number_of_words = 0
        for tuple in sorted_words:
            current_frequency_sum += tuple[1]
            number_of_words += 1
            if float(current_frequency_sum) / all_words >= (float(percentage) / 100):
                return number_of_words, current_frequency_sum, all_words
        return None, None, None
