#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Klassen import Charakter, Monster, Attacke, Angriff, Schaden
from Waffen import baue_waffe
from Ruestungen import baue_ruestung

regdar = Charakter(u'Regdar', u'm', 173, 644, u'Mensch', u'Kämpfer', 1, u'Gut',
                   15, 2, 12, 1, 14, 2, 10, 0, 8, -1, 13, 1,
                   1, -1, -1, -3, None, None, 0, -3,
                   1, -1, 4,
                   [baue_ruestung(u'Schuppenpanzer'),],
                   [baue_waffe(u'Zweihänder'), baue_waffe(u'Bogen')], [],
                   [], 11, 4, 12)

eberk = Charakter(u'Eberk', u'm', 103, 1061, u'Zwerg', u'Kleriker', 2, u'Gut',
                  12, 1, 8, -1, 16, 3, 10, 0, 15, 2, 11, 0,
                  1, 2, 2, -7, None, None, 0, -7,
                  -1, 4, 5,
                  [baue_ruestung(u'Kettenpanzer'), baue_ruestung(u'Schild')],
                  [baue_waffe(u'Maxi-Streithammer'), baue_waffe(u'Armbrust')],
                  [],
                  [u'Licht', u'Magie entdecken', u'Magie lesen',
                   u'Leichte Wunden heilen', u'Schutz vor Bösem', u'Segen'],
                  9, 4, 20)

naull = Charakter(u'Naull', u'w', 409, 1468, u'Mensch', u'Magier', 2, u'Gut',
                  10, 0, 14, 2, 13, 1, 15, 2, 12, 1, 8, -1,
                  -1, 3, 1, 2, None, None, 2, 2,
                  2, 4, 1,
                  [],
                  [baue_waffe(u'Kampfstab'), baue_waffe(u'Armbrust')],
                  [],
                  [u'Licht', u'Magie entdecken', u'Magie lesen',
                   u'Magisches Geschoss', u'Schlaf'],
                  12, 6, 10)

jozan = Charakter(u'Jozan', u'm', 99, 1468, u'Mensch', u'Kleriker', 2, u'Gut',
                  12, 1, 8, -1, 14, 2, 10, 0, 15, 2, 13, 1,
                  1, 4, 4, -9, None, None, 0, -7,
                  1, 5, 5,
                  [baue_ruestung(u'Bänderpanzer'), baue_ruestung(u'Schild')],
                  [baue_waffe(u'Schwerer Streitkolben'),
                   baue_waffe(u'Armbrust')],
                  [],
                  [u'Licht', u'Magie entdecken', u'Magie lesen',
                   u'Leichte Wunden heilen', u'Schutz vor Bösem', u'Segen'],
                  9, 4, 13)

tordek = Charakter(u'Tordek', u'm', 132, 1468, u'Zwerg', u'Kämpfer', 2,
                   u'Neutral',
                   15, 2, 13, 1, 16, 3, 10, 0, 12, 1, 6, -2,
                   -2, 1, 1, -7, None, None, 0, -5,
                   1, 1, 6,
                   [baue_ruestung(u'Bänderpanzer'), baue_ruestung(u'Schild')],
                   [baue_waffe(u'Zwergische Streitaxt'), baue_waffe(u'Bogen')],
                   [u'Rucksack'],
                   [],
                   11, 3, 21)

kerwyn = Charakter(u'Kerwyn', u'm', 284, 1351, u'Mensch', u'Schurke', 2,
                   u'Neutral',
                   12, 1, 15, 2, 13, 6, 14, 2, 10, 0, 8, -1,
                   -1, 5, 5, 7, 7, 7, 5, 7,
                   5, 0, 1,
                   [baue_ruestung(u'Lederrüstung')],
                   [baue_waffe(u'Rapier'), baue_waffe(u'Armbrust')],
                   [u'Rucksack', u'3 Fackeln', u'Diebeswerkzeug'],
                   [],
                   16, 6, 13)

z1 = Monster(u'Zombie', 20, 2, 9, 6, 11,
             [Attacke(u'Klaue', Angriff(1, 2), Schaden(1, 6, 1))],
             -1, 3, 0,
             10, None, 9, None,
             [],
             u'Neutral', 100)


if __name__ == '__main__':
    print unicode(regdar)
    print unicode(eberk)
    print unicode(naull)
    print unicode(jozan)
    print unicode(tordek)
    print unicode(kerwyn)
    print unicode(z1)
