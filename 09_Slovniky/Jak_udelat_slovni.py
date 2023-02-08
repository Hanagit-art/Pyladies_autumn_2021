# Jak_udelat_slovnik.py

barvy = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

barvy_po_tydnu = dict(barvy)

for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'černo-hnědo-' + barvy_po_tydnu[klic]
print(barvy['meloun'])
print(barvy_po_tydnu)

for klic, hodnota in barvy_po_tydnu.items():    
    print("{}: vyskytuje se {}".format(klic, hodnota)) 
    # print(f"{klic}: vyskytuje se {hodnota}") 

data = [(1, 'jedna'), (2, 'dva'), (3, 'tři')]
nazvy_cisel = dict(data)
print(nazvy_cisel)

popisy_funkci = dict(len='délka', str='řetězec', dict='slovník')
print(popisy_funkci['len'])