#  Zviratko.py

class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))


class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))


micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('myš')
azorek.snez('kost')

"--------------------------------------------------------------------------------------------"

# class Kotatko(Zviratko):
    
#     def zamnoukej(self, zprava):
#         print("{}: Mnau! {}".format(self.jmeno, zprava))
        
# class MlsneKotatko(Kotatko):
    
#     def zamnoukej(self, zprava):
#         print("{}: Mnam! {} mi velmi chutna.".format(self.jmeno, zprava))
        
#     def snez(self, jidlo):
#         print("{}: Fuj! {} mi vubec nechutna. Ja radeji zverinu.".format(self.jmeno, jidlo))
    
# mlsne_kotatko = MlsneKotatko("Mlsoun")
# mlsne_kotatko.zamnoukej("Mam hlad!")