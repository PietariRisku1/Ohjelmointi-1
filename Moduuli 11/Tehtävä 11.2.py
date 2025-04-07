class Auto:
    def __init__(self, rek, huippu):
        self.rek = rek
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, uusi):
        self.nopeus = uusi

    def kulje(self, h):
        self.matka = self.matka + self.nopeus * h

class Sahkoauto(Auto):
    def __init__(self, rek, huippu, akku):
        Auto.__init__(self, rek, huippu)
        self.akku = akku

class Polttisauto(Auto):
    def __init__(self, rek, huippu, tankki):
        Auto.__init__(self, rek, huippu)
        self.tankki = tankki

s1 = Sahkoauto("ABC-15", 180, 52.5)
p1 = Polttisauto("ACD-123", 165, 32.3)

s1.kiihdyta(100)
p1.kiihdyta(95)

s1.kulje(3)
p1.kulje(3)

print("Sähköauton matka: " + str(s1.matka) + " km")
print("Polttomoottoriauton matka: " + str(p1.matka) + " km")
