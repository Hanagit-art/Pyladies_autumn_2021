class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def snez(self, jidlo):
        print("{}: {} mi vůbec nechutná!".format(self.jmeno, jidlo))
        super().snez(jidlo)
        
    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))


class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))

class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)


micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('myš')
azorek.snez('kost')

standa = Hadatko('Stanislav')
standa.snez('myš')