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
    8: dict(n="Václav Mrvík", y="* 1884", st="prob", f=["* 29. 8. 1884 Podruhlí čp. 27 (fara Bělčice)", "× 4. 2. 1908 Bělčice, Marie Hupáková", "bydlel v Koupi čp. 51"],
            r=["belcice_krest_vaclav_mrvik_1884", "belcice_snatek_vaclav_mrvik_1908", "belcice_index_josef_mrvik_1910"],
            note="Křest a sňatek doloženy matrikou. Že je otcem Josefa (4), je pravděpodobné, ne přímo doložené: novomanželé bydleli v Koupi čp. 51 a tam se 1909 narodila Marie a 1910 Josef Mrvík, otec domkář (rejstřík narozených). Jméno otce v rejstříku není; kniha narozených po 1903 zatím není online."),
    9: dict(n="Marie Hupáková", y="* 1885", st="prob", f=["* 6. 8. 1885 Hošovice čp. 16 (fara Černívsko)", "× 4. 2. 1908 Bělčice, Václav Mrvík", "bydlela v Koupi čp. 51"],
            r=["cernivsko_krest_marie_hupakova_1885", "belcice_snatek_vaclav_mrvik_1908"],
            note="Křest a sňatek doloženy matrikou; matkou Josefa (4) pravděpodobně – viz Václav (8). Hošovice = na portálu archivu „Hostišovice“, fara Černívsko (odtud i křestní list ze sňatku 1908)."),
    16: dict(n="Václav Mrvík", y="* 1854", st="prob", f=["* 26. 1. 1854 Podruhlí čp. 12", "záložník c. k. 18. praporu myslivců (1883)", "× 9. 10. 1883 Bělčice, Barbora Křížová roz. Lokajová, vdova", "domkář v Podruhlí čp. 27", "1908 souhlasil se sňatkem nezletilého syna a podepsal se"],
             r=["belcice_krest_vaclav_mrvik_1854", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884", "belcice_snatek_vaclav_mrvik_1908"],
             note="Otec Václava (8) podle zápisu o křtu 1884 i o sňatku 1908; vlastní křest 1854 nalezen. Spojení s rodokmenem pravděpodobné (viz 8)."),
    17: dict(n="Barbora Lokajová", y="* 1845", st="prob", f=["* 27. 10. 1845 Ostrov čp. 4 (okr. Březnice)", "1. manžel Antonín Kříž, domkář v Podruhlí čp. 27", "× 9. 10. 1883 Bělčice, Václav Mrvík"],
             r=["belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884", "belcice_snatek_vaclav_mrvik_1908"],
             note="Matka Václava (8). Při druhém sňatku 1883 jí bylo 38 let, o devět let víc než ženichovi. Dům čp. 27 v Podruhlí byl jejího prvního manžela. Číslo domu v Ostrově: 1883 a 1884 „č. 4“, 1908 „č. 1“ (?)."),
    18: dict(n="Václav Hupák", y="* asi 1854", st="prob", f=["* asi 1854", "záložník c. k. 1. pluku zákopníků (1880)", "domkář v Hošovicích čp. 16", "× 21. 9. 1880 Bělčice, Marie Vavříková z Újezdce"],
             r=["belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885", "belcice_snatek_vaclav_mrvik_1908"],
             note="Otec Marie (9); sňatek doložen matrikou. Spojení s rodokmenem pravděpodobné (viz 8)."),
    19: dict(n="Marie Vavříková", y="* asi 1856", st="prob", f=["* asi 1856", "bydlela v Újezdci čp. 36", "× 21. 9. 1880 Bělčice, Václav Hupák"],
             r=["belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885", "belcice_snatek_vaclav_mrvik_1908"],
             note="Při sňatku 1880 dcera Františka Vavříka, kováře v Újezdci čp. 36, a Anny roz. Kozlové. Při křtu dcery 1885 a sňatku dcery 1908 ale uvedena jako dcera (rodem) Tintěrová, dcera Josefa Tintěry z Koupě čp. 51 a Anny roz. Kozlové. Matka sedí, otec ne – viz ISSUES."),
    32: dict(n="Václav Mrvík", y="", st="prob", f=["domkář v Podruhlí čp. 12"], r=["belcice_krest_vaclav_mrvik_1854", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884"],
             note="Dědeček Václava (8) podle zápisu o křtu 1884; spojení s rodokmenem pravděpodobné (viz 8)."),
    33: dict(n="Marie Pirhanzlová", y="", st="prob", f=["z Chobota (okr. Blatná)"], r=["belcice_krest_vaclav_mrvik_1854", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884"],
             note="Babička Václava (8) podle zápisu o křtu 1884 („rodem Pirhanzl z Chobota“); spojení s rodokmenem pravděpodobné (viz 8)."),
    34: dict(n="Václav Lokaj", y="", st="prob", f=["chalupník v Ostrově čp. 4 (okr. Březnice)"], r=["belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884"],
             note="Otec Barbory (17) podle zápisu o křtu 1884; spojení s rodokmenem pravděpodobné (viz 8)."),
    35: dict(n="Anna Suchá (?)", y="", st="prob", f=["z Paračova (okr. Blatná)"], r=["belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884"],
             note="Matka Barbory (17). Příjmení čteno nejistě: sňatek 1883 „rod. Suchý“, křest 1884 spíš „Sedlý“; spojení s rodokmenem pravděpodobné (viz 8)."),
    36: dict(n="Martin Hupák", y="", st="prob", f=["domkář v Hošovicích čp. 16"], r=["cernivsko_krest_marie_hupakova_1885"],
             note="Otec Václava Hupáka (18) podle zápisu o křtu vnučky 1885; spojení s rodokmenem pravděpodobné (viz 8)."),
    37: dict(n="Barbora Kočovská (?)", y="", st="prob", f=["z Hošovic čp. 22"], r=["belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885"],
             note="Matka Václava Hupáka (18). Sňatek 1880: „rodem Kočovské z Hošovic č. 22“; křest 1885: příjmení písař přeškrtl a opravil (čteno jako Hošovská?). Čtení nejisté."),
    38: dict(n="František Vavřík", y="", st="prob", f=["kovář v Újezdci čp. 36"], r=["belcice_snatek_vaclav_hupak_1880"],
             note="Otec Marie (19) podle zápisu o jejím sňatku 1880. Pozdější zápisy (1885, 1908) uvádějí jako otce Josefa Tintěru – viz ISSUES a SIDE."),
    39: dict(n="Anna Kozlová", y="", st="prob", f=["z Koupě čp. 3 (1880) / čp. 51 (1885)"], r=["belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885"],
             note="Matka Marie (19) – souhlasně v zápisu o sňatku 1880 i o křtu vnučky 1885. Možná se po Vavříkovi znovu vdala za Josefa Tintěru (hypotéza)."),
    64: dict(n="Jakub Mrvík", y="", st="prob", f=["tesař v Uzenicích čp. 1"], r=["belcice_krest_vaclav_mrvik_1854"],
             note="Otec Václava (32) podle zápisu o křtu vnuka 1854; spojení s rodokmenem pravděpodobné (viz 8)."),
    65: dict(n="Dorota Labská", y="", st="prob", f=["z Koupě"], r=["belcice_krest_vaclav_mrvik_1854"],
             note="Manželka Jakuba (64) podle zápisu o křtu vnuka 1854; spojení s rodokmenem pravděpodobné (viz 8)."),
    66: dict(n="Matěj Pirhansl", y="", st="prob", f=["krejčí v Chobotě (okr. Blatná)"], r=["belcice_krest_vaclav_mrvik_1854"],
             note="Otec Marie (33) podle zápisu o křtu vnuka 1854; spojení s rodokmenem pravděpodobné (viz 8)."),
    67: dict(n="Kateřina Kaprová (?)", y="", st="prob", f=["z Dobšic"], r=["belcice_krest_vaclav_mrvik_1854"],
             note="Manželka Matěje (66) podle zápisu o křtu vnuka 1854; příjmení čteno nejistě; spojení s rodokmenem pravděpodobné (viz 8)."),
}

# Rody = osm větví podle pradědečků a prababiček (čísla 8–15). Doplňte, jakmile je znáte:
# 8: ("Novákové", "Jedna věta, kdo to byli a odkud – ukáže se na webu u rodu."),
LINES = {
    8: ("Mrvíkové", "Domkáři z Podruhlí a Koupě na Blatensku (fara Bělčice); Josef Mrvík (1910) odešel po válce na Tachovsko."),
    9: ("Hupákovi", "Domkáři z Hošovic čp. 16 (fara Černívsko); Marie Hupáková (1885) se vdala do Koupě čp. 51, domu Josefa Tintěry."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=19, n="Josef Tintěra", t="Domkář v Koupi čp. 51. Při křtu Marie Hupákové 1885 zapsán jako otec její matky a zároveň byl kmotrem; sňatek 1880 ale uvádí jako otce nevěsty Františka Vavříka, kováře z Újezdce. Hypotéza: nevlastní otec (druhý manžel Anny Kozlové). Do jeho domu čp. 51 se Mrvíkovi po svatbě 1908 nastěhovali.", r=["cernivsko_krest_marie_hupakova_1885"]),
    dict(k=16, n="František Mrvík", t="Domkář v Podruhlí čp. 7, syn Václava Mrvíka z čp. 12 a Marie Pirhanzlové – tedy nejspíš bratr Václava (16). Jeho syn Josef se narodil 2. 4. 1884 (zápis na stejné stránce jako Václav, čteno z náhledu). František Mrvík, domkář v Podruhlí, byl 1908 svědkem na svatbě Václava (8).", r=["belcice_krest_vaclav_mrvik_1884"]),
    dict(k=4, n="Marie Mrvíková (* 1909)", t="Narozena 8. 3. 1909 v Koupi č. 51, otec domkář – stejný dům jako Josef (1910), rok po svatbě Václava Mrvíka a Marie Hupákové; nejspíš Josefova starší sestra.", r=["belcice_index_josef_mrvik_1910"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kdo byl otcem Marie, provdané Hupákové (* asi 1856)?", "Otevřené: sňatek 1880 – František Vavřík, kovář z Újezdce; křest dcery 1885 a sňatek dcery 1908 – Josef Tintěra z Koupě čp. 51. Matka v obou Anna Kozlová. Hypotéza: Josef Tintěra byl nevlastní otec. Ověřit křtem Marie (asi 1856) a sňatkem Anny Kozlové s Tintěrou."),
    ("Kde se narodil Josef Mrvík (1910)?", "Vyřešeno: Koupě čp. 51, fara Bělčice (rejstřík narozených). Celý zápis s rodiči je v knize narozených, která zatím není online."),
    ("Kdo byli rodiče Josefa Mrvíka (1910)?", "Hypotéza: Václav Mrvík a Marie Hupáková, oddaní 4. 2. 1908, bydleli v Koupi čp. 51, kde se Josef narodil. Potvrdí to zápis o křtu (kniha narozených Bělčice po 1903, zatím není online) nebo úmrtní list Josefa (1976)."),
    ("Jak byli příbuzní Snopovi z Bechlína?", "Otevřené: babička Anna u nich zemřela (2002); vztah k rodině zatím neznámý."),
]

# Hypotézy o původu rodu nad rámec doložené linie (zobrazí se na stránce rodu):
# dict(rod=8, nadpis="Hypotéza: Novákové z Lhoty", text="…", polozky=[("Jan Novák", "kmotr 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Předek v rodokmenu vícekrát (příbuzní rodiče): {alias: hlavní číslo}, např. {350: 140}
SAME = {}
