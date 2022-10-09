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
import time
import random

def get_series():
    time.sleep(1)
    print('Wczytywanie danych.')
    time.sleep(2)
    print('Wczytywanie zakończone.')
    time.sleep(2)
    print('W bibliotece dostepne sa nastepujace pozycje:\n')
    time.sleep(2)
    for x in Lista:
        try:
            print('Tytul: %s, Rok %s, Sezon %s, Odcinek %s' % (x.title,x.year,x.se_number,x.ep_number))
        except AttributeError:
            continue
def get_movies():
    time.sleep(1)
    print('Wczytywanie danych.')
    time.sleep(2)
    print('Wczytywanie zakończone.')
    time.sleep(2)
    print('W bibliotece dostepne sa nastepujace pozycje:\n')
    time.sleep(2)
    for x in Lista:
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
def top_views():
    top_view = (0)
    for x in Lista:
        if top_view < Lista[x].views:
            top_view = Lista[x].views

time.sleep(1)
print('|. Wczytywanie modułu.. 1/3...........|')
time.sleep(2)
print('|. Wczytywanie modułu.. 2/3...........|')
time.sleep(2)
print('|. Wczytywanie modułu.. 3/3...........|')
time.sleep(2)
print("|. Moduł wczytano: Biblioteka filmów..| \nVAULT TEC Inc \nRok dystrybucji 2152")
time.sleep(1)
print()
print(
    ' ______ Dostępne funkcje programu_________\n',
    '|. 1. Pobranie bazy filmów - get_movies()\n',
    '|. 2. Pobranie bazy seriali - get_series()\n',
    '|. 3. Wyszukanie po tytule filmu - search()\n',
    '|. 4. Wylosowanie 1 tytulu z losową ogladalnoscią - generate_views()\n',
    '|. 5. Wylosowanie 10 tytulow z losową ogladalnoscią filmu - generate_views10()\n'
    ' |. 6. Wskazanie tytulu z najwyzsza ogladalnoscia - top_views()\n')
n = int(input())
if n == 1:
    get_movies()
elif n == 2:
    get_series()
elif n == 3:
    search(input())
elif n == 4:
    generate_views()
elif n == 5:
    generate_views10()