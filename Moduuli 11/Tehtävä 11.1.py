class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivuja):
        Julkaisu.__init__(self, nimi)
        self.kirjoittaja = kirjoittaja
        self.sivuja = sivuja

    def tulosta_tiedot(self):
        print("Kirja: " + self.nimi)
        print("Kirjoittaja: " + self.kirjoittaja)
        print("Sivuja: " + str(self.sivuja))

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        Julkaisu.__init__(self, nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print("Lehti: " + self.nimi)
        print("Päätoimittaja: " + self.paatoimittaja)

lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

print("Julkaisut:")
print("")
lehti.tulosta_tiedot()
print("")
kirja.tulosta_tiedot()
