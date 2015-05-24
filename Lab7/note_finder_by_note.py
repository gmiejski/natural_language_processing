# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Lab7.impl.NoteFinder import NoteFinder

from Lab7.impl.TfIdf import TfIdf

tf_idf = TfIdf()
note_finder = NoteFinder()

notes = note_finder.find_notes_by_note('#000001', tf_idf.idf_matrix(), tf_idf.basic_form_of_words)
for note in notes:
    print note.text
