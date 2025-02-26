import requests
# print(requests.__version__)
from bs4 import BeautifulSoup

kwotaInwestycji = input('Jaką kwotę chcesz zainwestować. Podaj w PLN: ')
print('Możesz zainwestować w sztabki złota: 1g, 2g, 5g, 10g, 20g, 25g, 1oz, 50g, 100g')
sztabka = input('Dokonaj wyboru: ')
'''
sztabka_gramy = ['1','2','5','10','20','25','1oz','50','100']

while sztabka in sztabka_gramy:
    print(f'{sztabka} nie ma na liście, wpisz wartość z listy')
else:
    print(f'- Podsumowując - \nChcesz zainwestować: {kwotaInwestycji} PLN w sztabkę złota o wadze {sztabka}g')
'''
url1 = "https://mennica.apart.pl/produkt/c-hafner-sztabka-1-g-24h/28"
url2 = "https://mennica.apart.pl/produkt/c-hafner-sztabka-2-g-24h/29"
url5 = "https://mennica.apart.pl/produkt/c-hafner-sztabka-5-g-24h/30"
url10 = "https://mennica.apart.pl/produkt/c-hafner-sztabka-10-g-24h/31"
url20 = "https://mennica.apart.pl/produkt/c-hafner-sztabka-20-g-24h/32"
url25 = "https://mennica.apart.pl/produkt/c-hafner-sztabka-25-g-24h/193"
url1oz = "https://mennica.apart.pl/produkt/c-hafner-sztabka-1-oz-24h/33"
url50 = "https://mennica.apart.pl/produkt/c-hafner-sztabka-50-g-24h/34"
url100 = "https://mennica.apart.pl/produkt/c-hafner-sztabka-100-g-24h/35"

headers = {"User-Agent": "Mozilla/5.0"}
if sztabka == '1oz':
    response = requests.get(url1oz, headers=headers)
elif int(sztabka) == 1:
    response = requests.get(url1, headers=headers)
elif int(sztabka) == 2:
    response = requests.get(url2, headers=headers)
elif int(sztabka) == 5:
    response = requests.get(url5, headers=headers)
elif int(sztabka) == 10:
    response = requests.get(url10, headers=headers)
elif int(sztabka) == 20:
    response = requests.get(url20, headers=headers)
elif int(sztabka) == 25:
    response = requests.get(url25, headers=headers)
elif int(sztabka) == 50:
    response = requests.get(url50, headers=headers)
elif int(sztabka) == 100:
    response = requests.get(url100, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
input_name = soup.find("input", {"type": "hidden", "name": "name"})
input_price = soup.find("input", {"type": "hidden", "name": "price"})

producent_sztabki = input_name["value"][:8]

if input_price:
    cena_element = input_price["value"]
    if cena_element:
        print(f"Aktualna cena sztabki {producent_sztabki} {sztabka}g: {cena_element}")











'''
url = "https://mennica.apart.pl/produkt/c-hafner-sztabka-5-g-24h/30"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

cena_element = soup.find("span", class_="value")
if cena_element:
    cena = cena_element.text.strip()
    print(f'Aktualna cena sztabki 5g: {cena}')
else:
    print('Nie udało się znaleźć ceny.')
'''
# url = "https://mennica.apart.pl/produkt/c-hafner-sztabka-5-g-24h/30"
#
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(response.text, "html.parser")
#
# ceny = soup.find_all("span", class_="value")
# cena_sztabki = ceny[8].text.strip()
#
# print(f"Aktualna cena sztabki 5g: {cena_sztabki} PLN")

# for idx, cena in enumerate(ceny, 1):
#     print(f"Cena {idx}: {cena.text.strip()} PLN")
