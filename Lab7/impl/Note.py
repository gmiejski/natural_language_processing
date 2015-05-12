class Note():
    def __init__(self, note_id):
        self.note_id = note_id
        self.text = ''
        self.words = []

    def add_words(self, words):
        self.words += words

    def add_text(self, text):
        self.text += text

    def text(self):
        return self.text


    def words(self):
        return self.words

    def __str__(self):
        return self.text
