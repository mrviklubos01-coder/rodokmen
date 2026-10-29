# Přímí předci podle Kekulého čísel: 1 = výchozí osoba (ten, pro koho rodokmen děláme),
# otec osoby n má číslo 2n, matka 2n+1. Tedy 2 = otec, 3 = matka, 4–7 prarodiče, 8–15 pradědečci a prababičky…
#
# Každá osoba:  číslo: dict(n="Jméno Příjmení", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    jméno; ženy rodným příjmením („Anna Dvořáková“), u nejistého čtení otazník („Marie Špalková (?)“)
#   y    roky života pro přehledy: "* 1931" (žije / úmrtí neznámé), "1850–1910", "asi 1720–1785", "1680 – před 1740"
#   st   stav doložení:  doc  = doloženo matrikou (čteno přímo ze snímku)
#                        prob = pravděpodobné (shoda údajů, ale ne přímý doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = jen z cizího rodokmenu na internetu (MyHeritage, Geni…) – neověřeno
#                        unk  = neznámé (jen místo v rodokmenu)
#   f    fakta jako krátké věty: "* 12. 3. 1873 Hořice čp. 477", "kovář", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narození, × sňatek, † úmrtí – podle těchto značek web pozná sňatky a místa pro mapu)
#   r    klíče zápisů z data/zaznamy.json, které osobu dokládají
#   note poznámka: proč je údaj nejistý, rozpory, odkud se vzal
#   sex  jen u osoby 1: "M" nebo "F" (u ostatních plyne z čísla)
# Žijící lidé: jen jméno a rok narození (soukromí), note="Žijící – údaje jen základní."
# Neznámý otec nemanželského dítěte: dict(n="otec neuveden", st="unk", f=[], note="…")

P = {
    1: dict(n="Luboš Mrvík", y="* 1977", st="fam", sex="M", f=["* 1977 Planá (okr. Tachov)"],
            note="Žijící – údaje jen základní."),
    2: dict(n="Jan Mrvík", y="* 1948", st="fam", f=["* 1948 Bor (okr. Tachov)"],
            note="Otec výchozí osoby. Údaje od rodiny (uživatel, 29. 10. 2026). Zda žije – zatím nezjištěno; do té doby jen základní údaje."),
    3: dict(n="Marie Křivancová", y="* 1948", st="fam", f=["* 1948", "žila v Damnově (okr. Tachov)"],
            note="Matka výchozí osoby, provdaná Mrvíková. Údaje od rodiny (uživatel, 29. 10. 2026). Místo narození neznámé. Zda žije – zatím nezjištěno."),
    4: dict(n="Josef Mrvík", y="1910–1976", st="doc", f=["* 13. 3. 1910 Koupě čp. 51 (fara Bělčice)", "otec domkář", "žil v Boru a na Nové Hospodě (okr. Tachov)", "† 30. 6. 1976", "pohřben v Boru (okr. Tachov)"],
            r=["belcice_index_josef_mrvik_1910"],
            note="Otec Jana Mrvíka (2). Narození doloženo rejstříkem narozených fary Bělčice (datum souhlasí s údajem rodiny); samotná kniha narozených po 1903 zatím není online, jména rodičů proto zatím neznámá. Úmrtí a hrob od rodiny. Nejdřív uveden jako „Jan“, pak opraven na Josef."),
    5: dict(n="Anna Kicková", y="1912–2002", st="fam", f=["* 24. 9. 1912 Lehôtka pod Brehmi (Slovensko)", "žila v Boru a na Nové Hospodě (okr. Tachov)", "† 25. 2. 2002 Bechlín (okr. Litoměřice)", "pohřbena v Bechlíně u Roudnice nad Labem"],
            note="Matka Jana Mrvíka (2), provdaná Mrvíková. Od rodiny (uživatel, 29. 10. 2026). Zemřela u příbuzných Snopových v Bechlíně."),
    6: dict(n="Josef Křivanec", y="asi 1920–1980", st="fam", f=["* asi 1920", "† 1980", "pohřben v Damnově (okr. Tachov)"],
            note="Otec Marie Křivancové (3). Od rodiny (uživatel, 29. 10. 2026); roky a místa zatím neznámé."),
    7: dict(n="Marie Jačková", y="", st="fam", f=[],
            note="Matka Marie Křivancové (3), provdaná Křivancová. Od rodiny (uživatel, 29. 10. 2026); roky a místa zatím neznámé."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=4, n="Marie Mrvíková (* 1909)", t="Narozena 8. 3. 1909 v Koupi č. 51, otec domkář – stejný dům jako Josef (1910), nejspíš jeho starší sestra (neověřeno, rodiče zatím neznámí).", r=["belcice_index_josef_mrvik_1910"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kde se narodil Josef Mrvík (1910)?", "Vyřešeno: Koupě čp. 51, fara Bělčice (rejstřík narozených). Celý zápis s rodiči je v knize narozených, která zatím není online."),
    ("Kdo byli rodiče Josefa Mrvíka (1910)?", "Otevřené: kniha narozených Bělčice po 1903 není online; hledat sňatek rodičů (Bělčice, oddaní 1897–1949) a starší Mrvíky z Podruhlí."),
    ("Jak byli příbuzní Snopovi z Bechlína?", "Otevřené: babička Anna u nich zemřela (2002); vztah k rodině zatím neznámý."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
