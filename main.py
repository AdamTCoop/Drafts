print()
print('-- Zadanie 1 Rozwiazanie 1 --')
print()
lista_zakupow = {
    'warzywniak':['marchew','seler','rukola'],
    'piekarnia':['chleb','pączek','bułki']
}
for sklep, towar in lista_zakupow.items():
    print('Poszedłem do sklepu typu',sklep.capitalize(),'i kupiłem sobie przedmiot typu:', end = ' ')
    for i in towar:
        print(i.capitalize(), end =' ')
    print()
print()
print('-- Zadanie 1 Rozwiazanie 2 --')
print()
lz = next(iter(lista_zakupow.keys()))
lzz = next(iter(lista_zakupow.keys()))
lz2 = next(iter(lista_zakupow.values()))
lz22 = next(iter(lista_zakupow.values()))
print('Poszedłem do sklepu typu',lz.capitalize(),'i kupiłem sobie przedmiot typu:',[item.capitalize() for item in lz2])
print('Poszedłem do sklepu typu',lz.capitalize(),'i kupiłem sobie przedmiot typu:',[item.capitalize() for item in lz2])
print()
print('-- Zadanie 2 Rozwiazanie 1 --')
print()
piatki = []
for x in range(0,101):
    if x % 5 == 0:
        piatki.append(x)
        print(x, end =' ')
print()
print()
print('-- Zadanie 3 Rozwiazanie 1 --')
piatki3 = []
for z in piatki:
    piatki3.append(z * z * z)
print()
print(piatki3)