most = int(input('Wskaż docelową długość mostu:'))
plyta = int(input('Wskaż długość płyty:'))
print()
print('Dlugosc mostu ma wynieść:', most)
print('Dlugosc plyty do wykorzystania wynosi: ',plyta)
print()
lacznik = plyta / 2
print('Dlugosc łącznika wynosi:', lacznik)
ilosc_plyt = (most + lacznik) // (plyta + lacznik)
print('Ilosc niezbednych płyt wyniesie:',ilosc_plyt)
ilosc_lacznikow = ilosc_plyt - 1
print('Ilosc potrzebnych łączników wyniesie:',ilosc_lacznikow)
mozliwy_most = (ilosc_plyt * plyta) + (ilosc_lacznikow * lacznik)
print('Most możliwy do wybudowania taką ilościa materiałów wyniesie:',mozliwy_most)
print()
if mozliwy_most == most:
    print('Budujemy!')
else:
    print('Nie budujemy')
