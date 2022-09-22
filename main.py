lista_zakupow = {
    'warzywniak':'marchew',
    'warzywniak':'seler',
    'warzywniak':'rukola',
    'piekarnia':'chleb',
    'piekarnia':'pączek',
    'piekarnia':'bułki'
    }

zak = dict(lista_zakupow)
lz = iter(lista_zakupow.keys())
lz2 = iter(lista_zakupow.values())
print(zak.items())


print('Poszedłem do sklepu typu',next(lz),'i kupiłem sobie przedmiot typu:',next(lz2))
print('Poszedłem do sklepu typu',next(lz),'i kupiłem sobie przedmiot typu:',next(lz2))