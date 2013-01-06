#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Klassen import Nahkampfwaffe, Fernkampfwaffe

nahkampfwaffen = dict({
    # Name                      Preis  Schaden  beidhändig  Angriffsbonus
    u'Kampfstab':                (0,   (1, 6),  True,       0),
    u'Kurzschwert':              (10,  (1, 6),  False,      0),
    u'Rapier':                   (20,  (1, 6),  False,      0),
    u'Morgenstern':              (8,   (1, 8),  False,      0),
    u'Schwerer Streitkolben':    (12,  (1, 8),  False,      0),
    u'Streithammer':             (12,  (1, 8),  False,      0),
    u'Maxi-Streithammer':        (312, (1, 8),  False,      1),
    u'Langschwert':              (15,  (1, 8),  False,      0),
    u'Zwergische Streitaxt':     (30,  (1, 10), False,      0),
    u'Zweihändige Axt':          (20,  (1, 12), True,       0),
    u'Zweihänder':               (50,  (2, 6),  True,       0),
})

fernkampfwaffen = dict({
    u'Bogen':    (30, (1, 6)),
    u'Armbrust': (35, (1, 8)),
})

def baue_waffe(waffe):
    if waffe in nahkampfwaffen:
        w = nahkampfwaffen[waffe]
        return Nahkampfwaffe(waffe, w[0], w[1], w[2], w[3])
    elif waffe in fernkampfwaffen:
        w = fernkampfwaffen[waffe]
        return Fernkampfwaffe(waffe, w[0], w[1])
