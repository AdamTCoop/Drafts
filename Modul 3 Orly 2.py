import time
time.sleep(2)
most = int(input('Wskaż docelową długość mostu:'))
plyta = int(input('Wskaż długość płyty:'))

print('Dlugosc mostu ma wynieść:', most)
print('Dlugosc plyty do wykorzystania wynosi: ',plyta)
lacznik = plyta / 2
print('Dlugosc łącznika wynosi:', lacznik)
ilosc_plyt = (most + lacznik) // (plyta + lacznik)
print('Ilosc niezbednych płyt wyniesie:',ilosc_plyt)
ilosc_lacznikow = ilosc_plyt - 1
print('Ilosc potrzebnych łączników wyniesie:',ilosc_lacznikow)
mozliwy_most = (ilosc_plyt * plyta) + (ilosc_lacznikow * lacznik)
print('Most możliwy do wybudowania taką ilościa materiałów wyniesie:',mozliwy_most)
if mozliwy_most == most:
    time.sleep(2)
    print('Budujemy!')
else:
    time.sleep(2)
    print('Nie budujemy')

def build_bridge(most,plyta):
    lacznik = plyta / 2
    ilosc_plyt = (most + lacznik) // (plyta + lacznik)
    ilosc_lacznikow = ilosc_plyt - 1
    moscik = (ilosc_plyt * plyta) + (ilosc_lacznikow * lacznik)
    if moscik == most:
        time.sleep(2)
        return True
        time.sleep(2)
    else:
        time.sleep(2)
        return False
        time.sleep(2)

print()
time.sleep(2)
print(build_bridge((int(input('Wskaż docelową długość mostu:'))),(int(input('Wskaż długość płyty:')))))
