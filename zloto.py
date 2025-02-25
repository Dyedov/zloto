import requests
# print(requests.__version__)
from bs4 import BeautifulSoup

kwotaInwestycji = input('Jaką kwotę chcesz zainwestować. Podaj w PLN: ')
print('Możesz zainwestować w sztabki złota: 0.5g, 1g, 5g, 10g, 20g')
sztabka = input('Dokonaj wyboru: ')
print(f'- Podsumowując - \nChcesz zainwestować: {kwotaInwestycji} PLN w sztabkę złota o wadze {sztabka}g')

url = "https://mennica.apart.pl/produkt/c-hafner-sztabka-5-g-24h/30"

headers = {"User-Agent": "Mozilla/5.0"}  # Niektóre strony wymagają user-agenta
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

hidden_input = soup.find("input", {"type": "hidden", "name": "name"})
hidden_input2 = soup.find("input", {"type": "hidden", "name": "price"})

# if hidden_input:
#     print(hidden_input["value"])
#     print(hidden_input2["value"])

if hidden_input2:
    cena_element = hidden_input2["value"]
    if cena_element:
        # cena = cena_element.text.strip()
        print(f"Aktualna cena sztabki 5g: {cena_element}")






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
