from faker import Faker
fake = Faker()

class BaseContact:
    def __init__ (self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    @property
    def contact(self):
        print('Wybieram numer +48', self.phone, 'i dzwonię do', self.first_name, self.last_name, end = ' ')
    @property
    def label_length(self):
        wynik = len(self.first_name) + len(self.last_name)
        print('[Ilosc znakow:',wynik,']')

class BusinessContact(BaseContact):
   def __init__(self, position, company_name, company_number , *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company_name = company_name
       self.company_number = company_number
   @property
   def contact(self):
       print('Wybieram numer +48', self.company_number, 'i dzwonię do', self.first_name, self.last_name, end=' ')
   @property
   def label_length(self):
       wynik = len(self.first_name) + len(self.last_name)
       print('[Ilosc znakow:', wynik, ']')

Lp1 = BaseContact(first_name = fake.first_name(),last_name = fake.last_name(),phone = fake.phone_number(),email = fake.email)
Lp2 = BaseContact(first_name = fake.first_name(),last_name = fake.last_name(),phone = fake.phone_number(),email = fake.email)
Lp3 = BaseContact(first_name = fake.first_name(),last_name = fake.last_name(),phone = fake.phone_number(),email = fake.email)
Lp4 = BaseContact(first_name = fake.first_name(),last_name = fake.last_name(),phone = fake.phone_number(),email = fake.email)
Lp5 = BusinessContact(first_name = fake.first_name(),last_name = fake.last_name(),phone = fake.phone_number(),email = fake.email(),position = 'President',company_name = 'Żabka',company_number = fake.phone_number())
Lp6 = BusinessContact(first_name = fake.first_name(),last_name = fake.last_name(),phone = fake.phone_number(),email = fake.email(),position = 'President',company_name = 'Żabka',company_number = fake.phone_number())
Lp7 = BusinessContact(first_name = fake.first_name(),last_name = fake.last_name(),phone = fake.phone_number(),email = fake.email(),position = 'President',company_name = 'Żabka',company_number = fake.phone_number())
Lp8 = BusinessContact(first_name = fake.first_name(),last_name = fake.last_name(),phone = fake.phone_number(),email = fake.email(),position = 'President',company_name = 'Żabka',company_number = fake.phone_number())

kontakty = (Lp1,Lp2,Lp3,Lp4,Lp5,Lp6,Lp7,Lp8)
print()
for x in kontakty:
    x.contact, x.label_length
