import requests
# print(requests.__version__)
from bs4 import BeautifulSoup

sztabka_gramy = ['1','2','5','10','20','25','1oz','50','100']

while True:
    try:
        kwotaInwestycji = input('Jaką kwotę chcesz zainwestować. Podaj w PLN: ')
        print('Możesz zainwestować w sztabki złota: 1g, 2g, 5g, 10g, 20g, 25g, 1oz, 50g, 100g')
        sztabka = input('Dokonaj wyboru: ')

        if sztabka not in sztabka_gramy:
            raise ValueError('Błędna wartość! Wybierz jedną z dostępnych gramatur na liście.')

        print(f'- Podsumowując - \nChcesz zainwestować: {kwotaInwestycji} PLN w sztabkę złota o wadze {sztabka}g')

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

        break
    except ValueError as e:
        print(e)

# print('---działa narazie---')