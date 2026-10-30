# Projekt rodokmenu

Tohle je projekt rodokmenu vedený skillem **rodokmen**. Na začátku každé konverzace:
1. Načti skill `rodokmen` (pokud ještě není načtený).
2. Přečti `data/STAV.md` – stav, pravidla a co je rozpracované – a konec `data/research_log.md`.
3. Pokračuj tam, kde se skončilo. Komunikuj česky, stručně a srozumitelně pro člověka bez zkušeností s genealogií a programováním.
4. Co by šlo ve skillu zlepšit (chyby nástrojů, nové archivy, nápady), zapisuj do `poznamky_pro_skill.md` – viz skill, sekce „Poznámky pro správce skillu“.

## Cloudové prostředí (claude.ai/code)
- Projekt žije v GitHub repozitáři `mrviklubos01-coder/rodokmen`, větev `claude/zacit-rodokmen-n7ezpf`. Kontejner je dočasný:
  co není uložené (`git commit`) a odeslané (`git push`), se po skončení relace ztratí.
- `pracovni/` se do gitu neukládá – stažené snímky matrik je tedy v nové relaci potřeba stáhnout znovu.
  Vše podstatné (výřezy, přepisy, deník) musí skončit v `data/`, `vyrezy/`, `zdroje/`.
- ImageMagick je tu verze 6 (`convert`), nástroje ji použijí samy.
- Náhled webu (localhost) uživatel nevidí – posílej snímky stránek z headless prohlížeče.

## Přání uživatele
- Každý nález zapisuj i do `data/podklady_pribeh.md` (věk snoubenců, dny svatba→narození, nemanželské děti, vojna, řemesla,
  domy, kmotři, rozpory, historické souvislosti). Uživatel z toho chce napsat rodinný příběh na pozadí dějin.
