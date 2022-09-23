print()
print('-- Rozw 1 --')
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
print('-- Rozw 2 --')
print()
lz = next(iter(lista_zakupow.keys()))
lzz = next(iter(lista_zakupow.keys()))
lz2 = next(iter(lista_zakupow.values()))
lz22 = next(iter(lista_zakupow.values()))

print('Poszedłem do sklepu typu',lz.capitalize(),'i kupiłem sobie przedmiot typu:',[item.capitalize() for item in lz2])
print('Poszedłem do sklepu typu',lz.capitalize(),'i kupiłem sobie przedmiot typu:',[item.capitalize() for item in lz2])
