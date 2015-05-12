# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Lab7.impl.NoteFinder import NoteFinder

from Lab7.impl.TfIdf import TfIdf

tf_idf = TfIdf()

tf_idf.tf_idf('do', '#000003')

note_finder = NoteFinder()

notes = note_finder.find_notes("do", tf_idf.idf_matrix())

for note in notes:
    print note.text
