# Cvičení č. 8 - Datové struktury

* Na vlastním GitHub účtu vytvoř kopii (**fork**) zdrojového repozitáře. 
Otevři v prohlížeči adresu zdrojového repozitáře. Vpravo nahoře najdi tlačítko <kbd>Fork</kbd> a klikni na něj.
* Naklonuj si repozitář ze **svého GitHub účtu** do složky s dnešním cvičením.
* V lokálním repozitáři nastav pomocí terminálu novou vzdálenou adresu (**remote**) na **původní** (slytherins-hub) adresu repozitáře (trojúhelníková spolupráce):
  ```commandline
  git remote add upstream <repository_address>
  ```
* V lokálním repozitáři vytvoř novou větev (**branch**) s názvem `criminals` a do této větve se přepni pomocí příkazu:
  ```commandline
  git checkout <branch_name>
  ```

## Narcos
* Vytvoř nový skript `criminals.py` a v něm hlavní funkci `main()`, do ní zkopíruj následující řádky:
  ```python
  names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
  production = [(138, 164, 151), (125, 113, 113), (52, 50, 63)]
  most_wanted = dict(zip(names, production))
  ```
* V hlavní funkci proveď načtení dat ze souboru `new_criminals.json`, přiřaď je do proměnné `new_criminals` a ověř,
v jaké datové struktuře se data načetla.
* Vytvoř funkci `criminals()`, která bude mít dva vstupní parametry: současný slovník zločinců - `most_wanted` 
a bude nový slovník zločinců - `new_criminals`.
* Ve funkci zkontroluj, jestli se některý z nových zločinců již nachází ve slovníku `most_wanted`.
* Pokud ano, proveď ve slovníku `most_wanted` aktualizaci hodnot produkce drog pro daného zločince. 
Pokud ne, přidej daného zločince do slovníku `most_wanted` včetně jeho hodnot produkce.
* Volání funkce a korektnost její implementace ověřte voláním z hlavní funkce `main()`.
* Vytvoř novou revizi (**commit**) a změny nahrajte na svůj vzdálený repozitář (**push**).


* Hlavní funkci rozšiř o slovník `origin`, do kterého jsme uložili množiny všech hledaných osob dle země jejich původu 
(volba je zcela fiktivní):
  ```python
  origin = {
     "Mexico": {"Manuel Noriega", "Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"},
     "Columbia": {"Rick Ross", "William Jardine"},
  }
  ```
* Vytvoř funkci `get_production()`, která pro zadaný stát vrátí celkovou produkci syntetických drog za poslední tři roky. 

* Vstupním parametrem funkce bude kromě názvu státu také slovník `origin` a `most_wanted`. 
  Pro řešení využijte hodnoty ve slovníku `origin` jako klíče pro vyhledávání ve slovníku `most_wanted`. 
  Volání funkce a její výstup pak může vypadat např. takto:
  ```commandline
  >>> get_production("Columbia", origin, most_wanted)
  >>> 70
  ```
* Volání funkce a korektnost její implementace ověřte voláním z hlavní funkce `main()`.
* Vytvoř novou revizi (commit) a změny nahrajte na svůj vzdálený repozitář (push).
* Přepni se na hlavní větev a změny z nové větve začleň do větve hlavní.

## Sudoku
Implementujte algoritmus pro kontrolu správně vyplněného řádku sudoku.
* V lokálním repozitáři se přepni na hlavní větvi `main` a  vytvoř novou větev s názvem `sudoku` a do této větve se přepni.
* V modulu `sudoku.py` vytvoř funkci `is_correct()`. Funkce bude mít jeden vstupní parametr – seznam s devíti prvky (čísly).
* Výstupním parametrem bude logická hodnota `True`, pokud je řádek sudoku správně vyplněn.
* Na funkci jsou kladeny následující požadavky:
  * Seznam projde kontrolou, pokud bude obsahovat čísla 1 až 9 a každé z nich právě jednou.
  * Kontrola bude provedena pomocí množin a metod nad množinou.
* Volání funkce a korektnost její implementace ověř voláním hlavní funkce `main()`. 
* Vytvoř novou revizi (commit). Přepni se na hlavní větev a změny z nové větve začleň do větve hlavní. Změny nahrajte na svůj vzdálený repozitář (push).

