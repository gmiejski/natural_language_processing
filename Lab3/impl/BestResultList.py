class BestResultList():
    def __init__(self):
        self.list = []

    def append(self, probability, word):
        self.list.append((probability, word))
        self.list.sort(key=lambda a: a[0])
        if len(self.list) > 5:
            self.list = self.list[1:]
        pass

    def get_results(self):
        return self.list

    def print_results(self):
        for x in self.list:
            print x


class ProbDist:
    def __init__(self, probability, word):
        self.probability = probability
        self.word = word

    def __str__(self):
        return "(" + str(self.probability) + ", " + self.word + ")"



