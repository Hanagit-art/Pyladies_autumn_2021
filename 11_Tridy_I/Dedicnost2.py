#  Dedicnost2.py

class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return '<Kotatko jmenem {}>'.format(self.jmeno)

    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))
        
    def zamnoukej(self, zprava):
        print('{}: {}' . format(self.jmeno, zprava))

kotatko = Kotatko('Mourek')
kotatko.zamnoukej("Mnau!")
kotatko.snez("Mys")
print(kotatko)