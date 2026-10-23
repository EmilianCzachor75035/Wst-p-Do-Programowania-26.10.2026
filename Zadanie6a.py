#zadanie6a
#A) Zmodyfikuj skrypt tak, aby długość przejechanej drogi była generowana losowo 
#(liczba całkowita z zakresu ), a użytkownik podawał aktualną cenę paliwa za litr. 

import random
x = int(random.randint(1,1000))
y = float(input("Podaj średnie spalanie na 100km"))
c = float(input("Podaj aktualną cenę paliwa"))
zuzycie = x * y / 100
koszt = zuzycie * c
print("Wylosowana droga to: ", x ,"Szacowane zuzycie paliwa: ", zuzycie ,"Szacowany koszt podrozy: ", koszt)
