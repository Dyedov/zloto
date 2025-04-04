import requests
from bs4 import BeautifulSoup

def pobieranie_inflacje_CPI():
    url = 'https://www.nbp.pl/statystyka-i-sprawozdawczosc/inflacja/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    resource = requests.get(url, headers=headers)

    if resource.status_code == 200:
        soup = BeautifulSoup(resource.text, 'html.parser')

        wiersze = soup.find_all('tr', class_='table-last-row')

        for wiersz in wiersze:
            komorki = wiersz.find_all('td')
            if len(komorki) >= 2 and komorki[0].text.strip() == '02-2025':
                cpi_value = komorki[1].text.strip().replace(',','.')
                return float(cpi_value) / 100

    return 0.05

inflacja_cpi = pobieranie_inflacje_CPI()
print(f'Wartość inflacji CPI: {inflacja_cpi * 100}%')


