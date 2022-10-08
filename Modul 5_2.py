
class BaseContact:
    def __init__ (self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    @property
    def contact(self):
        wiz = ('Wybieram numer +48 %s i dzwonię do %s %s' % (self.phone, self.name, self.last_name))
        print(wiz)

    @property
    def label_length(self):
        wiz = ('%s %s' % (self.name, self.last_name))
        print('[ Ilosc znakow:', len(wiz), ']\n')

class BusinessContact(BaseContact):
   def __init__(self,position, company_name, company_number , *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.position = position
       self.company_name = company_name
       self.company_number = company_number

   @property
   def contact(self):
       wiz = ('Wybieram numer +48 %s i dzwonię do %s %s, %s z firmy %s' % (self.company_number, self.name, self.last_name, self.position, self.company_name))
       print(wiz)

   @property
   def label_length(self):
       wiz = ('%s %s' % (self.name, self.last_name))
       print('[ Ilosc znakow:', len(wiz), ']\n')


Lp1 = BaseContact(name = 'Jan',last_name='Kowalski',phone='111111111',email='abednarz@gmail.com')
Lp2 = BaseContact(name = 'Adam',last_name='Nowak',phone='222222222',email='anowak@gmail.com')
Lp3 = BaseContact(name = 'Wojciech',last_name='Kowal',phone='333333333', email='wkowal@gmail.com')
Lp4 = BaseContact(name = 'Yan',last_name='Fasola',phone='444444444',email='yfasola@gmail.com')
Lp5 = BusinessContact(name = 'Krzysztof',last_name='Hefajstos',phone='123123123',email='bigcompany@gmail.com',position='President',company_name='Żabka',company_number='555555555')
Lp6 = BusinessContact(name = 'Maciej',last_name='Zaraz',phone='345345345',email='greatcompany@gmail.com',position='Vice-president',company_name='Yahoo',company_number='666666666')
Lp7 = BusinessContact(name = 'Zbyszek',last_name='Czwartek',phone='678678678', email='smallcompany@gmail.com',position='Smuggler',company_name='Google',company_number='777777777')
Lp8 = BusinessContact(name = 'Omikron',last_name='Stół',phone='912912912',email='notcompany@gmail.com',position='Thief',company_name='Facebook',company_number='888888888')

kontakty = (Lp1,Lp2,Lp3,Lp4,Lp5,Lp6,Lp7,Lp8)
print()
for x in kontakty:
    x.contact, x.label_length
