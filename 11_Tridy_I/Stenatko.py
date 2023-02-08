#  Stenatko.py

class Stenatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutnaji!".format(self.jmeno, jidlo))

    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))
        
stenatko = Stenatko('Mia')
stenatko.snez('granulky')

stenatko.zastekej()