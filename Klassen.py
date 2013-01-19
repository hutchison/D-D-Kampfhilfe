#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from termcolor import colored

class Charakter(object):
    """Ein normaler Charakter."""

    tab_grundangriffsbonus = dict({
        u'Kämpfer': [1, 2, 3, 4, 5,
                (6, 1), (7, 2), (8, 3), (9, 4), (10, 5),
                (11, 6, 1), (12, 7, 2), (13, 8, 3), (14, 9, 4), (15, 10, 5),
                (16, 11, 6, 1), (17, 12, 7, 2), (18, 13, 8, 3), (19, 14, 9, 4),
                (20, 15, 10, 5)],
        u'Kleriker': [0, 1, 2, 3, 3, 4, 5,
                (6, 1), (6, 1), (7, 2), (8, 3), (9, 4), (9, 4), (10, 5),
                (11, 6, 1), (12, 7, 2), (12, 7, 2), (13, 8, 3), (14, 9, 4),
                (15, 10, 5)],
        u'Schurke': [0, 1, 2, 3, 3, 4, 5,
                (6, 1), (6, 1), (7, 2), (8, 3), (9, 4), (9, 4), (10, 5),
                (11, 6, 1), (12, 7, 2), (12, 7, 2), (13, 8, 3), (14, 9, 4),
                (15, 10, 5)],
        u'Magier': [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
                (6, 1), (6, 1), (7, 2), (7, 2), (8, 3), (8, 3), (9, 4), (9, 4),
                (10, 5)],
    })

    groessenmod = dict({
        u'kolossal': -8,
        u'riesig': -4,
        u'sehr groß': -2,
        u'groß': -1,
        u'normal': 0,
        u'klein': 1,
        u'sehr klein': 2,
        u'winzig': 4,
    })

    volksgroesse = dict({
        u'Mensch': u'normal',
        u'Zwerg': u'normal',
        u'Halbling': u'klein',
        u'Elf': u'normal',
    })

    def __init__(self,
                 name=u'',
                 geschlecht=u'',
                 goldmuenzen=0,
                 erfahrungspunkte=0,
                 volk=u'',
                 klasse=u'',
                 stufe=1,
                 gesinnung='',
                 staerke=10, staerkebonus=0,
                 geschicklichkeit=10, geschicklichkeitsbonus=0,
                 konstitution=10, konstitutionsbonus=0,
                 intelligenz=10, intelligenzbonus=0,
                 weisheit=10, weisheitsbonus=0,
                 charisma=10, charismabonus=0,
                 diplomatie=None, entdecken=None, lauschen=None,
                 leise_bewegen=None, mechanismus_ausschalten=None,
                 schloesser_oeffnen=None, suchen=None, verstecken=None,
                 reflex=0, willen=0, zaehigkeit=0,
                 ruestung=[],
                 waffen=[],
                 ausruestung=[],
                 zauber=[],
                 initiative=0, bewegungsrate=0, trefferpunkte=1):
        self.name = name
        self.geschlecht = geschlecht
        self.goldmuenzen = goldmuenzen
        self.erfahrungspunkte = erfahrungspunkte
        self.volk = volk
        self.klasse = klasse
        self.stufe = stufe
        self.gesinnung = gesinnung
        self.staerke = staerke
        self.staerkebonus = staerkebonus
        self.geschicklichkeit = geschicklichkeit
        self.geschicklichkeitsbonus = geschicklichkeitsbonus
        self.konstitution = konstitution
        self.konstitutionsbonus = konstitutionsbonus
        self.intelligenz = intelligenz
        self.intelligenzbonus = intelligenzbonus
        self.weisheit = weisheit
        self.weisheitsbonus = weisheitsbonus
        self.charisma = charisma
        self.charismabonus = charismabonus
        self.diplomatie = diplomatie
        self.entdecken = entdecken
        self.lauschen = lauschen
        self.mechanismus_ausschalten = mechanismus_ausschalten
        self.schloesser_oeffnen = schloesser_oeffnen
        self.suchen = suchen
        self.verstecken = verstecken
        self.reflex = reflex
        self.willen = willen
        self.zaehigkeit = zaehigkeit
        self.ruestung = ruestung
        self.waffen = waffen
        self.ausruestung = ausruestung
        self.zauber = zauber
        self.initiative = initiative
        self.bewegungsrate = bewegungsrate
        self.trefferpunkte = trefferpunkte

    def __str__(self):
        g = self.geschlecht
        r = colored(unichr(0x2606) + u' {name}'.format(name=self.name),
                    'green')
        r += u' ist {artikel} {volk} {klasse}'.format(
            name=self.name,
            artikel=gend_adj(u'Artikel', g),
            volk=gend_adj(self.volk, g),
            klasse=gend_adj(self.klasse, g)
        )
        r += u' der Stufe {stufe} mit {gold}GM und {xp}EP.\n'.format(
            stufe=self.stufe,
            gold=self.goldmuenzen,
            xp=self.erfahrungspunkte,
        )
        r += u'  Initative: {:2d}'.format(self.initiative)
        r += u'  Bewegungsrate: {bew}\n'.format(bew=self.bewegungsrate)

        """
        r += '### Attributswerte\n'
        r += '  ST: {:2d} {:+d}\n'.format(self.staerke, self.staerkebonus)
        r += '  GE: {:2d} {:+d}\n'.format(self.geschicklichkeit,
                                          self.geschicklichkeitsbonus)
        r += '  KO: {:2d} {:+d}\n'.format(self.konstitution,
                                          self.konstitutionsbonus)
        r += '  IN: {:2d} {:+d}\n'.format(self.intelligenz,
                                          self.intelligenzbonus)
        r += '  WE: {:2d} {:+d}\n'.format(self.weisheit, self.weisheitsbonus)
        r += '  CH: {:2d} {:+d}\n'.format(self.charisma, self.charismabonus)

        r += '### Fertigkeiten\n'
        r += '  Diplomatie:\n'
        r += '  Entdecken:\n'
        r += '  Lauschen:\n'
        r += '  Leise bewegen:\n'
        r += '  Mechanismus ausschalten:\n'
        r += '  Schlösser öffnen:\n'
        r += '  Suchen:\n'
        r += '  Verstecken:\n'
        """

        r += u'### Waffen\n'
        for w in self.waffen:
            r += u'  ' + w.kurz_mit_boni(self.angriffsbonus(w),
                                        self.schadensbonus(w)) + u'\n'

        if self.ruestung:
            r += u'### Rüstung\n'
            for rs in self.ruestung:
                r += u'  ' + unicode(rs) + '\n'

        r += u'Rüstungsklasse: {rk}\n'.format(rk=self.ruestungsklasse())
        r += u'Trefferpunkte: {tp:2d}'.format(tp=self.trefferpunkte)

        return r

    def waffe_hinzufuegen(self, w):
        self.waffen.append(w)

    def waffe_entfernen(self, w):
        if w in self.waffen:
            self.waffen.remove(w)

    def grundangriffsbonus(self):
        return self.tab_grundangriffsbonus[self.klasse][self.stufe-1]

    def angriffsbonus(self, waffe):
        ab = (self.grundangriffsbonus() +
              self.groessenmod[self.volksgroesse[self.volk]])
        if isinstance(waffe, Nahkampfwaffe):
            if self.klasse == u'Kämpfer':
                ab += 1
            return ab + self.staerkebonus
        elif isinstance(waffe, Fernkampfwaffe):
            return ab + self.geschicklichkeitsbonus
        else:
            return 0

    def schadensbonus(self, waffe):
        if isinstance(waffe, Nahkampfwaffe):
            b = self.staerkebonus
            if waffe.beidhaendig:
                b = int(math.floor(1.5 * self.staerkebonus))
            return b
        else:
            return 0

    def ruestungsbonus(self):
        return sum([x.rk_bonus for x in self.ruestung]) if self.ruestung else 0

    def ruestungsklasse(self):
        rk = 10 + self.geschicklichkeitsbonus
        rl = [rk]
        for r in self.ruestung:
            rk += r.rk_bonus
            rl.append(rk)
        return tuple(rl)


class Waffe(object):
    """Eine generische Waffe."""
    def __init__(self, name='', preis=0, schaden=(1,6), beidhaendig=False,
                 angriffsbonus=0):
        self.name = name
        self.preis = preis
        self.schaden = schaden
        self.beidhaendig = beidhaendig
        self.angriffsbonus = angriffsbonus

    def __str__(self):
        s = u'{0}, {1}W{2}, {3}GM'.format(
            self.name, self.schaden[0], self.schaden[1], self.preis)
        if self.beidhaendig:
            s += u', beidhändig'
        else:
            s += u', einhändig'
        if self.angriffsbonus:
            s += u' {:+d} Angriffsbonus'
        return s

    def kurz_mit_boni(self, fremd_angr_b, schad_b):
        s = u'{:<21}'.format(self.name)
        if self.angriffsbonus:
            fremd_angr_b += self.angriffsbonus
        if fremd_angr_b and schad_b:
            return s + u'  1W20{0:+d}  {1}W{2}{3:+d}'.format(
                fremd_angr_b, self.schaden[0], self.schaden[1], schad_b)
        elif fremd_angr_b:
            return s + u'  1W20{0:+d}  {1}W{2}'.format(
                fremd_angr_b, self.schaden[0], self.schaden[1])
        elif schad_b:
            return s + u'  1W20    {0}W{1}{2:+d}'.format(
                self.schaden[0], self.schaden[1], schad_b)
        else:
            return s + u'  1W20    {0}W{1}'.format(
                self.schaden[0], self.schaden[1])

class Nahkampfwaffe(Waffe):
    """Eine Nahkampfwaffe."""
    def __init__(self, name='', preis=0, schaden=(1,6), beidhaendig=False,
                 angriffsbonus=0):
        super(Nahkampfwaffe, self).__init__(name, preis, schaden, beidhaendig,
                                           angriffsbonus)

class Fernkampfwaffe(Waffe):
    """Eine Fernkampfwaffe ist immer beidhändig."""
    def __init__(self, name='', preis=0, schaden=(1,6)):
        super(Fernkampfwaffe, self).__init__(name, preis, schaden, True)

class Ruestung(object):
    """Eine Rüstung."""
    def __init__(self, name='', preis=0, rk_bonus=2, malus=0):
        self.name = name
        self.preis = preis
        self.rk_bonus = rk_bonus
        self.malus = malus

    def __str__(self):
        s = u'{name}, {preis}GM, {rk_bonus:+d} RK-Bonus'.format(
            name=self.name, preis=self.preis, rk_bonus=self.rk_bonus)
        s += u', {malus: d} R-Malus'.format(malus=self.malus)
        return s

class Monster(object):
    """Ein Monster."""
    def __init__(self, name=u'', trefferpunkte=1, trefferwuerfel=1,
                 initiative=1, bewegungsrate=1, ruestungsklasse=0,
                 attacken=[],
                 reflex=0, willen=0, zaehigkeit=0,
                 entdecken=None, lauschen=None, leise_bewegen=None,
                 verstecken=None,
                 ausruestung=[],
                 gesinnung=u'Böse', erfahrungspunkte=0):
        self.name = name
        self.trefferpunkte = trefferpunkte
        self.trefferwuerfel = trefferwuerfel
        self.initiative = initiative
        self.bewegungsrate = bewegungsrate
        self.ruestungsklasse = ruestungsklasse
        self.attacken = attacken
        self.reflex, self.willen, self.zaehigkeit = reflex, willen, zaehigkeit
        self.entdecken, self.lauschen = entdecken, lauschen
        self.leise_bewegen, self.verstecken = leise_bewegen, verstecken
        self.ausruestung = ausruestung
        self.gesinnung = gesinnung
        self.erfahrungspunkte = erfahrungspunkte

    def __str__(self):
        r =  colored(unichr(0x2620) + u'  {name}\n'.format(name=self.name),
                     'red', attrs=['blink'])
        r += u'TP {tp:2d}   IN {ini:2d}\n'.format(tp=self.trefferpunkte,
                                               ini=self.initiative)
        r += u'RK {rk:2d}   BR {br:2d}'.format(rk=self.ruestungsklasse,
                                              br=self.bewegungsrate)
        return r

class Attacke(object):
    """Eine Attacke eines Monsters. Bestehend aus Name, Angriff und Schaden."""
    def __init__(self, name=u'', angriff=None, schaden=None):
        self.name = name
        self.angriff = angriff
        self.schaden = schaden

    def __str__(self):
        r = self.name + u'  '
        r += u'A: ' + unicode(self.angriff) + u'  S: '
        if self.angriff.anzahl > 1:
            r += u'{anz}×'.format(anz=self.angriff.anzahl)
        r += unicode(self.schaden)
        return r

class Angriff(object):
    """Angriff eines Monsters."""
    def __init__(self, anzahl=1, bonus=0):
        self.anzahl = anzahl
        self.bonus = bonus

    def __str__(self):
        r = u''
        if self.anzahl > 1:
            r += u'{anz}×'.format(anz=self.anzahl)
        r += u'1W20'
        if self.bonus:
            r += u'{bon:+d}'.format(bon=self.bonus)
        return r

class Schaden(object):
    """Schaden eines Monsters."""
    def __init__(self, anzahl_wuerfel=1, seiten=4, bonus=0):
        self.anzahl_wuerfel = anzahl_wuerfel
        self.seiten = seiten
        self.bonus = bonus

    def __str__(self):
        r = u'{anz}W{sei}'.format(anz=self.anzahl_wuerfel, sei=self.seiten)
        if self.bonus:
            r += u'{bon:+d}'.format(bon=self.bonus)
        return r

def gend_adj(a, g):
    aspekte = dict({
        u'Artikel': (u'ein', u'eine'),
        u'Mensch': (u'menschlicher', u'menschliche'),
        u'Kämpfer': (u'Kämpfer', u'Kämpferin'),
        u'Zwerg': (u'zwergischer', u'zwergische'),
        u'Kleriker': (u'Kleriker', u'Klerikerin'),
        u'Magier': (u'Magier', u'Magierin'),
        u'Schurke': (u'Schurke', u'Schurkin'),
    })
    if g == u'm':
        return aspekte[a][0]
    else:
        return aspekte[a][1]
