#zadanie1b
#B)	Sprawdź i wyjaśnij działanie następujących instrukcji:  
#1.	int(3.0)  
#2.	float(3) 
#3.	float("3")  
#4.	str(12.4)  
#5.	bool(0) 

z = int(3.0) #funkcja int zmienia liczbe zmiennoprzecinkowa w liczbe calkowita dopisujac czesc dziesietna.
x = float(3) #funkcja float  zmienia liczbe calkowita w ulamkowa dopisujac czesc dziesietna.
c = float("3") #wszystko wpisane w cudzyslow jest traktowane jako tekst. Funkcja Float sprawia ze cyfry wpisane w cudzyslow z tekstu sa zamieniane na cyfry tak aby mozna bylo wykonywac na niej dzialania.
v = str(12.4 ) #funkcja str sprawia ze cyfry sa zmieniane na tekst wiec nie bedzie mozliwe dokonywanie na nich obliczen
b = bool(0) #jest to wartosc logiczna ktora moze byc tylko prawda lub falszem.
print(type(z),type(x),type(c),type(v),type(b))
