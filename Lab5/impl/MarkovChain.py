class MarkovChain():
    def __init__(self, markov_path, ngrams_by_endings):
        possible_sentence_starting_words = filter(lambda x: '.' in x[0], markov_path.keys())
        pass