
models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

# wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}

for i in zip(models,sales2018,sales2017,sales2016):

  brand,model = i[0].split(" - ")
  brand_models = cars.setdefault(brand,{})
  brand_model_sales = brand_models.setdefault(model,{})
  brand_model_sales["sales"] = {"2016": 0 if i[3] == "NA" else int(i[3].replace(',',"")),
                                "2017": 0 if i[2] == "NA" else int(i[2].replace(',',"")),
                                "2018": 0 if i[1] == "NA" else int(i[1].replace(',',""))}

##ZAPOŻYCZONE Z YOUTUBE:
def dict_walk(d):
    for k, v in d.items():
        if type(v)==dict:
            print(k)
            dict_walk(v)
        else:
            print(k, ':', v)

dict_walk(cars )

top_2017_sales = ("",0)
for brand in cars.keys():
    for model in cars[brand].keys():
        sales = cars[brand][model]['sales']['2017']
    if sales > top_2017_sales[1]:
        top_2017_sales = (model,sales)
answer1 = top_2017_sales[0]
print('\nAnswer1, czyli który model sprzedawał się najlepiej w 2017:',answer1)

top_2018_brand = ("",0)
for brand in cars.keys():
    brand_sales = 0
for model in cars[brand].keys():
    model_sales = cars[brand][model]['sales']['2018']
    brand_sales += model_sales
if brand_sales > top_2018_brand[1]:
    top_2018_brand = (brand,brand_sales)
answer2 = top_2018_brand[0]
print('\nAnswer2, czyli która marka sprzedawała się najlepiej w 2018:',answer2)

for brand in cars.keys():
  for model in cars[brand].keys():
    sales = cars[brand][model]['sales']
    if sales['2016'] == 0 and sales['2017'] > 0:
      answer3.append(model)
print('\nAnswer3, czyli których modeli nie było w 2016 a pojawiły się w 2017:',answer3)


min_model_sales = ("",100000000000000)
for brand in cars.keys():
  for model in cars[brand].keys():
    model_sales = sum(cars[brand][model]['sales'].values())
    if model_sales < min_model_sales[1]:
      min_model_sales = (model,model_sales)
answer4 = min_model_sales[0]
print('\nAnswer4, czyli który model sprzedawał się najgorzej ze wszystkich latach:',answer4)

sales17 = 0
sales18 = 0
for sales in cars['Ford'].values():
  sales17 += sales['sales']['2017']
  sales18 += sales['sales']['2018']
answer5 = "{0:.0%}".format(sales18 / sales17 - 1)
print('\nAnswer5, czyli wzrost sprzedaży Forda w latach 2017 - 2018:',answer5)

answer1 = '" '# wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'





"""

panowie = ['Bednarz - Adam','Bednarz - Leszek','Ciba - Tomasz','Ciba - Dariusz']
auta93 = ['13','45','21','NA']
auta94 = ['45','23','NA','87']
auta95 = ['23','NA','88','54']

auta_all = zip(panowie,auta93,auta94,auta95)
sprzedawcy = {}

for i in (auta_all):
    nazwisko,imie = i[0].split(' - ')
    nazwiska = sprzedawcy.setdefault(nazwisko,{})
    imiona = nazwiska.setdefault(imie,{})
    imiona["Sprzedaż"] = {
        '93': 0 if i[1] == "NA" else int(i[1].replace(',',"")),
        '94': 0 if i[2] == "NA" else int(i[2].replace(',',"")),
        '95': 0 if i[3] == "NA" else int(i[3].replace(',',""))
    }


top_1993_sales = ("",0)
for nazwiska in sprzedawcy.keys():
    for imiona in sprzedawcy[nazwiska].keys():
        sprzedaz = sprzedawcy[nazwiska][imiona]['Sprzedaż']['93']
        if sprzedaz > top_1993_sales[1]:
            top_1993_sales = (imiona,sprzedaz)

print(sprzedawcy)


test = ('Adam - Bednarz')
print(test)
imie,nazwisko = test.split(' - ')
print(imie)
print(nazwisko)

"""