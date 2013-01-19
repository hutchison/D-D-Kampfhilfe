#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import readline
from Vorgefertigtes import regdar, eberk, naull, jozan, tordek, kerwyn
from Monster import monster, erschaffe_monster
from Klassen import Monster
from termcolor import colored

party = [regdar, eberk, naull, jozan, tordek, kerwyn]
gegner = []
besiegte_gegner = []

def liste_party_auf():
    for a in party:
        print unicode(a)

def liste_vordef_monster_auf():
    for m in monster.keys():
        print unicode(m)

def create_monster():
    M = monster.keys()
    N = len(M)
    print "Folgende Monster haben wir im Angebot:"
    for mt, i in zip(M, range(N)):
        print str(i+1) + ':', mt
    i = int(raw_input('# ') or 1)
    s = M[i-1]
    if s in monster:
        anz = int(raw_input('Wie viele? ') or 1)
        for i in range(anz):
            m = erschaffe_monster(s)
            # Wie viele Monster gleichen Typs gibt es schon in der Gegnerliste?
            n = len(filter(lambda x: isinstance(x, type(m)), gegner))
            m.name += u' ' + unicode(n+1)
            print "Erschaffe", m.name
            gegner.append(m)
    else:
        print s, "kenne ich nicht. Breche ab."


def beende_mich():
    print 'Bye'
    sys.exit()

def kommandoliste():
    print ', '.join(sorted(cmds.keys()))

def liste_gegner_auf():
    print str(len(gegner)) + " Gegner in der Liste"
    for g in gegner:
        print unicode(g)

def tp_aendern(p, t):
    if t > 0:
        p.trefferpunkte = t
    else:
        p.trefferpunkte = max(0, p.trefferpunkte+t) # JA, PLUS!

def zeige_kampf():
    global gegner
    L = sorted(party + gegner, key=lambda x: x.initiative, reverse=True)
    print (u'Es kämpfen ' + u', '.join([x.name for x in party]) +
           u' gegen ' + u', '.join([x.name for x in gegner]))
    M = len(L)
    i = 0
    while filter(lambda x: isinstance(x, Monster) and x.trefferpunkte > 0, L):
        m = L[i]
        if m.trefferpunkte:
            print
            print unicode(m)
            print
            while True:
                print (u'Aktionen: weiter [' + unichr(0x21b5) +
                       u' ], TP ändern [t]')
                print colored(unichr(0x2694), 'blue'),
                a = raw_input(' ')
                if a:
                    if a == 't':
                        t = int(raw_input('# ') or 0)
                        tp_aendern(m, t)
                        print (unicode(m.name) + u' hat nun ' + 
                               unicode(m.trefferpunkte) + u' TP')
                        if isinstance(m, Monster):
                            besiegte_gegner.append(m)
                        break
                    else:
                        print colored(unichr(0x26a1) + u' ' + unicode(a)
                                      + u' kenne ich nicht.', 'red')
                else:
                    break
        i = (i+1) % M
    print 'Kampf beendet.'
    print u', '.join([x.name for x in L if x.trefferpunkte > 0]), u'haben überlebt.'
    print u', '.join([x.name for x in besiegte_gegner]), u'wurden besiegt.'
    gegner = []

cmds = dict({
    'exit': beende_mich,
    'ls': liste_party_auf,
    'lm': liste_vordef_monster_auf,
    'cm': create_monster,
    'cmds': kommandoliste,
    'le': liste_gegner_auf,
    'fi': zeige_kampf,
})

def main():
    c = ''
    print "Eingebaute Befehle:",
    kommandoliste()

    while c != 'exit':
        try:
            c = raw_input('>>> ').strip()
            if c in cmds:
                cmds[c].__call__()
            elif not c:
                continue
            else:
                print c + " kenne ich nicht."
        except EOFError:
            print
            beende_mich()

if __name__ == '__main__':
    main()
