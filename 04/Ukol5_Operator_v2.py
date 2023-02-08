
a = int(input('Zadej prvni cislo: '))
b = int(input('Zadej druhe cislo: '))
operator = input('Zadej druh operace(+, -, *, /: ')


if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
    
else:
    print(a / b)


