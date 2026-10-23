#zadanie9
x = float(input("Wpisz pierwsza liczbe: "))
y = float(input("Wpisz druga liczbe: "))

dodawanie = x+y
odejmowanie = x-y
mnozenie = x*y
potegowanie = x**y

print("Wynik dodawania: ", dodawanie)
print("Wynik odejmowania: ", odejmowanie)
print("Wynik mnozenia: ",mnozenie)

if y == 0:
    print("Wynik dzielenia: nie można dzielić przez zero")
else:
    dzielenie = x/y
    print("Wynik dzielenia: ",dzielenie)

print("Wynik potegowania: ", potegowanie)

