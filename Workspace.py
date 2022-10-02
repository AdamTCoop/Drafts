def dzial_1(x1,x2):
    return x1 + x2
def dzial_2(x1,x2):
    return x1 - x2
def dzial_3(x1,x2):
    return x1 * x2
def dzial_4(x1,x2):
    return x1 / x2
def dzial_5(x1):
    return x1 / x1
def dzial_6(x1):
    return x1 * x1

print("Kalkulator by CooperAT Corporate")
print()
print('Niniejsze oprogramowanie umożliwia dokonanie arcytrudnych obliczeń przy użyciu jednego z dostępnych działań.')
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
print('Zdecydowałeś się na',n)
print()
if n == 6:
    print('Wskaż liczbę do obliczenia: ', end=' ')
    x1 = int(input())
    print('Wynik działania wynosi: ',dzial_6(x1))
elif n == 5:
    print('Wskaż liczbę do obliczenia: ', end=' ')
    x1 = int(input())
    print('Wynik działania wynosi: ',dzial_5(x1))
elif n == 4:
    print('Wskaż dwie liczby do obliczeń: ', end = ' ')
    x1 = int(input())
    x2 = int(input())
    print('Wynik działania wynosi: ', dzial_4(x1,x2))
elif n == 3:
    print('Wskaż dwie liczby do obliczeń: ', end = ' ')
    x1 = int(input())
    x2 = int(input())
    print('Wynik działania wynosi: ', dzial_3(x1,x2))
elif n == 2:
    print('Wskaż dwie liczby do obliczeń: ', end = ' ')
    x1 = int(input())
    x2 = int(input())
    print('Wynik działania wynosi: ', dzial_2(x1,x2))
elif n == 1:
    print('Wskaż dwie liczby do obliczeń: ', end = ' ')
    x1 = int(input())
    x2 = int(input())
    print('Wynik działania wynosi: ', dzial_1(x1,x2))
else:
    print("Coś poszło nie tak.")