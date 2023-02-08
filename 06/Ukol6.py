"Napiš funkci, která vypíše čísla od jedné do 100, ale:"

"Pokud je číslo dělitelné třemi, napíše místo něj bum."
"Pokud je číslo dělitelné pěti, napíše místo něj bác."
"Pokud je číslo dělitelné pěti i třemi zároveň, napíše místo toho bum-bác."
"""Napiš funkci, která vypíše čísla od jedné do 100, ale:

Pokud je číslo dělitelné třemi, napíše místo něj "bum".
Pokud je číslo dělitelné pěti, napíše místo něj "bác".
Pokud je číslo dělitelné pěti i třemi zároveň, napíše místo toho "bum-bác"."""


def vypis_cislo(N): 
    
    for i in range(1, N+1):

        if i%3 == 0 and i%5 == 0:
            print("bum-bac")
    
        elif i%3 == 0:
            print("bum")
        
        elif i%5 == 0:
            print("bac")
        
        else:
            print(i)

vypis_cislo(100)

