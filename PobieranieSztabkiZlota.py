import requests
from bs4 import BeautifulSoup
url = "https://mennica.apart.pl/produkt/c-hafner-sztabka-5-g-24h/30"
'''
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

ceny = soup.find_all("span", class_="value")
cena_sztabki = ceny[8].text.strip()

print(f"Aktualna cena sztabki 5g: {cena_sztabki} PLN")
'''
'''
# Pobieramy kod HTML strony
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# Pobieramy wszystkie elementy z klasą "value"
ceny = soup.find_all("span", class_="value")

# Wypisujemy znalezione ceny, żeby zobaczyć, które są na stronie
for idx, cena in enumerate(ceny, 1):
    print(f"Cena {idx}: {cena.text.strip()} PLN")
'''
headers = {"User-Agent": "Mozilla/5.0"}  # Niektóre strony wymagają user-agenta
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Znalezienie sekcji produktu
# produkt = soup.find("div", class_="product-single__info")
hidden_input = soup.find("input", {"type": "hidden", "name": "name"})
hidden_input2 = soup.find("input", {"type": "hidden", "name": "price"})

if hidden_input:
    print(hidden_input["value"])
    print(hidden_input2["value"])

if hidden_input2:
    cena_element = hidden_input2["value"]
    if cena_element:
        # cena = cena_element.text.strip()
        print(f"Aktualna cena sztabki 5g: {cena_element}")
    else:
        print("Nie znaleziono ceny!")
else:
    print("Nie znaleziono produktu!")

# if produkt:
#     cena_element = produkt.find("span", class_="value")
#     if cena_element:
#         cena = cena_element.text.strip()
#         print(f"Aktualna cena sztabki 5g: {cena}")
#     else:
#         print("Nie znaleziono ceny!")
# else:
#     print("Nie znaleziono produktu!")
