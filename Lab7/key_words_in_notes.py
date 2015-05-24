# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Lab7.impl.NoteFinder import NoteFinder

from Lab7.impl.TfIdf import TfIdf

tf_idf = TfIdf()
note_finder = NoteFinder()

key_words_in_notes = note_finder.key_words_in_notes(tf_idf.idf_matrix())

for note_id, key_words in key_words_in_notes.iteritems():
    print note_id
    for pair in key_words:
        print pair[0] + ' - ' + str(pair[1])
