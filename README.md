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

1. Dla osób, które chcą przetestować program bez instalowania Pythona – przygotowana została wersja `.exe`, dostępna w repozytorium.

⚠️ **Uwaga**: Ze względu na to, że plik `.exe` nie pochodzi z oficjalnego sklepu (np. Microsoft Store), niektóre programy antywirusowe mogą go oznaczyć jako **potencjalnie niebezpieczny plik**.  
Jeśli ufasz autorowi i źródłu (czyli temu repozytorium), możesz go bezpiecznie uruchomić.

2. Uruchom program:
```bash
python zloto.py
```

2. Postępuj zgodnie z instrukcjami w terminalu:

### Przykład działania:

```
==================================================
           SYMULATOR INWESTYCJI W ZŁOTO
==================================================

Jaką kwotę chcesz zainwestować. Podaj w PLN: 10000
Możesz zainwestować w sztabki złota: 1g, 2g, 5g, 10g, 20g, 25g, 1oz, 50g, 100g
Podaj gramaturę: 1

--------------------------------------------------
🔎 PODSUMOWANIE INWESTYCJI
--------------------------------------------------
Chcesz zainwestować: 10000 PLN w sztabkę złota o wadze 1g
Aktualna cena sztabki C-Hafner 1g: 439.0
Możesz zainwestować w 22 sztabkę po 1g.
Twoja inwestycja wyniesie 9658.0 PLN,
co pozwoli Ci kupić 22 sztabek złota.
Reszta 342.0 PLN

--------------------------------------------------
📈 Prognozy na 10 lat
--------------------------------------------------
Wartość inflacji CPI: 4.9%
Za 10 lat Twoja inwestycja w złoto może być warta:
16 134.48 PLN
Przewidywana siła nabywcza Twoich pieniędzy za 10 lat wyniesie:
6 197.91 PLN
Aktualna cena złota wyliczona w NBP: 390.43 PLN za gram

--------------------------------------------------
💡 Strategia: "Największa wartość"
--------------------------------------------------
1 sztuk sztabki o gramaturze 20g
2 sztuk sztabki o gramaturze 2g
Pozostała kwota: 269.00 PLN

--------------------------------------------------
💡 Strategia: "Najwięcej sztuk - zaczynamy od 5g"
--------------------------------------------------
4 sztuk sztabki o gramaturze 5g
1 sztuk sztabki o gramaturze 2g
1 sztuk sztabki o gramaturze 1g
Pozostała kwota: 404.00 PLN
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

