#zadanie8
a = float(input("Wpisz liczbe a"))
b = float(input("Wpisz liczbe b"))
c = float(input("Wpisz liczbe c"))

if a == 0:
    print("a nie moze byc rowne 0")
else:
    delta = (b ** 2) - (4 * a * c)
    print("delta wynosi: ", delta)

if delta > 0:
    x1 = (-b - (delta ** 0.5)) / (2 * a)
    x2 = (-b + (delta ** 0.5)) / (2 * a)
    print("X1 Wynosi: ", x1, "natomiast X2 wynosi: ", x2)
elif delta == 0:
    x0 = -b / (2 * a)
    print("X0 wynosi: ", x0)
else:
    print("Delta na minusie, brak rozwiązań")