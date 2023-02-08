# Fibonacciho_posloupnost.py

print("Fibonacciho posloupnost: \n")


prvni_cislo = 0
druhe_cislo = 1

for i in range(10):
    soucet = prvni_cislo + druhe_cislo
    prvni_cislo = druhe_cislo
    druhe_cislo = soucet
    print(soucet," ", end="")

    

