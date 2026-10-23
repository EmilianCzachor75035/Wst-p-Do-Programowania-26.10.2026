#zadanie6
#Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych kosztach podróży (cena paliwa 6.5 zł/l). 

x = float(input("Podaj pokonaną drogę w kilometrach"))
y = float(input("Podaj średnie spalanie na 100km"))
c = 6.5
zuzycie = x * y / 100
koszt = zuzycie * c
print("Szacowane zuzycie paliwa: " , zuzycie , " Szacowany koszt podrozy: " , koszt)
