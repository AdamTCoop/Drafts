from faker import Faker
fake = Faker()

class BaseContact:
    def __init__ (self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    @property
    def contact(self):
        print('Wybieram numer +48 %s i dzwonię do %s %s' % (self.phone, self.name, self.last_name))

    @property
    def label_length(self):
        print(len(BaseContact.contact))

class BusinessContact(BaseContact):
   def __init__(self, position, company_name, company_number , *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company_name = company_name
       self.company_number = company_number

   @property
   def contact(self):
       print('Wybieram numer +48',self.company_number, 'i dzwonię do ', self.name, self.last_name)

       #print('Wybieram numer +48 %s i dzwonię do %s %s' % (self.company_number, self.name, self.last_name))

   def label_length(self):
       print(len(BusinessContact.contact))

Lp1 = BaseContact(name = fake.name,last_name = fake.last_name,phone= fake.phone_number,email=fake.email())
Lp2 = BaseContact(name = fake.name(),last_name = fake.last_name,phone= fake.phone_number,email=fake.email())
Lp3 = BaseContact(name = fake.name(),last_name = fake.last_name,phone= fake.phone_number, email=fake.email())
Lp4 = BaseContact(name = fake.name(),last_name = fake.last_name,phone= fake.phone_number,email=fake.email())
Lp5 = BusinessContact(name = fake.name(),last_name = fake.last_name,phone= fake.phone_number,email=fake.email(),position='President',company_name='Żabka',company_number= fake.phone_number)
Lp6 = BusinessContact(name = fake.name(),last_name = fake.last_name,phone= fake.phone_number,email=fake.email(),position='Vice-president',company_name='Yahoo',company_number= fake.phone_number)
Lp7 = BusinessContact(name = fake.name(),last_name = fake.last_name,phone= fake.phone_number, email=fake.email(),position='Smuggler',company_name='Google',company_number= fake.phone_number)
Lp8 = BusinessContact(name = fake.name(),last_name = fake.last_name,phone= fake.phone_number,email=fake.email(),position='Thief',company_name='Facebook',company_number= fake.phone_number)

kontakty = (Lp1,Lp2,Lp3,Lp4,Lp5,Lp6,Lp7,Lp8)
print()
for x in kontakty:
    x.contact