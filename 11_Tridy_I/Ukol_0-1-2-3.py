# from cgi import print_environ


class Clovek:
    def __init__(self, jmeno, prijmeni):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        
    def run_name(self):
        print(self.jmeno, self.prijmeni)
        
    def test_jmeno(self):
        print(self.jmeno[0].isupper() and self.jmeno[1:].islower(),',', 
            self.prijmeni[0].isupper() and self.prijmeni[1:].islower(),)
        
    def inicialy(self):
        return (self.jmeno[0] + self.prijmeni[0]).upper()
        
    def kdo_jsi(self):
        print("Jmenuji se {} {} a me inicialy jsou {}.".format(self.jmeno, self.prijmeni, self.inicialy()))
        
osoba = Clovek('anna', 'NOva')
osoba.run_name()
osoba.test_jmeno()
osoba.kdo_jsi()
print(osoba.inicialy())
