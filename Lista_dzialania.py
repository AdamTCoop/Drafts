
zbior_liczb = []
ilosc_liczb = ()
print("Aktualny zbiór liczb: ",zbior_liczb)
while True:
    try:
        ilosc_liczb = int(input('Ile liczb będzie w zbiorze?'))
    except ValueError:
        print('Możesz wprowadzić tylko wartości liczbowe. Spróbuj jeszcze raz.')
        continue
    else:
        break
for i in range(ilosc_liczb):
    while True:
        try:
            zbior_liczb.append(int(input("Wprowadz liczbę:\n")))
        except ValueError:
            print('Możesz wprowadzić tylko wartości liczbowe. Spróbuj jeszcze raz.')
            continue
        else:
            break
print("Aktualny zbiór zawiera: ",zbior_liczb,"Co zamierzasz z nimi zrobić?\n 1. Dodać \n 2. Pomnożyć")
wybor = 0
sum1 = 1
while True:
    try:
        wybor = int(input('Wybierz działanie: \n'))
    except ValueError:
        print('Możesz wprowadzić tylko wartości liczbowe: 1 lub 2. Spróbuj ponownie.')
        continue
    if wybor > 2 or wybor < 1:
        print('Możesz wprowadzić tylko wartości liczbowe: 1 lub 2. Spróbuj ponownie.')
        continue
    else:
        break
if wybor == 1:
    print('Suma liczb w zbiorze wynosi: ',sum(zbior_liczb))
elif wybor == 2:
    for i in zbior_liczb:
        sum1 *= i
    print(f"Wynik mnozenia: {sum1}")
