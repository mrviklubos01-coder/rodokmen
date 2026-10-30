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
            note="Matka Jana Mrvíka (2), provdaná Mrvíková. Od rodiny (uživatel, 29. 10. 2026). Zemřela u příbuzných Snopových v Bechlíně. Rodná obec patřila k farnosti Horné Opatovce (maďarsky obec 1892–1913 Apáthegyalja)."),
    6: dict(n="Josef Křivanec", y="1917–1980", st="doc", f=["* 19. 11. 1917 Leskovice čp. 32 (okr. Strakonice, fara Radomyšl)", "majitel hospodářství v Damnově čp. 10 (1947)", "× 12. 4. 1947 Čížová, Marie Jačková", "† 1980", "pohřben v Damnově (okr. Tachov)"],
            r=["cizova_snatek_josef_krivanec_1947"],
            note="Otec Marie Křivancové (3). Narození a rodiče podle zápisu o sňatku 1947 (doloženo); úmrtí a hrob od rodiny. Rodina uvádí Petrovice (bydliště) – zápis uvádí narození v Leskovicích; obě obce patří k faře Radomyšl."),
    7: dict(n="Marie Jačková", y="1925–2005", st="doc", f=["* 29. 9. 1925 Brloh-Nedílná čp. 37 (okr. Písek, fara Čížová)", "× 12. 4. 1947 Čížová, Josef Křivanec", "† 10/2005"],
            r=["cizova_snatek_josef_krivanec_1947"],
            note="Matka Marie Křivancové (3). Narození a rodiče podle zápisu o sňatku 1947 (doloženo); úmrtí od rodiny."),
    12: dict(n="Josef Křivanec", y="* 1891", st="doc", f=["* 20. 2. 1891 Leskovice čp. 32 (fara Radomyšl)", "kovář v Leskovicích čp. 32 (1917)", "× 19. 2. 1917 Radomyšl, Anežka Lišková", "rolník v Damnově čp. 10 (1947)"], r=["radomysl_krest_josef_krivanec_1891", "radomysl_snatek_josef_krivanec_1917", "cizova_snatek_josef_krivanec_1947"],
             note="Otec Josefa Křivance (6). Křest 1891 doložen (s okrajovou poznámkou o sňatku 19. 2. 1917; v knize oddaných je řádek s rodiči překrytý). Kovářem byl i podle prvního (přeškrtnutého) zápisu 1947 – v Damnově se stal rolníkem."),
    13: dict(n="Anežka Lišková", y="* 1894", st="doc", f=["* 19. 5. 1894 Chrášťovice čp. 30 (fara Radomyšl)", "legitimována 1896 sňatkem rodičů", "× 19. 2. 1917 Radomyšl, Josef Křivanec"], r=["radomysl_krest_anezka_liskova_1894", "radomysl_snatek_josef_krivanec_1917", "cizova_snatek_josef_krivanec_1947"],
             note="Matka Josefa Křivance (6). Narodila se jako nemanželská dcera Anny Čapkové, později legitimována sňatkem rodičů (otec František Liška)."),
    26: dict(n="František Liška", y="* 1872", st="doc", f=["* 19. 5. 1872 Sedlice", "nádeník v Chrášťovicích čp. 37 (1894), čp. 68 (1917)", "× 24. 11. 1896 Radomyšl, Anna Čapková"], r=["radomysl_snatek_frantisek_liska_1896", "radomysl_krest_anezka_liskova_1894", "radomysl_snatek_josef_krivanec_1917"],
             note="Otec Anežky (13) – legitimoval ji dodatečně sňatkem s její matkou (zápis 1917)."),
    27: dict(n="Anna Čapková", y="", st="doc", f=["z Chrášťovic čp. 30", "× 24. 11. 1896 Radomyšl, František Liška"], r=["radomysl_snatek_frantisek_liska_1896", "radomysl_krest_anezka_liskova_1894", "radomysl_snatek_josef_krivanec_1917"],
             note="Matka Anežky (13) podle zápisu o sňatku 1917."),
    14: dict(n="Jan Jačka", y="* 1893", st="doc", f=["* 1. 1. 1893 Brloh čp. 37 (Nedílná, fara Čížová)", "zednický pomocník, domkář v Nedílné čp. 37", "× 21. 5. 1921 Čížová, Jana Cvrčková"], r=["cizova_krest_jan_jacka_1893", "cizova_snatek_jan_jacka_1921", "cizova_snatek_josef_krivanec_1947"],
             note="Otec Marie Jačkové (7); sňatek 1921 i sňatek dcery 1947 doloženy. Příjmení v matrice „Jačka“ (rodina „Jaček“)."),
    15: dict(n="Jana Cvrčková", y="1899 – před 1947", st="doc", f=["* 21. 5. 1899 Mlaka čp. 21 (fara Čížová)", "× 21. 5. 1921 Čížová, Jan Jačka", "† před 1947"], r=["cizova_krest_jana_cvrckova_1899", "cizova_snatek_jan_jacka_1921", "cizova_snatek_josef_krivanec_1947"],
             note="Matka Marie Jačkové (7). V křestní matrice „Johanna Julie“.. Sňatek 1921 potvrdil čtení ze sňatku dcery 1947; vdávala se v den svých 22. narozenin."),
    28: dict(n="Josef Jačka", y="", st="doc", f=["* Brloh čp. 22", "domkář v Brlohu (Nedílné) čp. 37"], r=["cizova_krest_jan_jacka_1893", "cizova_snatek_jan_jacka_1921"],
             note="Otec Jana Jačky (14) podle sňatku 1921."),
    29: dict(n="Terezie Matoušková", y="", st="doc", f=["* Malá Turná čp. 2 (okr. Strakonice)"], r=["cizova_krest_jan_jacka_1893", "cizova_snatek_jan_jacka_1921"],
             note="Matka Jana Jačky (14) podle sňatku 1921."),
    30: dict(n="Jan Cvrček", y="* 1864", st="doc", f=["* 2. 2. 1864 Mlaka čp. 21 (fara Čížová)", "chalupník na Mlakách čp. 21", "× 3. 10. 1893 Čížová, Johanna Sichrovská"], r=["cizova_krest_jan_cvrcek_1864", "cizova_snatek_jan_cvrcek_1893", "cizova_krest_jana_cvrckova_1899", "cizova_snatek_jan_jacka_1921"],
             note="Otec Jany Cvrčkové (15) podle sňatku 1921."),
    31: dict(n="Johanna Sichrovská", y="* 1868", st="doc", f=["* 16. 5. 1868 Třepkov čp. 18 (fara Čížová)", "× 3. 10. 1893 Čížová, Jan Cvrček"], r=["cizova_krest_johanna_sichrovska_1868", "cizova_snatek_jan_cvrcek_1893", "cizova_krest_jana_cvrckova_1899", "cizova_snatek_jan_jacka_1921"],
             note="Matka Jany Cvrčkové (15) podle sňatku 1921."),
    8: dict(n="Václav Mrvík", y="* 1884", st="prob", f=["* 29. 8. 1884 Podruhlí čp. 27 (fara Bělčice)", "× 4. 2. 1908 Bělčice, Marie Hupáková", "bydlel v Koupi čp. 51"],
            r=["belcice_krest_vaclav_mrvik_1884", "belcice_snatek_vaclav_mrvik_1908", "belcice_index_josef_mrvik_1910"],
            note="Křest a sňatek doloženy matrikou. Že je otcem Josefa (4), je pravděpodobné, ne přímo doložené: novomanželé bydleli v Koupi čp. 51 a tam se 1909 narodila Marie a 1910 Josef Mrvík, otec domkář (rejstřík narozených). Jméno otce v rejstříku není; kniha narozených po 1903 zatím není online."),
    9: dict(n="Marie Hupáková", y="* 1885", st="prob", f=["* 6. 8. 1885 Hošovice čp. 16 (fara Černívsko)", "× 4. 2. 1908 Bělčice, Václav Mrvík", "bydlela v Koupi čp. 51"],
            r=["cernivsko_krest_marie_hupakova_1885", "belcice_snatek_vaclav_mrvik_1908"],
            note="Křest a sňatek doloženy matrikou; matkou Josefa (4) pravděpodobně – viz Václav (8). Hošovice = na portálu archivu „Hostišovice“, fara Černívsko (odtud i křestní list ze sňatku 1908)."),
    16: dict(n="Václav Mrvík", y="* 1854", st="prob", f=["* 26. 1. 1854 Podruhlí čp. 12", "záložník c. k. 18. praporu myslivců (1883)", "× 9. 10. 1883 Bělčice, Barbora Křížová roz. Lokajová, vdova", "domkář v Podruhlí čp. 27", "1908 souhlasil se sňatkem nezletilého syna a podepsal se"],
             r=["belcice_krest_vaclav_mrvik_1854", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884", "belcice_snatek_vaclav_mrvik_1908"],
             note="Otec Václava (8) podle zápisu o křtu 1884 i o sňatku 1908; vlastní křest 1854 nalezen. Spojení s rodokmenem pravděpodobné (viz 8)."),
    17: dict(n="Barbora Lokajová", y="* 1845", st="prob", f=["* 27. 10. 1845 Ostrov čp. 4 (fara Mišovice)", "1. manžel Antonín Kříž, domkář v Podruhlí čp. 27", "× 9. 10. 1883 Bělčice, Václav Mrvík"],
             r=["misovice_krest_barbora_lokajova_1845", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884", "belcice_snatek_vaclav_mrvik_1908"],
             note="Matka Václava (8). Křest doložen (s okrajovou poznámkou o sňatku 1883). Při druhém sňatku 1883 jí bylo 38 let, o devět let víc než ženichovi. Dům čp. 27 v Podruhlí byl jejího prvního manžela. Číslo domu v Ostrově: 1883 a 1884 „č. 4“, 1908 „č. 1“ (?)."),
    18: dict(n="Václav Hupák", y="* 1854", st="prob", f=["* 13. 2. 1854 Hošovice čp. 16 (fara Černívsko)", "záložník c. k. 1. pluku zákopníků (1880)", "domkář v Hošovicích čp. 16", "× 21. 9. 1880 Bělčice, Marie Vavříková z Újezdce"],
             r=["cernivsko_krest_vaclav_hupak_1854", "belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885", "belcice_snatek_vaclav_mrvik_1908"],
             note="Otec Marie (9); křest i sňatek doloženy matrikou. Spojení s rodokmenem pravděpodobné (viz 8)."),
    19: dict(n="Marie Vavříková", y="* 1856", st="prob", f=["* 25. 1. 1856 Újezdec čp. 36 (fara Bělčice)", "bydlela v Újezdci čp. 36", "× 21. 9. 1880 Bělčice, Václav Hupák"],
             r=["belcice_krest_marie_vavrikova_1856", "belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885", "belcice_snatek_vaclav_mrvik_1908"],
             note="Křest 1856 i sňatek 1880 shodně: dcera Františka Vavříka. Při sňatku 1880 dcera Františka Vavříka, kováře v Újezdci čp. 36, a Anny roz. Kozlové. Při křtu dcery 1885 a sňatku dcery 1908 ale uvedena jako dcera (rodem) Tintěrová, dcera Josefa Tintěry z Koupě čp. 51 a Anny roz. Kozlové. Matka sedí, otec ne – viz ISSUES."),
    32: dict(n="Václav Mrvík", y="", st="prob", f=["domkář v Podruhlí čp. 12"], r=["belcice_krest_vaclav_mrvik_1854", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884"],
             note="Dědeček Václava (8) podle zápisu o křtu 1884; spojení s rodokmenem pravděpodobné (viz 8)."),
    33: dict(n="Marie Pirhanzlová", y="", st="prob", f=["z Chobota (okr. Blatná)"], r=["belcice_krest_vaclav_mrvik_1854", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884"],
             note="Babička Václava (8) podle zápisu o křtu 1884 („rodem Pirhanzl z Chobota“); spojení s rodokmenem pravděpodobné (viz 8)."),
    34: dict(n="Václav Lokaj", y="", st="prob", f=["chalupník v Ostrově čp. 4 (okr. Březnice)"], r=["misovice_krest_barbora_lokajova_1845", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884"],
             note="Otec Barbory (17) podle zápisu o křtu 1884; spojení s rodokmenem pravděpodobné (viz 8)."),
    35: dict(n="Anna Suchá", y="", st="prob", f=["z Paračova (okr. Blatná)"], r=["misovice_krest_barbora_lokajova_1845", "belcice_snatek_vaclav_mrvik_1883", "belcice_krest_vaclav_mrvik_1884"],
             note="Matka Barbory (17), dcera Martina Suchého, domkáře z Paračova (křest 1845) – potvrzuje čtení „Suchá“ ze sňatku 1883."),
    68: dict(n="Jakub Lokaj", y="– před 1845", st="prob", f=["chalupník v Ostrově", "† před 1845"], r=["misovice_krest_barbora_lokajova_1845"],
             note="Otec Václava Lokaje (34) podle křtu vnučky 1845; spojení s rodokmenem pravděpodobné (viz 8)."),
    69: dict(n="Dorota Kolářová (?)", y="– před 1845", st="prob", f=["z Hodonic (?)", "† před 1845"], r=["misovice_krest_barbora_lokajova_1845"],
             note="Matka Václava Lokaje (34) podle křtu vnučky 1845; jméno, příjmení i místo čteny nejistě."),
    70: dict(n="Martin Suchý", y="", st="prob", f=["domkář v Paračově"], r=["misovice_krest_barbora_lokajova_1845"],
             note="Otec Anny (35) podle křtu vnučky 1845; spojení s rodokmenem pravděpodobné (viz 8)."),
    71: dict(n="Kateřina Krčmářová (?)", y="– před 1845", st="prob", f=["z Lašovic (?)", "† před 1845"], r=["misovice_krest_barbora_lokajova_1845"],
             note="Matka Anny (35) podle křtu vnučky 1845; příjmení i místo čteny nejistě."),
    36: dict(n="Martin Hupák", y="* asi 1812", st="prob", f=["* asi 1812", "vysloužilý voják 35. pěšího pluku (1845)", "× 17. 11. 1845 Černívsko, Barbora Kočovská", "domkář v Hošovicích čp. 16"], r=["cernivsko_snatek_martin_hupak_1845", "cernivsko_krest_vaclav_hupak_1854", "belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885"],
             note="Otec Václava Hupáka (18) podle zápisu o křtu vnučky 1885; spojení s rodokmenem pravděpodobné (viz 8)."),
    37: dict(n="Barbora Kočovská", y="* asi 1810", st="prob", f=["* asi 1810", "podruhyně v Hošovicích čp. 22 (1845)", "× 17. 11. 1845 Černívsko, Martin Hupák"], r=["cernivsko_snatek_martin_hupak_1845", "cernivsko_krest_vaclav_hupak_1854", "belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885"],
             note="Matka Václava Hupáka (18) podle sňatku syna 1880; sňatek s Martinem 1845 doložen. Rozpor: zápis o křtu Václava 1854 uvádí matku jako „Marii, dceru Jana Š[kách]y (?), domkáře z Hošovic č. 30, a Marie roz. Šimůnkové“ – to je jiná rodina (Marie Škáchová, dcera Jana Škáchy z Hošovic 30, se 1848 vdala za jiného muže). Nejspíš omyl písaře v roce 1854 – viz ISSUES."),
    38: dict(n="František Vavřík", y="", st="prob", f=["kovář v Újezdci čp. 36"], r=["belcice_krest_marie_vavrikova_1856", "belcice_snatek_vaclav_hupak_1880"],
             note="Otec Marie (19) podle jejího křtu 1856 i sňatku 1880. Pozdější zápisy (1885, 1908) uvádějí jako otce Josefa Tintěru – nejspíš nevlastní otec, viz SIDE."),
    39: dict(n="Anna Kozlová", y="", st="prob", f=["z Koupě čp. 3"], r=["belcice_krest_marie_vavrikova_1856", "belcice_snatek_vaclav_hupak_1880", "cernivsko_krest_marie_hupakova_1885"],
             note="Matka Marie (19), dcera Václava Kozla z Koupě čp. 3 (křest 1856, sňatek 1880). Není totožná s Annou Kozlovou, dcerou Martina Kozla, která si 1871 vzala Josefa Tintěru – viz ISSUES."),
    76: dict(n="Jakub Vavřík", y="– před 1856", st="prob", f=["kovář v Újezdci čp. 36", "† před 1856"], r=["belcice_krest_marie_vavrikova_1856"],
             note="Otec Františka (38) podle křtu vnučky 1856 (tehdy už zesnulý); spojení s rodokmenem pravděpodobné (viz 8)."),
    77: dict(n="Barbora Maštalířová", y="", st="prob", f=["z Újezdce čp. 27"], r=["belcice_krest_marie_vavrikova_1856"],
             note="Matka Františka (38) podle křtu vnučky 1856; spojení s rodokmenem pravděpodobné (viz 8)."),
    78: dict(n="Václav Kozel", y="", st="prob", f=["chalupník v Koupi čp. 3"], r=["belcice_krest_marie_vavrikova_1856"],
             note="Otec Anny (39) podle křtu vnučky 1856; „Kozel“ potvrzuje i sňatek jeho syna Josefa 1849 (Černívsko, kniha 7, sn. 16)."),
    79: dict(n="Anna Hudečková (?)", y="", st="prob", f=["z Volenic"], r=["belcice_krest_marie_vavrikova_1856"],
             note="Matka Anny (39) podle křtu vnučky 1856 a sňatku syna Josefa 1849 („Anna rozená Hudeček z Volenic N. 15“)."),
    72: dict(n="Matěj Hupák", y="", st="prob", f=["domkář v Hošovicích čp. 16"], r=["cernivsko_krest_vaclav_hupak_1854"],
             note="Otec Martina (36) podle křtu vnuka 1854; spojení s rodokmenem pravděpodobné (viz 8)."),
    73: dict(n="Kateřina Zelenková", y="", st="prob", f=["z Chobota čp. 8"], r=["cernivsko_krest_vaclav_hupak_1854"],
             note="Matka Martina (36) podle křtu vnuka 1854; spojení s rodokmenem pravděpodobné (viz 8)."),
    74: dict(n="František Kočovský", y="– před 1845", st="prob", f=["krejčí (?) z Kraupic (?) čp. 6", "† před 1845"], r=["cernivsko_snatek_martin_hupak_1845"],
             note="Otec Barbory (37) podle jejího sňatku 1845; řemeslo a místo čteny nejistě."),
    75: dict(n="Anna Černá (?)", y="", st="prob", f=["z Kraupic (?)"], r=["cernivsko_snatek_martin_hupak_1845"],
             note="Matka Barbory (37) podle jejího sňatku 1845; příjmení čteno nejistě."),
    52: dict(n="Anna Lišková", y="", st="doc", f=["z Sedlice"], r=["radomysl_krest_anezka_liskova_1894"], note="Matka Františka Lišky (26), dcera Matěje Lišky, obecního sluhy v Sedlici čp. 78 (zápis 1894). Otec Františka neuveden."),
    53: dict(n="otec neuveden", st="unk", f=[], note="František Liška (26) byl podle zápisu 1894 nemanželský syn Anny Liškové."),
    54: dict(n="Jan Čapek", y="", st="doc", f=["domkář v Chrášťovicích čp. 30"], r=["radomysl_krest_anezka_liskova_1894"], note="Otec Anny Čapkové (27) podle křtu vnučky 1894."),
    55: dict(n="Josefa Duchoslavová", y="", st="doc", f=["z Lázu čp. 22"], r=["radomysl_krest_anezka_liskova_1894"], note="Matka Anny Čapkové (27) podle křtu vnučky 1894."),
    56: dict(n="Josef Jačka", y="", st="doc", f=["chalupník v Brlohu čp. 22"], r=["cizova_krest_jan_jacka_1893"], note="Dědeček Jana Jačky (14) podle jeho křtu 1893."),
    57: dict(n="Anna Kunclová (?)", y="", st="doc", f=["z Třepkova čp. 5"], r=["cizova_krest_jan_jacka_1893"], note="Babička Jana Jačky (14) podle jeho křtu 1893; příjmení čteno nejistě."),
    58: dict(n="Václav Matoušek", y="", st="doc", f=["rolník (sedlák) v Malé Turné čp. 2"], r=["cizova_krest_jan_jacka_1893"], note="Dědeček Jana Jačky (14) podle jeho křtu 1893."),
    59: dict(n="Anna Houdková", y="", st="doc", f=["z Domanic čp. 16"], r=["cizova_krest_jan_jacka_1893"], note="Babička Jana Jačky (14) podle jeho křtu 1893 (čteno „Hes…“); příjmení „Houdek z Domanic č. 16“ zřetelně v zápisu o sňatku její dcery Rosálie 1891 (Radomyšl O, kniha 18, sn. 187)."),
    60: dict(n="Jan Cvrček", y="", st="doc", f=["chalupník na Mlakách čp. 21"], r=["cizova_krest_jan_cvrcek_1864", "cizova_snatek_jan_cvrcek_1893", "cizova_krest_jana_cvrckova_1899"], note="Dědeček Jany Cvrčkové (15) podle jejího křtu 1899."),
    61: dict(n="Marie Křížová", y="", st="doc", f=["z Mlak čp. 26"], r=["cizova_krest_jan_cvrcek_1864", "cizova_snatek_jan_cvrcek_1893", "cizova_krest_jana_cvrckova_1899"], note="Babička Jany Cvrčkové (15) podle jejího křtu 1899."),
    62: dict(n="Jan Sichrovský", y="", st="doc", f=["kolář (1868), chalupník (1893), domkář (1899) v Třepkově čp. 18"], r=["cizova_krest_johanna_sichrovska_1868", "cizova_snatek_jan_cvrcek_1893", "cizova_krest_jana_cvrckova_1899"], note="Dědeček Jany Cvrčkové (15) podle jejího křtu 1899."),
    63: dict(n="Anna Ratajová", y="", st="doc", f=["z Třepkova čp. 15"], r=["cizova_krest_johanna_sichrovska_1868", "cizova_snatek_jan_cvrcek_1893", "cizova_krest_jana_cvrckova_1899"], note="Babička Jany Cvrčkové (15) podle jejího křtu 1899."),
    24: dict(n="Václav Křivanec", y="", st="doc", f=["chalupník v Leskovicích čp. 32 (1891)"], r=["radomysl_krest_josef_krivanec_1891"], note="Otec Josefa Křivance (12) podle jeho křtu 1891."),
    25: dict(n="Anna Varousová", y="", st="doc", f=["z Doubravice čp. 60"], r=["radomysl_krest_josef_krivanec_1891"], note="Matka Josefa Křivance (12) podle jeho křtu 1891."),
    48: dict(n="Václav Křivanec", y="", st="doc", f=["sedlák v Leskovicích čp. 10"], r=["radomysl_krest_josef_krivanec_1891"], note="Dědeček Josefa Křivance (12) podle jeho křtu 1891."),
    49: dict(n="Barbora Finková", y="", st="doc", f=["z Nahošína čp. 5"], r=["radomysl_krest_josef_krivanec_1891"], note="Babička Josefa Křivance (12) podle jeho křtu 1891."),
    50: dict(n="Josef Varous", y="", st="doc", f=["sedlák v Doubravici čp. 60", "1891 kmotr vnuka Josefa"], r=["radomysl_krest_josef_krivanec_1891"], note="Dědeček Josefa Křivance (12) podle jeho křtu 1891."),
    51: dict(n="Marie Švehlová", y="", st="doc", f=["z Mečichova čp. 26"], r=["radomysl_krest_josef_krivanec_1891"], note="Babička Josefa Křivance (12) podle jeho křtu 1891."),
    120: dict(n="Josef Cvrček", y="", st="doc", f=["sedlák z Černíkova (?)"], r=["cizova_krest_jan_cvrcek_1864"], note="Otec Jana Cvrčka st. (60) podle křtu vnuka 1864; místo čteno nejistě."),
    121: dict(n="Anna Líšalová (?)", y="", st="doc", f=["z Pražetic (?)"], r=["cizova_krest_jan_cvrcek_1864"], note="Matka Jana Cvrčka st. (60) podle křtu vnuka 1864; příjmení i místo čteny nejistě."),
    122: dict(n="Josef Kříž", y="", st="doc", f=["chalupník na Mlakách čp. 21"], r=["cizova_krest_jan_cvrcek_1864"], note="Otec Marie Křížové (61) podle křtu vnuka 1864; dům čp. 21 byl jeho – Cvrček se přiženil."),
    123: dict(n="Barbora Voldánová", y="", st="doc", f=["z Brloha"], r=["cizova_krest_jan_cvrcek_1864"], note="Matka Marie Křížové (61) podle křtu vnuka 1864."),
    124: dict(n="Josef Sichrovský", y="", st="doc", f=["kolář v Čížové čp. 3"], r=["cizova_krest_johanna_sichrovska_1868"], note="Otec Jana Sichrovského (62) podle křtu vnučky 1868."),
    125: dict(n="Barbora Bartasová (?)", y="", st="doc", f=["z Pamětic"], r=["cizova_krest_johanna_sichrovska_1868"], note="Matka Jana Sichrovského (62) podle křtu vnučky 1868; příjmení nejisté."),
    126: dict(n="Jakub Rataj", y="", st="doc", f=["domkář v Třepkově čp. 18"], r=["cizova_krest_johanna_sichrovska_1868"], note="Otec Anny Ratajové (63) podle křtu vnučky 1868; dům čp. 18 byl jeho."),
    127: dict(n="Anna Schránilová (?)", y="", st="doc", f=["z Borečnice"], r=["cizova_krest_johanna_sichrovska_1868"], note="Matka Anny Ratajové (63) podle křtu vnučky 1868; příjmení nejisté."),
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
    12: ("Křivancovi", "Kováři z Leskovic čp. 32 u Radomyšle na Strakonicku; po válce přesídlili do Damnova u Plané na Tachovsku."),
    13: ("Liškovi", "Z Chrášťovic u Radomyšle."),
    14: ("Jačkovi", "Domkáři z Nedílné čp. 37 (obec Brloh) u Čížové na Písecku."),
    15: ("Cvrčkovi", "Chalupníci na Mlakách čp. 21 u Čížové."),
    8: ("Mrvíkové", "Domkáři z Podruhlí a Koupě na Blatensku (fara Bělčice); Josef Mrvík (1910) odešel po válce na Tachovsko."),
    9: ("Hupákovi", "Domkáři z Hošovic čp. 16 (fara Černívsko); Marie Hupáková (1885) se vdala do Koupě čp. 51, domu Josefa Tintěry."),
}

# Příbuzní mimo přímou linii (sourozenci, strýcové…): k = číslo předka, ke kterému patří.
# dict(k=16, n="Josef Novák (1865–1920)", t="Bratr Jana. Kovář v …", r=["klic_zapisu"])
SIDE = [
    dict(k=31, n="Josef Sichrovský", t="Profesor v Novém Jičíně na Moravě; 1899 kmotr Jany Cvrčkové – nejspíš bratr její matky Johanny.", r=["cizova_krest_jana_cvrckova_1899"]),
    dict(k=39, n="Josef Kozel (* asi 1823)", t="Bratr Anny Kozlové (39): chalupník v Koupi čp. 3, syn Václava Kozla, chalupníka tamtéž, a Anny roz. Hudečkové z Volenic čp. 15; 30. 1. 1849 se oženil v Černívsku (oddíl Uzenice). Potvrzuje rodiče Anny.", r=[]),
    dict(k=19, n="Josef Tintěra (* asi 1830) a Anna Kozlová (* asi 1838)", t="Josef, čeledín v panském dvoře v Březnici, syn řezníka Šimona Tintěry z Koupě čp. 54; 1. 5. 1871 si vzal svobodnou Annu Kozlovou, dceru domkáře Martina Kozla z Koupě čp. 51. Při křtu Marie Hupákové 1885 a sňatku 1908 jsou uvedeni jako rodiče její matky Marie (a Josef byl 1885 kmotr), jenže Marie (* 1856) byla podle křtu i sňatku dcerou kováře Františka Vavříka a jiné Anny Kozlové (dcery Václava Kozla z Koupě čp. 3). Vztah zatím nevysvětlen – možná pěstouni nebo příbuzní. Do jejich domu čp. 51 se 1908 nastěhovali Mrvíkovi.", r=["belcice_snatek_josef_tintera_1871", "cernivsko_krest_marie_hupakova_1885"]),
    dict(k=32, n="Vojtěch Mrvík", t="Domkář v Podruhlí čp. 11, děti 1839–1847 (Marie, Anna, Anděla). Ve stejném domě se 1851 narodil syn Václava Mrvíka (32) František. Možná Václavův bratr – neověřeno."),
    dict(k=16, n="Anna a František Mrvíkovi", t="Sourozenci Václava (16): Anna * 11. 10. 1849 Podruhlí čp. 12, František * 9. 5. 1851 Podruhlí čp. 11 (podle rejstříku narozených Bělčice)."),
    dict(k=16, n="František Mrvík", t="Domkář v Podruhlí čp. 7, syn Václava Mrvíka z čp. 12 a Marie Pirhanzlové – tedy nejspíš bratr Václava (16). Jeho syn Josef se narodil 2. 4. 1884 (zápis na stejné stránce jako Václav, čteno z náhledu). František Mrvík, domkář v Podruhlí, byl 1908 svědkem na svatbě Václava (8).", r=["belcice_krest_vaclav_mrvik_1884"]),
    dict(k=4, n="Marie Mrvíková (* 1909)", t="Narozena 8. 3. 1909 v Koupi č. 51, otec domkář – stejný dům jako Josef (1910), rok po svatbě Václava Mrvíka a Marie Hupákové; nejspíš Josefova starší sestra.", r=["belcice_index_josef_mrvik_1910"]),
]

# Rozpory a otevřené otázky (na web do „Co hledáme“) jako dvojice (otázka, odpověď). Odpověď začněte
# „Vyřešeno: …“ (na webu se skryje), „Hypotéza: …“ nebo „Otevřené: …“. Jde na web – nic citlivého.
# ("Kdy se narodil Jan Novák?", "Otevřené: rodina říká 1850, v Holicích 1848–1852 nenalezen.")
ISSUES = [
    ("Kdo byla matka Václava Hupáka (* 1854)?", "Hypotéza: Barbora Kočovská (sňatek s Martinem Hupákem 1845, sňatek syna 1880). Zápis o křtu 1854 má jako matku Marii, dceru Jana Škáchy z Hošovic 30 – nejspíš omyl písaře (Škáchovi byli sousedé)."),
    ("Kdo byl otcem Marie, provdané Hupákové (* 1856)?", "Vyřešeno: František Vavřík, kovář z Újezdce čp. 36 (křest 1856 i sňatek 1880)."),
    ("Proč zápisy 1885 a 1908 uvádějí jako rodiče Marie Hupákové roz. Vavříkové Josefa Tintěru a Annu Kozlovou z Koupě čp. 51?", "Otevřené: Josef Tintěra se 1871 oženil se svobodnou Annou Kozlovou, dcerou Martina Kozla z Koupě 51 – jiná žena než Mariina matka (dcera Václava Kozla z Koupě 3). Možná Marii vychovali (příbuzní její matky?). Ověřit úmrtí Františka Vavříka a Anny Vavříkové (Bělčice, zemřelí)."),
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
