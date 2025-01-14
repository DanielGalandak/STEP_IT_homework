# 13.py

'''
Příklady kompozice
    1. Struktura Úřadu vlády
        Sekce > Odbor > Oddělení

    2. Lokomotiva - trakce > vagón > průvodčí > vlak

    3. Seriál - řada - epizoda
'''

class Lokomotiva:
    def __init__(self, rok_vyroby, nazev, trakce='eletkrina'):
        self.rok_vyroby = rok_vyroby
        self.nazev = nazev
        self.trakce = trakce      

class Vagon:
    def __init__(self, pocet=5):
        self.pocet = pocet
        
    def zarad_vagon():
        pocet += 1
        
    def uber_vagon():
        if pocet < 1:
            raise ValueError
        else:
            pocet -=1

class Vlak:
    def __init__(self, lokomotiva: Lokomotiva, vagon: Vagon, linka, start, cil):
        self.vagon = vagon
        self.lokomotiva = lokomotiva
        self.linka = linka
        self.start = start
        self.cil = cil

taurus = Lokomotiva(2008, 'Siemens ES64U4')
vagon = Vagon()
berliner = Vlak(taurus, vagon, 'EC 178', 'Praha hl. n.', 'Berlin Hbf (tief)')

'''
Příklady dědičnosti

    1. smluvní vztah - kupní smlouva
    2. počítač - notebook
    3. boty - gumovky
'''
class Boty:
    def __init__(self, velikost, podrazka, barva, zapinani=True):
        self.velikost = velikost
        self.podrazka = podrazka
        self.barva = barva
        self.zapinani = zapinani

class Gumovky(Boty):
    def __init__(self, vyska, velikost, podrazka, barva, zapinani=False):
        super().__init__(velikost, podrazka, barva, zapinani)
        self.vyska = vyska

    def __repr__(self):
        return (f"Gumovky(vyska={self.vyska}, velikost={self.velikost}, "
                f"podrazka='{self.podrazka}', barva='{self.barva}', zapinani={self.zapinani})")

    def jdi_do_louze(self):
        mokre_ponozky = False
        return mokre_ponozky

gumovky = Gumovky(17, 32, 'guma', 'žluté', False)
print(gumovky)

