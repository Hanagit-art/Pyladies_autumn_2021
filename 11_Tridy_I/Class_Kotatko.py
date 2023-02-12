
class Kotatko:
    def __init__(self, jmeno, inicialy):
        self.jmeno = jmeno
        self.inicialy = inicialy
        
    def __str__(self):
        print('<Kotatko jmenem {}>'.format(self.jmeno))
        
    def zamnoukej(self):
        print("{}: Mnau!".format(self.jmeno))
        
    def snez(self, jidlo):
        print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))
        
mourek = Kotatko('Mourek')
# mourek.jmeno = "Mourek"
mourek.snez("Ryba")

micka = Kotatko("Micka")
# micka.jmeno = "Micka"

mourek.zamnoukej()
micka.zamnoukej()
# print(mourek)
mourek.__str__()
# print(mourek.jmeno)
# print(micka.jmeno)



