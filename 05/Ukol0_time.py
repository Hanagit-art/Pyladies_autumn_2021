
# Napis funkci, ktere bere 2 argumenty - minuty a sekunky, ale vraci cas v sekundach.

from datetime import datetime

now = datetime.now()
sec = '{:02d}'.format(now.second)
minute = '{:02d}'.format(now.minute)
hour = '{:02d}'.format(now.hour)
hour_min = 60 * hour # nelze, udela to 60 * "15"

# min = 25
# sek = 45

min = int(minute)
sek = int(sec)

def pocet_vterin(min, sek):
      sek =  60*min + sek
      return sek
  
print(pocet_vterin(min, sek))

# print(sec)
print(now)

