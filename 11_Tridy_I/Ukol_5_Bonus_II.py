
class Clovek:
    def __init__(self, jmeno, prijmeni, rd):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.rd = rd
       
    # def __repr__(self):
    #     return "Jmenuji se {} {} a me inicialy jsou {}. Jsem {} rok narozeni {} a narozeniny mam {}.{}.".format(self.jmeno, self.prijmeni, self.inicialy(), 
    #     self.process_s(), self.process_y(), self.process_d(), self.process_m())
        
    def run_name(self):
        print(self.jmeno, self.prijmeni)
        
    def test_jmeno(self):
        print(self.jmeno[0].isupper() and self.jmeno[1:].islower(),',', 
            self.prijmeni[0].isupper() and self.prijmeni[1:].islower(),)
        
    def inicialy(self):
        return (self.jmeno[0] + self.prijmeni[0]).upper()
    
    def process_y(self):
        """year"""
        if int(self.rd[0:2]) >= 54:
            year = "19"+self.rd[0:2]
        else:
            year = "20"+self.rd[0:2]
        return year
    
    def process_m(self):
        
        """month"""
        if int(self.rd[2]) == 5 or int(self.rd[2]) == 0:
            month = int(self.rd[3])
        elif int(self.rd[2]) == 1:
            month = int(self.rd[2:4])
        else: 
            month = int(self.rd[3])+10
        return month
    
    def process_d(self):
        
        """day"""
        if int(self.rd[4]) == 0:
            day = self.rd[5] 
        else:
            day = self.rd[4:6]
        return day
        
    def process_s(self):
            
        """sex"""
        if int(self.rd[2]) > 1:
            sex = "<female>"
        else:
            sex = "<male>"
                
        return sex
                
    def kdo_jsi(self):
        print("Jmenuji se {} {} a me inicialy jsou {}. Jsem {} rok narozeni {} a narozeniny mam {}.{}.".format(self.jmeno, self.prijmeni, self.inicialy(), 
        self.process_s(), self.process_y(), self.process_d(), self.process_m()))
        
osoba = Clovek('Anna', 'Nova', "0062021234")
# osoba = Clovek('jan', 'malý', '0007021234')
osoba.run_name()
osoba.test_jmeno()
osoba.kdo_jsi()
# print(osoba.inicialy())
# print(osoba)



