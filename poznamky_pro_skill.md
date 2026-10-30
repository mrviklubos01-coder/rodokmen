# Poznámky pro správce skillu „rodokmen“

Sem Claude průběžně zapisuje, co by se mělo ve skillu zlepšit: chyby nástrojů, nové archivy a postupy, nápady.
Jen technické věci, žádné údaje o rodině. Nic se neposílá automaticky – když budete chtít, Claude poznámky vypíše
a vy je zkopírujete do e-mailu na sarsonj@gmail.com. Klidně připište i vlastní zkušenosti – užitečné změny autor rád
zapracuje do skillu, aby je měli i ostatní. Děkujeme!


- Cloudové prostředí (claude.ai/code): výchozí síťová politika blokuje archivní portály (portafontium.eu, aron.vychodoceskearchivy.cz,
  slovakiana.sk, familysearch.org – proxy vrací 403 na CONNECT). Skill by mohl ve Fázi 0 v cloudu hned ověřit dostupnost portálů
  a poradit uživateli přidat domény do „Allowed domains“ v nastavení prostředí.
- Past: osoby v `P` nejsou v souboru seřazené podle čísla (nové se přidávají kam se hodí). Úprava „vyříznout od `N: dict(` po `M: dict(`“
  skriptem omylem smazala osoby mezi nimi. Pomohl by nástroj `osoba.py <číslo> <vstup>` (jako zapis.py) pro změnu jedné osoby.
