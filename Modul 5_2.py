
class Book:
    def __init__ (self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email

    @property
    def contact(self):
        print('Kontaktuje sie z %s %s %s' % (self.name, self.last_name, self.email), end = ' ')
        print('[Dlugosc znakow:',len(('Kontaktuje sie z %s %s %s' % (self.name, self.last_name, self.email))),']')

Lp1 = Book(name = 'Jan',last_name='Kowalski',email='abednarz@gmail.com')
Lp2 = Book(name = 'Adam',last_name='Nowak',email='anowak@gmail.com')
Lp3 = Book(name = 'Wojciech',last_name='Kowal', email='wkowal@gmail.com')
Lp4 = Book(name = 'Yan',last_name='Fasola',email='yfasola@gmail.com')

kontakty = (Lp1,Lp2,Lp3,Lp4)
print()
for x in kontakty:
    x.contact
