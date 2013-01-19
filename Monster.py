#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Klassen import Monster, Attacke, Angriff, Schaden

monster = dict({
    # TODO:
    u'Zombie': (u'Zombie', 20, 2, 9, 6, 11,
                [Attacke(u'Klaue', Angriff(1, 2), Schaden(1, 6, 1))],
                -1, 3, 0,
                10, None, 9, None,
                [],
                u'Neutral', 100),
})

def erschaffe_monster(s):
    if s in monster:
        m = monster[s]
        return Monster(m[0], m[1], m[2], m[3], m[4], m[5],
                       m[6],
                       m[7], m[8], m[9],
                       m[10], m[11], m[12], m[13],
                       m[14],
                       m[15], m[16])
