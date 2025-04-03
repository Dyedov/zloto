import requests
# print(requests.__version__)
from bs4 import BeautifulSoup

mapowanie_sztabek = {
    '1g':'1',
    '1':'1',
    '2g':'2',
    '2':'2',
    '5g':'5',
    '5':'5',
    '10g':'10',
    '10':'10',
    '20g':'20',
    '20':'20',
    '25g':'25',
    '25':'25',
    '50g':'50',
    '50':'50',
    '100g':'100',
    '100':'100'
}

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

sztabka_gramy = ['1','1g','2','2g','5','5g','10','10g','20','20g','25','25g','1oz','50','50g','100','100g']

while True:
    try:
        while True:
            try:
                kwotaInwestycji = int(input('Jaką kwotę chcesz zainwestować. Podaj w PLN: '))
                break
            except ValueError:
                print('To nie jest liczba! Podaj poprawną kwotę.')

        print('Możesz zainwestować w sztabki złota: 1g, 2g, 5g, 10g, 20g, 25g, 1oz, 50g, 100g')
        sztabka = input('Podaj gramaturę: ').strip().lower()
        sztabka = mapowanie_sztabek.get(sztabka, sztabka)

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
            cena_sztabki = float(input_price["value"])
            print(f"Aktualna cena sztabki {producent_sztabki} {sztabka}g: {cena_sztabki}")

            liczba_sztabek = int(kwotaInwestycji//cena_sztabki)
            reszta = kwotaInwestycji - liczba_sztabek * cena_sztabki
            reszta_zaokraglona = round(reszta,2)
            print(f'Możesz zainwestować w {liczba_sztabek} sztabkę po {sztabka}g.')

            inwestycja = liczba_sztabek * cena_sztabki
            inwestycja_zaokraglona = round(inwestycja,2)
            print(f'Twoja inwestycja wyniesie {inwestycja_zaokraglona} PLN,'
                  f'\nco pozwoli Ci kupić {liczba_sztabek} sztabek złota.')
            print(f'Reszta {reszta_zaokraglona} PLN')

        inflacja = 5/100
        inflacja_zloto = round(kwotaInwestycji * (1 + inflacja ) ** 10, 2)
        inflacja_pln = round(kwotaInwestycji / (1 + inflacja ) ** 10, 2)

        print(f'Za 10 lat Twoja inwestycja w złoto może być warta: '
              f'\n{inflacja_zloto:,.2f} PLN'.replace(',',' '))
        print(f'Przewidywana siła nabywcza Twoich pieniędzy za 10 lat wyniesie: '
              f'\n{inflacja_pln:,.2f} PLN'.replace(',',' '))

        response_NBP = requests.get('https://api.nbp.pl/api/cenyzlota/')

        if response_NBP.status_code == 200:
            dane = response_NBP.json()
            cena_zlota = dane[0]['cena']
            print(f'Aktualna cena złota wyliczona w NBP: {cena_zlota} PLN za gram')
        else:
            print(f'Błąd! Kod odpowiedzi: {response_NBP.status_code}')

        # print(response_NBP.text)

        def pobieranie_ceny(url):
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                input_price = soup.find('input', {'type': 'hidden', 'name': 'price'})

                if input_price:
                    return float(input_price['value'])
                else:
                    return None
            else:
                return None

        # url_testowy = urls['5']
        # print(pobieranie_ceny(url_testowy))

        ceny_sztabek = {}

        for gramatura, url in urls.items():
            ceny_sztabek[gramatura] = pobieranie_ceny(url)

        # print(ceny_sztabek)

        gramatury = []
        for g in ceny_sztabek:
            if g != '1oz':
                gramatury.append(int(g))
            else:
                gramatury.append(31.1)

        gramatury_max_value = sorted(gramatury, reverse=True)
        gramatury_max_pieces = sorted([g for g in gramatury if g >= 5 and g != 31.1], reverse=True)

        sztabki_max_value = {}
        kwota_temp = kwotaInwestycji

        for gramatura in gramatury_max_value:
            klucz = '1oz' if gramatura == 31.1 else str(gramatura)
            cena = ceny_sztabek[klucz]
            if cena <= kwota_temp:
                liczba_sztuk = int(kwota_temp // cena)
                sztabki_max_value[gramatura] = liczba_sztuk
                kwota_temp -= liczba_sztuk * cena

        sztabki_max_pieces = {}
        kwota_temp2 = kwotaInwestycji

        for gramatura in gramatury_max_pieces:
            klucz = '1oz' if gramatura == 31.1 else str(gramatura)
            cena = ceny_sztabek[klucz]

            print(f'DEBUG: gramatura {gramatura}, cena {cena}, kwota przed: {kwota_temp2}')

            if cena <= kwota_temp2:
                liczba_sztuk = int(kwota_temp2 // cena)
                sztabki_max_pieces[gramatura] = liczba_sztuk
                kwota_temp2 -= liczba_sztuk * cena

            print(f'DEBUG: Kupiono {liczba_sztuk}, sztuk, pozostała kłota: {kwota_temp2}')

        print('\n Strategia "Największa wartość":')
        for gramatura, liczba_sztuk in sztabki_max_value.items():
            print(f'{liczba_sztuk} sztuk sztabki o gramaturze {gramatura}g')
        print(f'Pozostała kwota: {kwota_temp:,.2f} PLN')

        print('\n Strategia "Najwięcej sztuk - zaczynamy od 5g":')
        for gramatura, liczba_sztuk in sztabki_max_pieces.items():
            print(f'{liczba_sztuk} sztuk sztabki o gramaturze {gramatura}g')
        print(f'Pozostała kwota: {kwota_temp2:,.2f} PLN')

        print("gramatury_max_value:", gramatury_max_value)
        print("gramatury_max_pieces:", gramatury_max_pieces)


        break

    except ValueError as e:
        print(e)
