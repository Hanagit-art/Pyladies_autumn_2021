
jmeno = "Alfonsi"
soucet = 3 + 4
podpis = "Tva Pylady"

print(f"""Mily {jmeno}
      Vas vysledek je {soucet+1}
S pozdravem,
{podpis}
""")

sablona = """Mily {jmeno},
Vas vysledek je {soucet},
S pozdrem,
{podpis}
"""

print(sablona.format(jmeno=jmeno, soucet=soucet, podispi="Tvuj pritel}"))
print(sablona.format(jmeno="Karle", soucet=4+4, podpis="Neznamy"))

sablona = "Ahoj {jmeno}!"

for j in "Hynku, Vileme, Jarmilo":
    print(sablona.format(jmeno=j))
    # print(f"Nazdar {j}")
