class Movies:
    def __init__(self, title, year, type, lenght):
        self.title = title
        self.year = year
        self.type = type
        self.lenght = lenght
        self.views = 0
    def __str__(self):
        return f'{self.title} {self.year} {self.type}'
    def play(self):
        print('Ogladasz wlasnie: %s z roku %s. Dotychczas ten film obejrzano %s razy.' % (self.title,self.year,self.views))
        self.views += 1
    def show(self):
        print('Wylosowano film: %s z roku %s. Dotychczas ten film obejrzano %s razy.' % (self.title,self.year,self.views))
class Series(Movies):
   def __init__(self, ep_number, se_number, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.ep_number = ep_number
       self.se_number = se_number
       self.views = 0
   def play(self):
       print('Ogladasz wlasnie: %s z roku %s S%sE%s. Dotychczas ten odcinek obejrzano %i razy.' % (self.title,self.year,self.se_number,self.ep_number,self.views))
       self.views += 1
   def show(self):
       print('Wylosowano film: %s z roku %s. Dotychczas ten film obejrzano %s razy.' % (self.title,self.year,self.views))

Lista = [
Movies(title = 'Tie Me Up! Tie Me Down!', year = '1990',type = 'Comedy',lenght='M'),
Movies(title = 'High Heels', year = '1991',type = 'Comedy',lenght='M'),
Movies(title = 'Dead Zone  The', year = '1983',type = 'Horror',lenght='M'),
Movies(title = 'Cuba', year = '1979',type = 'Action',lenght='M'),
Movies(title = 'Days of Heaven', year = '1978',type = 'Drama',lenght='M'),
Movies(title = 'Octopussy', year = '1983',type = 'Action',lenght='M'),
Movies(title = 'Target Eagle', year = '1984',type = 'Action',lenght='M'),
Movies(title = 'American Angels: Baptism of Blood  The', year = '1989',type = 'Drama',lenght='M'),
Movies(title = 'Subway', year = '1985',type = 'Drama',lenght='M'),
Movies(title = 'Camille Claudel', year = '1990',type = 'Drama',lenght='M'),
Movies(title = 'Fanny and Alexander', year = '1982',type = 'Drama',lenght='M'),
Movies(title = 'Tragedy of a Ridiculous Man', year = '1982',type = 'Drama',lenght='M'),
Movies(title = 'A Man & a Woman', year = '1966',type = 'Drama',lenght='M'),
Movies(title = 'A Man & a Woman: Twenty Years Later', year = '1986',type = 'Drama',lenght='M'),
Movies(title = 'Blackmail', year = '1929',type = 'Mystery',lenght='M'),
Movies(title = 'Donovan s Reef', year = '1963',type = 'Comedy',lenght='M'),
Movies(title = 'Tucker: The Man & His Dream', year = '1988',type = 'Drama',lenght='M'),
Movies(title = 'Scrooged', year = '1988',type = 'Comedy',lenght='M'),
Movies(title = 'Running Man  The', year = '1987',type = 'Science Fiction',lenght='M'),
Movies(title = 'Raiders of the Lost Ark', year = '1981',type = 'Action',lenght='M'),
Movies(title = 'Predator 2', year = '1991',type = 'Action',lenght='M'),
Movies(title = 'Colors', year = '1988',type = 'Drama',lenght='M'),
Movies(title = 'Un Hombre y una Mujer', year = '1966',type = 'Drama',lenght='M'),
Movies(title = 'Official Story  The', year = '1985',type = 'Drama',lenght='M'),
Series(title = 'Gra o Tron', year = '2012',type = 'Fantasy',se_number = '01', ep_number = '02',lenght='S'),
Series(title = 'Gra o Tron', year = '2012',type = 'Fantasy',se_number = '01', ep_number = '03',lenght='S'),
Series(title = 'Gra o Tron', year = '2012',type = 'Fantasy',se_number = '02', ep_number = '01',lenght='S'),
Series(title = 'Gra o Tron', year = '2012',type = 'Fantasy',se_number = '02', ep_number = '02',lenght='S'),
Series(title = 'Gra o Tron', year = '2012',type = 'Fantasy',se_number = '02', ep_number = '03',lenght='S'),
Series(title = 'Gra o Tron', year = '2012',type = 'Fantasy',se_number = '03', ep_number = '01',lenght='S'),
Series(title = 'Gra o Tron', year = '2012',type = 'Fantasy',se_number = '03', ep_number = '02',lenght='S'),
Series(title = 'Gra o Tron', year = '2012',type = 'Fantasy',se_number = '03', ep_number = '03',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '01', ep_number = '01',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '01', ep_number = '02',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '01', ep_number = '03',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '02', ep_number = '01',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '02', ep_number = '02',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '02', ep_number = '03',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '03', ep_number = '01',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '03', ep_number = '02',lenght='S'),
Series(title = 'Rodzina Soprano', year = '2000',type = 'Drama',se_number = '03', ep_number = '03',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '01', ep_number = '01',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '01', ep_number = '02',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '01', ep_number = '03',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '02', ep_number = '01',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '02', ep_number = '02',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '02', ep_number = '03',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '03', ep_number = '01',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '03', ep_number = '02',lenght='S'),
Series(title = 'The Office', year = '2010',type = 'Comedy',se_number = '03', ep_number = '03',lenght='S'),
]

Lista_alfa = sorted(Lista, key=lambda self: self.title)
Lista_year = sorted(Lista, key=lambda self: self.year)
import time
import random
import datetime
def get_series():
    for x in Lista_alfa:
        try:
            print('Tytul: %s, Rok %s, Sezon %s, Odcinek %s' % (x.title,x.year,x.se_number,x.ep_number))
        except AttributeError:
            continue
def get_movies():
    for x in Lista_year:
        if x.lenght == 'M':
            print('Tytul: %s, Rok %s' % (x.title,x.year))
def search(value):
   for x in Lista:
       if x.title == value:
           print(x.title,x.year)
           break
def generate_views():
    x = random.randrange(10)
    Lista[x].views = random.randrange(1,100)
    (Lista[x].show())
def generate_views10():
    for x in range(10):
        x = random.randrange(10)
        Lista[x].views = random.randrange(1, 100)
        (Lista[x].show())
def top_titles():
    top_view = 1
    top_view2 = 1
    top_view3 = 1
    top_title = ()
    top_title2 = ()
    top_title3 = ()
    for x in Lista:
        cur_view = x.views
        if top_view < cur_view:
            top_view = cur_view
            top_title = x.title
    for x in Lista:
        cur_view = x.views
        if top_view2 < cur_view < top_view:
            top_view2 = cur_view
            top_title2 = x.title
    for x in Lista:
        cur_view = x.views
        if top_view3 < cur_view < top_view2:
            top_view3 = cur_view
            top_title3 = x.title
    return print('\n1. %s, z iloścą wyświeteń: %s. \n2. %s, z ilością wyświetleń %s. \n3. %s, z ilością wyświetleń z %s' % (top_title,top_view, top_title2,top_view2, top_title3,top_view3))

def dodaj_1():
        Lista_alfa.append(Series(title=(input('Wprowadz tytul filmu:')), year=(input('Wprowadz rok produkcji filmu:')), type=(input('Wprowadz gatunek filmu:')), se_number=(input('Wprowadz sezon filmu:')), ep_number=(input('Wprowadz numer odcinka:')), lenght=(input('Wprowadz typ filmu (M-Movie,S-Series'))))


def dodaj_few():
    ile = int(input('Ile odcinków danego serialu chcesz dodać?'))
    in_tytul = (input('Wprowadz tytul filmu:'))
    in_rok = (input('Wprowadz rok filmu:'))
    in_kat = (input('Wprowadz kategorie filmu:'))
    in_sezon = (input('Wprowadz sezon filmu:'))
    for x in range(ile):
        y = x+1
        Lista_alfa.append(Series(title = (in_tytul), year=(in_rok), type=(in_kat), se_number=(in_sezon), ep_number=(y), lenght=('S')))
    get_series()

while True:
    try:
        print()
        print(
            ' |______ Dostępne funkcje programu______________________|\n',
            '|. 1. Pobranie bazy filmów - get_movies()______________|\n',
            '|. 2. Pobranie bazy serialów - get_series()____________|\n',
            '|. 3. Wyszukanie po tytule filmu - search()____________|\n',
            '|. 4. Pobranie 1 tytulu - generate_views()_____________|\n',
            '|. 5. Pobranie 10 tytulow - generate_views10()_________|\n',
            '|. 6. Lokalny BoxOffice - top_views()__________________|\n'
            ' |. 7. Chcesz dodać seriale? Śmiało!____________________|\n'
            ' |------------------------------------------------------|')
        n = int(input('\nWprowadź numer polecenia jakie ma zostać wykonane:\n'))
    except ValueError:
        print('Możesz wprowadzić tylko wartości liczbowe od 1 do 6. Spróbuj jeszcze raz.')
        continue
    if n < 1 or n > 8:
        print('Możesz wprowadzić tylko wartości liczbowe od 1 do 6. Spróbuj jeszcze raz.')
        continue
    elif n == 1:
        get_movies()
        continue
    elif n == 2:
        get_series()
        continue
    elif n == 3:
        search(input())
        continue
    elif n == 4:
        generate_views()
        continue
    elif n == 5:
        generate_views10()
        continue
    elif n == 6:
        top_titles()
        continue
    elif n == 7:
        dodaj_few()
        continue
    else:
        break
