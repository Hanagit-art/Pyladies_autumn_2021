
Prijmeni = input("Zadej prijmeni: ")

def function(Prijmeni):
    if Prijmeni[-3:] == "ova" or Prijmeni[-3:] == "ová":
        return "zena"
    
    else:
        return "muz"
    
print(function(Prijmeni))