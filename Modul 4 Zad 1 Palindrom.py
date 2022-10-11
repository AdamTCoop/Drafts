
def wspak(str):
  return str[::-1]

def czy_wspak(x = (str(input("1. Wskaz słowo do testu: ")))):
    if wspak(x) == x:
        return print('\n1. Odp: Wskazane słowo to palindrom')
    else:
        return print('\n2. Odp: Wskazane słowo nie jest palindromem')

czy_wspak()
print()

def odwroc(str):
  return str[::-1]

def czypalindrom(x = (str(input("3. Wskaz słowo do testu: ")))):
    if odwroc(x) == x:
        return True
    else:
        return False
print()
print(czypalindrom())