# Symulator Inwestycji w Złoto z uwzględnieniem inflacji (CPI)

Ten program pozwala użytkownikowi zasymulować inwestycję w fizyczne złoto (sztabki) i ocenić, jak może ona wyglądać w przyszłości, biorąc pod uwagę inflację (CPI). Wszystkie dane dotyczą inwestycji w złoto wyceniane w polskich złotych (PLN), z uwzględnieniem aktualnych wskaźników inflacji w Polsce.

---

## Funkcje programu

- Pobieranie na bieżąco aktualnych cen złota (dane pobierane są z internetu przy każdym uruchomieniu programu, bez ręcznego wpisywania).
- Pobieranie aktualnego wskaźnika inflacji CPI (z oficjalnej strony NBP).
- Dwie strategie inwestycyjne:
  - "Najwięcej sztuk – zaczynamy od sztabki 5g"
  - "Największa wartość – zaczynamy od największych gramatur"
- Obliczenie przyszłej wartości inwestycji w złoto.
- Porównanie tej wartości z przewidywaną siłą nabywczą pieniędzy (uwzględniając inflację).

---

## Wymagania

- Python 3.9+
- Biblioteki:
  - `requests`
  - `beautifulsoup4`
  - `lxml`

Zainstaluj je za pomocą:
```bash
pip install -r requirements.txt
```

---

## Jak uruchomić

1. Uruchom program:
```bash
python main.py
```

2. Postępuj zgodnie z instrukcjami w terminalu:

### Przykład działania:

```
Jaką kwotę chcesz zainwestować. Podaj w PLN: 10000
Możesz zainwestować w sztabki złota: 1g, 2g, 5g, 10g, 20g, 25g, 1oz, 50g, 100g
Podaj gramaturę: 5
- Podsumowując -
Chcesz zainwestować: 10000 PLN w sztabkę złota o wadze 5g
Aktualna cena sztabki C-Hafner 5g: 2012.0
Możesz zainwestować w 4 sztabkę po 5g.
Twoja inwestycja wyniesie 8048.0 PLN,
co pozwoli Ci kupić 4 sztabek złota.
Reszta 1952.0 PLN
Wartość inflacji CPI: 4.9%
Za 10 lat Twoja inwestycja w złoto może być warta:
16 134.48 PLN
Przewidywana siła nabywcza Twoich pieniędzy za 10 lat wyniesie:
6 197.91 PLN
Aktualna cena złota wyliczona w NBP: 378.97 PLN za gram

 Strategia "Największa wartość":
1 sztuk sztabki o gramaturze 25g
Pozostała kwota: 256.00 PLN

 Strategia "Najwięcej sztuk - zaczynamy od 5g":
4 sztuk sztabki o gramaturze 5g
2 sztuk sztabki o gramaturze 2g
Pozostała kwota: 306.00 PLN
```

---

## Autor
Projekt hobbystyczny do nauki Pythona oraz analizy inwestycji w fizyczne złoto, skoncentrowany na rynku polskim. Program jest w fazie rozwoju i nie jest jeszcze ostatecznie ukończony, a jego funkcjonalności są na bieżąco rozbudowywane.

---

## Planowane funkcje w przyszłości

- Ulepszenie wyglądu konsoli (czytelniejsze kolory, formatowanie).
- Automatyczny wybór najlepiej opłacalnej strategii.
- Eksport raportu do pliku (np. CSV lub PDF).
- Wybór różnych mennic i ich porównanie.
- Historia cen złota.
- Możliwość inwestycji cyklicznych (np. co miesiąc).
- Możliwość wyboru kilku gramatur sztabek złota, a nie tylko jednej.
- Obliczenia dla różnych okresów (np. 3, 5, 10, 15, 30 lat), a nie tylko dla 10 lat.
- Rozszerzenie obliczeń o inwestycje w monety złote.

---

## Licencja
MIT License

