def licz14(x1,x2):
    if n == 6:
        return x1 * x1
    elif n == 5:
        import math
        return math.sqrt(x1)
    elif n == 4:
        return x1 / x2
    elif n == 3:
        return x1 * x2
    elif n == 2:
        return x1 - x2
    elif n == 1:
        return x1 + x2
    else:
        return print("Coś poszło nie tak.")
def licz56(x1):
    if n == 6:
        return x1 * x1
    elif n == 5:
        import math
        return math.sqrt(x1)
        return print("Coś poszło nie tak.")
print()
print("Kalkulator")
print()
print('Niniejszy kod umożliwia dokonanie arcytrudnych obliczeń przy użyciu jednego z dostępnych działań.')
print('Wskaż rodzaj działania które chcesz przeprowadzić, posługując się wskazanym numerem działania:')
print()
print('1. Dodawanie')
print('2. Odejmowanie')
print('3. Mnożenie')
print('4. Dzielenie')
print('5. Pierwiastkowanie')
print('6. Potęgowanie')
print()
print('Jakie działanie zamierzasz przeprowadzic? Wskaż numer: ', end = ' ')
n = int(input())
print()
print('Zdecydowałeś się na:',n)
wynik = 0
if n >= 5:
    print('Wskaż liczbę do obliczenia. Wybór potwierdź klawiszem enter: ', end=' ')
    x1 = float(input())
    print('Wskazales liczbe:', x1)
    print()
    print('Wynik działania wynosi: ', licz56(x1))
    wynik = (licz56(x1))
else:
    print('Wskaż dwie liczby do obliczeń. Wprowadź pierwszą liczbę i potwierdź klawiszem enter: ', end = ' ')
    x1 = float(input())
    print('Wskazales liczbe:', x1,' Liczba numer dwa, to:')
    x2 = float(input())
    print('Wskazales liczby',x1,' i ',x2)
    print()
    print('Wynik działania wynosi: ', licz14(x1,x2))
    wynik = licz14(x1)

print('W zaokragleniu: ',(round(wynik,2)))
