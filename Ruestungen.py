#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Klassen import Ruestung

ruestungen = dict({
    u'Lederrüstung':             (10,    2,  0),
    u'Beschlagene Lederrüstung': (25,    3, -1),
    u'Schuppenpanzer':           (50,    4, -4),
    u'Kettenpanzer':             (150,   5, -5),
    u'Bänderpanzer':             (250,   6, -6),
    u'Ritterrüstung':            (1500,  8, -6),
    u'Schild':                   (7,     2, -2),
})

def baue_ruestung(ruestung):
    if ruestung in ruestungen:
        r = ruestungen[ruestung]
        return Ruestung(ruestung, r[0], r[1], r[2])
