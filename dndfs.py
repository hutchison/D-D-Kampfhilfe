#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import readline
from Vorgefertigtes import regdar, eberk, naull, jozan, tordek, kerwyn
from Monster import monster, erschaffe_monster
from Klassen import Monster, Charakter
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
    global gegner
    print str(len(gegner)) + " Gegner in der Liste"
    for g in gegner:
        print unicode(g)

def tp_aendern(p, t):
    if t >= 0:
        p.trefferpunkte = t
    else:
        p.trefferpunkte = max(0, p.trefferpunkte + t) # JA, PLUS!

def fuege_schaden_zu(p, s):
    p.trefferpunkte = p.trefferpunkte - s if s < p.trefferpunkte else 0

def waehle_ziel(ist_monster):
    global party, gegner
    if ist_monster:
        l = party + gegner
    else:
        l = gegner + party
    print u'Wen möchtest du angreifen?'
    for i, a in enumerate(l, 1):
        print unicode(i) + u':',
        if isinstance(a, Charakter):
             print colored(unicode(a.name), 'green')
        else:
             print colored(unicode(a.name), 'red')
    while True:
        wahl = raw_input('1-'+str(len(l))+' # ')
        try:
            if wahl:
                wahl = int(wahl)
                if 1 <= wahl <= len(l):
                    return l[wahl-1]
                else:
                    print wahl, 'hab ich nicht. Nochmal!'
        except ValueError:
            lern_schreiben()

def lese_schaden_ein():
    while True:
        s = raw_input('Wieviel Schaden? ')
        try:
            if s:
                return int(s)
        except ValueError:
            lern_schreiben()

def lern_schreiben():
    print colored(unichr(0x26a1) + u' Lern schreiben!', 'red')


def zeige_kampf():
    global party, gegner, besiegte_gegner
    L = sorted(party + gegner, key=lambda x: x.initiative, reverse=True)
    print (u'Es kämpfen ' + u', '.join([x.name for x in party]) +
           u' gegen ' + u', '.join([x.name for x in gegner]))
    M = len(L)
    i = 0
    while filter(lambda x: isinstance(x, Monster) and x.trefferpunkte > 0, L):
    # solange noch alle Monster am Leben sind:
        m = L[i]
        if m.trefferpunkte:
            print
            print unicode(m)
            print
            while True:
                print (u'weiter [' + unichr(0x21b5) + u' ], Angriff [a]')
                print colored(unichr(0x2694), 'blue'),
                a = raw_input(' ')
                if a:
                    if a == 'a':
                        opfer = waehle_ziel(isinstance(m, Monster))
                        print u'Du brauchst eine', opfer.ruestungsklasse, u'um zu treffen.'
                        schaden = lese_schaden_ein()
                        fuege_schaden_zu(opfer, schaden)
                        print (unicode(opfer.name) + u' hat nun ' + 
                               unicode(opfer.trefferpunkte) + u' TP')
                        if isinstance(opfer, Monster) and not opfer.trefferpunkte:
                            besiegte_gegner.append(opfer)
                            del gegner[gegner.index(opfer)]
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
