

class Kocka:
    def __init__(self):
        self.pocet_zivotu = 4
        
    def zamnoukej(self):
        print("Mnau, mnau, mnauuu!")   
    
    def je_ziva(self):
        return self.pocet_zivotu > 0
            
    def uber_zivot(self):
        if not self.je_ziva():
            print('Nemuzu zabit mrtvou kocku!')
        else:
            self.pocet_zivotu -= 1
            
    def snez(self, jidlo):
        if not self.je_ziva():
            print("Je zbytecne krmit mrtvou kocku!")
            # return
        elif jidlo == "ryba" and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print("Kocka spapala rybu a obnovil se ji jeden zivot.")
        else:
            print("Kocka se krmi.")
            
micka = Kocka()
print(micka.pocet_zivotu)
micka.je_ziva()
micka.uber_zivot()
# micka.snez("mys")
micka.snez("ryba")