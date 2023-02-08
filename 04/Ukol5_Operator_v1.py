
import operator

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv 
}

a = int(input('Zadej prvni cislo: '))
b = int(input('Zadej druhe cislo: '))
oper = input('Zadej druh operace(+, -, *, /: ')

print(a, oper, b, '=', operator_dict[oper](int(a), int(b)))