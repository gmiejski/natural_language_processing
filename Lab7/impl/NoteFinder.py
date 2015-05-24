import codecs
import operator
from Lab7.impl.Note import Note


class NoteFinder():
    def __init__(self):
        self.notes_by_id = self.notes_by_id()
        self.sorted_idf = None
        pass

    def notes_by_id(self):
        notes_by_id = {}
        for line in codecs.open('./files/pap_short.txt', 'r', 'utf-8'):
            words_from_pap = map(lambda x: x.strip().lower(), line.split())

            if words_from_pap[0].startswith("#"):
                note_id = words_from_pap[0]
                current_note = Note(note_id)
                notes_by_id[note_id] = current_note
            current_note.add_text(line)
            current_note.add_words(words_from_pap)
        return notes_by_id


    def find_notes(self, term, idf, top=3):
        new_map = {}
        for note_id, words_map in idf.iteritems():
            new_map[note_id] = words_map[term]
        sorted_by_occurances = sorted(new_map.items(), key=operator.itemgetter(1), reverse=True)
        containing_word = filter(lambda x: idf[x[0]][term] > 0, sorted_by_occurances)
        sorted_new_map = map(lambda x: x[0], containing_word)
        return map(lambda x: self.notes_by_id[x], sorted_new_map[0:top])

    def key_words_in_notes(self, idf):
        result = {}
        for note_id, note in self.notes_by_id.iteritems():
            idf_for_note = {}
            for word in note.words:
                idf_for_note[word] = idf[note_id][word]

            sorted_key_terms = sorted(idf_for_note.items(), key=operator.itemgetter(1), reverse=True)
            result[note_id] = sorted_key_terms[0:3]
        return result

    def find_notes_by_note(self, note, idf, base_words):

        original_note = self.notes_by_id[note]
        all_notes = map(lambda x: x[0], self.notes_by_id.iteritems())

        notes_by_similiarity = {}
        for note_id, note in self.notes_by_id.iteritems():
            # if note_id is not original_note:
            notes_by_similiarity[note_id] = 0
            for word_in_note in note.words:
                base_word = base_words[word_in_note]
                notes_by_similiarity[note_id] += idf[note_id][base_word]
        sorted_by_similiarity = sorted(notes_by_similiarity.items(), key=operator.itemgetter(1), reverse=True)
        sorted_notes_ids = map(lambda x: x[0], sorted_by_similiarity)

        return map(lambda x: self.notes_by_id[x], sorted_notes_ids[0:3])


