import requests
# print(requests.__version__)
from bs4 import BeautifulSoup

urls = {
    '1':'https://mennica.apart.pl/produkt/c-hafner-sztabka-1-g-24h/28',
    '2':'https://mennica.apart.pl/produkt/c-hafner-sztabka-2-g-24h/29',
    '5':'https://mennica.apart.pl/produkt/c-hafner-sztabka-5-g-24h/30',
    '10':'https://mennica.apart.pl/produkt/c-hafner-sztabka-10-g-24h/31',
    '20':'https://mennica.apart.pl/produkt/c-hafner-sztabka-20-g-24h/32',
    '25':'https://mennica.apart.pl/produkt/c-hafner-sztabka-25-g-24h/193',
    '1oz':'https://mennica.apart.pl/produkt/c-hafner-sztabka-1-oz-24h/33',
    '50':'https://mennica.apart.pl/produkt/c-hafner-sztabka-50-g-24h/34',
    '100':'https://mennica.apart.pl/produkt/c-hafner-sztabka-100-g-24h/35'
}

sztabka_gramy = ['1','2','5','10','20','25','1oz','50','100']

while True:
    try:
        kwotaInwestycji = input('Jaką kwotę chcesz zainwestować. Podaj w PLN: ')
        print('Możesz zainwestować w sztabki złota: 1g, 2g, 5g, 10g, 20g, 25g, 1oz, 50g, 100g')
        sztabka = input('Dokonaj wyboru: ')

        if sztabka not in sztabka_gramy:
            raise ValueError('Błędna wartość! Wybierz jedną z dostępnych gramatur na liście.')

        print(f'- Podsumowując - \nChcesz zainwestować: {kwotaInwestycji} PLN w sztabkę złota o wadze {sztabka}g')

        url = urls[sztabka]
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")
        input_name = soup.find("input", {"type": "hidden", "name": "name"})
        input_price = soup.find("input", {"type": "hidden", "name": "price"})

        if input_name and input_price:
            producent_sztabki = input_name["value"][:8]
            cena_element = input_price["value"]
            print(f"Aktualna cena sztabki {producent_sztabki} {sztabka}g: {cena_element}")

        break

    except ValueError as e:
        print(e)