
def wspak(str):
  return str[::-1]

def czy_wspak(x = (str(input("Wskaz słowo do testu: ")))):
    if wspak(x) == x:
        return print('\nWskazane słowo to palindrom')
    else:
        return print('\nWskazane słowo nie jest palindromem')

czy_wspak()