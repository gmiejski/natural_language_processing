from ggplot import *
import pandas as pd


class FrequencyGraphDrawer():
    def __init__(self):
        pass

    def draw(self, sorted_words):
        sorted_words_2 = []
        index = 1
        for tup in sorted_words:
            sorted_words_2.append((index, tup[1]))
            index += 1

        sorted_data = pd.DataFrame(sorted_words_2)
        sorted_data.columns = ['x', 'y']

        f1_data = []
        for tup in sorted_words_2:
            x = tup[0]
            y = float(30000 / x)
            f1_data.append((x, y))
        f1_data = pd.DataFrame(f1_data, columns=['A', 'B'])

        f2_data = []
        for tup in sorted_words_2:
            x = tup[0]
            y = float(300000 / ((x + 3) ** 1.75))
            f2_data.append((x, y))
        f2_data = pd.DataFrame(f2_data, columns=['A', 'B'])

        p = ggplot(sorted_data, aes(x='x', y='y'))
        print p + geom_point() + xlim(0, 50) + ylim(-20000, 20000) + geom_line() + geom_point(f1_data,
                                                                                              aes(x='A', y='B'),
                                                                                              color='blue') + geom_point(
            f2_data, aes(x='A', y='B'), color='red')