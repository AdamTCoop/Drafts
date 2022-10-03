import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
def licz(x1,*args):
    if n == 6:
        return x1 * x1
    elif n == 5:
        import math
        return math.sqrt(x1)
    if n == 4:
        return x1 / x2
    elif n == 3:
        return x1 * x2
    elif n == 2:
        return x1 - x2
    elif n == 1:
        return x1 + x2
    else:
        return print("Coś poszło nie tak.")
if __name__ == "__main__":
    print()
    print("Kalkulator")
    logging.info("Kalkulator")
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
    while True:
        try:
            n = int(input('Jakie działanie zamierzasz przeprowadzic? Wskaż numer: '))
        except ValueError:
            print('Możesz wprowadzić tylko wartości liczbowe od 1 do 6. Spróbuj jeszcze raz.')
            continue
        if n < 0 or n > 6:
            print('Możesz wprowadzić tylko wartości liczbowe od 1 do 6. Spróbuj jeszcze raz.')
            continue
        else:
            break
    print('Zdecydowałeś się na:',n)
    logging.info('Zdecydowałeś się na: %s' %n)
    wynik = 0
    if n >= 5:
        print('Wskaż liczbę do obliczenia. Wybór potwierdź klawiszem enter: ', end=' ')
        while True:
            try:
                x1 = float(input())
            except ValueError:
                print('Możesz wprowadzić tylko wartości liczbowe')
                continue
            else:
                break
        print('Wskazales liczbe:', x1)
        logging.info('Wskazales liczbe:' %n)
        print()
        print('Wynik działania wynosi: ', licz(x1))
        wynik = (licz(x1))
    else:
        print('Wskaż dwie liczby do obliczeń. Wprowadź pierwszą liczbę i potwierdź klawiszem enter: ', end = ' ')
        while True:
            try:
                x1 = float(input())
            except ValueError:
                print('Możesz wprowadzić tylko wartości liczbowe')
                continue
            else:
                break
        print('Wskazales liczbe:', x1,' Liczba numer dwa, to:')
        logging.info('Wskazales liczbe:%s Liczba numer dwa, to:' %x1)
        while True:
            try:
                x2 = float(input())
            except ValueError:
                print('Możesz wprowadzić tylko wartości liczbowe')
                continue
            else:
                break
        print('Wskazales liczby',x1,' i ',x2)
        print()
        print('Wynik działania wynosi: ', licz(x1,x2))
        wynik = licz(x1,x2)
    print('W zaokragleniu: ',(round(wynik,2)))