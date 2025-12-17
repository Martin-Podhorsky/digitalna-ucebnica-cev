---
linkTitle: "12.2 Posilňovače riadenia"
title: "Posilňovače riadenia"
type: docs
weight: 2
sidebar:
  open: false
---

Posilňovač riadenia je zariadenie, ktoré znižuje silu potrebnú na otáčanie volantu. Bez posilňovača by bolo riadenie, najmä pri nízkych rýchlostiach alebo pri parkovaní, veľmi namáhavé. Posilňovače riadenia znižujú potrebnú ovládaciu silu až o 80%.

## Hydraulický posilňovač riadenia (HPS)

Hydraulický posilňovač riadenia využíva tlak hydraulickej kvapaliny (oleja) na zosilnenie sily, ktorú vodič vyvíja na volant.

### Hlavné časti:

{{< figure src="HPS.png" alt="Schéma hydraulického posilňovača riadenia (HPS)" width="80%" caption="Obr. 12.11 - Schéma hydraulického posilňovača riadenia (HPS)" >}}

1 - Riadené kolesá <br>
2 a 4 - Pomocné páky <br>
3 - Pracovný valec <br>
5 - Ovládací ventil <br>
6 - Posúvač ovládacieho ventilu
7 - Čerpadlo <br>
8 - Nádržka <br>
9 - Hriadeľ volantu <br>
10 - Prevodovka riadenia <br>
11 - Hlavná páka riadenia <br>
12 - Kalibrovaný otvor

### Princíp činnosti:

Pri otáčaní volantu v smere hodiových ručičiek (doprava) sa hlavná páka riadenia (11) prevodovky riadenia (10) otáča v smere hodinových ručičiek a presúva posúvač ovládacieho ventilu (6) dozadu, proti smeru pohybu vozidla. Následkom toho prechádza tlakový olej z čerpadla (7) cez ovládací ventil (5) do priestoru A pracovného valca (3). Pracovný valec (3) začína natáčať riadené kolesá (1) doprava. Priestor B pracovného valca je pritom prepojený cez ovládací ventil s nádržkou (8), do ktorej je z neho olej vytláčaný. Obdobný proces sa deje pri zatáčaní smerom doľava.

### Výhody:

- Výrazné zníženie ovládacej sily (až o 80%)
- Lepší komfort riadenia, najmä pri parkovaní
- Dobrá spätná väzba z cesty (vodič cíti odpor kolies)
- Spoľahlivá a overená technológia

### Nevýhody:

- Závislosť od chodu motora (pri vypnutom motore nefunguje)
- Čerpadlo beží neustále, aj keď nie je potrebné
- Potreba pravidelnej údržby (kontrola a výmena oleja, hadíc)
- Možné úniky hydraulickej kvapaliny

### Použitie

Staršie osobné automobily, nákladné vozidlá, autobusy a ťažké úžitkové vozidlá.

## Elektrohydraulický posilňovač riadenia (EHPS)

EHPS kombinuje prvky hydraulického a elektrického systému. Namiesto čerpadla poháňaného motorom využíva **elektrické čerpadlo** na generovanie hydraulického tlaku.

### Výhody oproti HPS:

- Čerpadlo pracuje len keď je potrebné
- Nezávisí od otáčok motora
- Možnosť meniť silový účinok posilňovača (zvýšiť alebo znížiť) reguláciou elektrického čerpadla

### Použitie:

Ťažké úžitkové vozidlá a niektoré osobné automobily ako prechodná technológia medzi HPS a EPS.

## Elektronický posilňovač riadenia (EPS)

EPS (Electric Power Steering) je moderný systém posilňovania riadenia pomocou elektromotora. V súčasnosti sa používa vo väčšine nových osobných automobilov.

{{< figure src="eps-schema.png" alt="Schéma elektronického posilňovača riadenia" width="70%" caption="Obr. 12.12 - Schéma elektronického posilňovača riadenia" >}}

### Hlavné časti:

1 - Jednosmerný elektromotor (klasický alebo bezkartáčový) <br>
2 - Riadiaca jednotka (ECU) <br>
3 - Snímač krútiaceho momentu <br>
4 - Snímač uhla natočenia volantu <br>
5 - Prevodovka elektromotora

### Princíp činnosti:

1. Snímač krútiaceho momentu meria silu, ktorou vodič pôsobí na volant.
2. Snímač uhla natočenia určuje polohu a smer otáčania volantu.
3. Riadiaca jednotka vyhodnocuje údaje zo snímačov a z ďalších systémov vozidla (rýchlosť, otáčky motora).
4. Na základe vyhodnotenia ECU aktivuje elektromotor, ktorý poskytuje potrebnú pomocnú silu.

### Typy EPS podľa umiestnenia elektromotora:

1. **C-EPS (Column-mounted)** - motor pripojený k stĺpiku riadenia. Používa sa v menších a stredných vozidlách.
2. **P-EPS (Pinion-mounted)** - motor na vstupe prevodovky riadenia (na pastorku). Vhodné pre stredné vozidlá.
3. **R-EPS (Rack-mounted)** - motor priamo na ozubenú tyč (hrebeň). Používa sa vo väčších vozidlách pre vyšší výkon.

### Výhody:

- Nezávisí od chodu motora (funguje aj pri vypnutom motore)
- Nižšia spotreba paliva (motor pracuje len pri riadení)
- Premenlivé posilňovanie podľa rýchlosti vozidla
- Žiadna hydraulika (bez rizika úniku oleja)
- Jednoduchšia údržba a vyššia spoľahlivosť
- Tichšia prevádzka
- Možnosť integrácie s asistenčnými systémami (parkovací asistent, udržiavanie v jazdnom pruhu, autonómne riadenie)

### Nevýhody:

- Vyššie náklady na opravu elektronických komponentov
- Menej priamy pocit z riadenia v porovnaní s hydraulickým systémom (závisí od nastavenia výrobcu)
- Diagnostika vyžaduje špeciálne vybavenie

### Funkcie moderných EPS systémov:

- **Premenlivé posilňovanie podľa rýchlosti** - pri nízkych rýchlostiach (parkovanie) je riadenie ľahké, pri vysokých rýchlostiach tuhšie pre lepšiu stabilitu
- **Aktívny návrat volantu** do stredovej polohy
- **Kompenzácia bočného vetra** - automatická korekcia pri nárazoch vetra
- **Asistent pre udržanie v jazdnom pruhu (LKA)** - jemné korekcie riadenia
- **Parkovací asistent** - automatické natáčanie volantu pri parkovaní

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="geometria-riadenia" title="Geometria riadenia" subtitle="Definícia, jednotlivé parametre, ich vplyv na jazdné vlastnosti...">}}
{{< /cards >}}