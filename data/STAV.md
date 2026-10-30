# Stav rodokmenu a pravidla práce

Tento soubor je vstupní bod. Po každém restartu (nová konverzace, zkrácený kontext) ho Claude čte jako první,
pak konec `research_log.md` a sekci „Rozpracováno“.

## Pro koho
- Výchozí osoba: Luboš Mrvík, * 1977 Planá (okr. Tachov); dříve Bor u Tachova, nyní Damnov.
- Kdo s Claudem pracuje a jak chce komunikovat: sám Luboš; česky, stručně; chce doptávání a poctivě říct, co chybí.

## Kde co je
| Soubor | Obsah |
|---|---|
| `data/osoby.py` | Přímí předci podle Kekulého čísla + rody, boční příbuzní, otevřené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (klíč = název obrázku). |
| `data/svazky.json` | Matriční svazky (archiv, signatura, odkaz). |
| `data/prepisy.json` | Přepis originálu a český překlad každého zápisu. |
| `data/zvyrazneni.json` | Rámečky – které místo výřezu čteme. |
| `data/research_log.md` | Deník VŠECH hledání, i neúspěšných. |
| `data/udaje_od_rodiny.md` | Co řekla rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Co by šlo zjistit jen v archivu. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavení webu. |
| `vyrezy/`, `zdroje/` | Výřezy zápisů pro web (1800 px) a v plném rozlišení. |
| `dokumenty/` | Rodinné dokumenty a fotky od uživatele (originály). |
| `pracovni/` | Pracovní soubory (stažené stránky, kontrolní obrázky) – nejdou na web. |
| `web/` | Rodinný web. `cd web && npm run data && npm run build`, náhled `npm run preview`. |

## Pravidla
1. Než něco ohlásím jako nové, prohledám `osoby.py`, `zaznamy.json` a `research_log.md` (jméno, místo, rok).
2. Údaj je „doloženo“ (doc) jen tehdy, když jsem ho přečetl přímo na snímku. Čtení od pomocníků ověřím sám.
3. Každé hledání (i neúspěšné) zapíšu do `research_log.md`.
4. Nejistá čtení označím (?) – nic nedomýšlím.
5. Ke každému novému zápisu: výřez (`tools/vyrez.py`), rámeček (`tools/ramecek.py`) a přepis s překladem.
6. Po změně dat spustím `python3 -I tools/kontrola.py`.

## Rozpracováno (aktualizovat průběžně)
- **Plán uživatele (29. 10. 2026):** nejdřív dohledat otcův rodokmen (Mrvíkové – Jakub z Uzenic a starší; Hupákovi z Hošovic), příběh rodu až později. Další na řadě (upřesněno 30. 10. 2026): slovenská větev babičky z otcovy strany Anny Kickové (* 24. 9. 1912 Lehôtka pod Brehmi). Matčina linie (Křivancová) až po dokončení otcova rodokmenu.
- Fáze 1: od rodiny chybí údaje o babičce Marii Jačkové (7) a narození Josefa Křivance (6, asi 1920).
- Fáze 2, větev Mrvíkové (fary Bělčice a Černívsko, SOA Třeboň, `trebon.py`; Uzenice, Chobot, Hošovice = fara Černívsko): doloženo Josef (4) * 1910 Koupě 51 (rejstřík), sňatek rodičů (pravděp.) Václav Mrvík × Marie Hupáková 1908, křest Václava 1884. Další kroky – konec `research_log.md`.
- Hupákovi: doloženo Marie Hupáková * 1885, sňatek rodičů 1880, křest matky Marie Vavříkové 1856 (otec kovář František Vavřík, Újezdec 36). Další krok: sňatek Josefa Tintěry s Annou Kozlovou (nevlastní otec).
- Mrvíkové: sňatek Václava (32) × Marie Pirhanzlové nenalezen (asi 1848–49) – Bělčice 1840–72 ne, Černívsko oddíl Chobot nenalezen. Jakub (64) z Uzenic zatím nehledán.
- Slovenská větev: Anna Kicková * 24. 9. 1912 Lehôtka pod Brehmi (okr. Žiar nad Hronom, dříve Tekovská stolice) – zatím nehledáno. Uživatel má účet na FamilySearch (29. 10. 2026); snímky otevírá on a posílá snímky obrazovky – Claude se za něj nepřihlašuje. Farnost Lehôtky neověřena (sousední farnost Brehy – jen hypotéza).
- Síť: uživatel povolil plný přístup k internetu (29. 10. 2026); Porta fontium přes curl hlásila chybu – ověřit nástrojem.
