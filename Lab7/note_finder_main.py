# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Lab7.impl.NoteFinder import NoteFinder

from Lab7.impl.TfIdf import TfIdf

tf_idf = TfIdf()
note_finder = NoteFinder()

while True:
    print ''
    term = raw_input('term: ')
    notes = note_finder.find_notes(unicode(term, 'utf-8'), tf_idf.idf_matrix())
    for note in notes:
        print note.text

