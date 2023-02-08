# Ukol2.py

string = "Máme rádi PyLadies!"
string = string.replace(" ", "")
# string = list(string) # tento radek neni treba, i retezec se da prochazet znak po znaku

print(string, "\n")

def frequency(string):
    freq = {}
    for key in string:
        freq[key] = freq.get(key,0) +1
    return freq

print(frequency(string))

"------------------------------------------------------"

# l = string.split()
# print(l)
# keys = []
# for i in range(3):
#     i = list(l[i])
#     keys.append(i)
    
# print(keys)
# keys = (list(l[0])) + (list(keys[1])) + (list(keys[2]))
# print(keys)
