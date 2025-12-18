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

- Poskytuje prirodzenejšiu spätnú väzbu z cesty (vodič lepšie cíti povrch) na rozdiel od elektrických posilňovačov (EPS), ktoré môžu pôsobiť umelo.
- Má nižšie výrobné náklady a jednoduchšiu konštrukciu v porovnaní s modernými elektronickými systémami.
- Dokáže vyvinúť veľmi veľkú pomocnú silu, čo je výhoda pri ťažkých nákladných vozidlách oproti bežným systémom EPS.

### Nevýhody:

- Má vyššiu spotrebu paliva na rozdiel od EPS, pretože hydraulické čerpadlo beží neustále a zaťažuje motor.
- Vyžaduje pravidelnú údržbu a hrozí riziko úniku kvapaliny, čo pri EPS odpadá.
- Posilňovač je nefunkčný pri vypnutom motore (napr. pri ťahaní vozidla), na rozdiel od EPS.

### Použitie

Staršie osobné automobily, nákladné vozidlá, autobusy a ťažké úžitkové vozidlá.

## Elektrohydraulický posilňovač riadenia (EHPS)

EHPS kombinuje prvky hydraulického a elektrického systému. Namiesto čerpadla poháňaného motorom využíva **elektrické čerpadlo** na generovanie hydraulického tlaku.

### Výhody:

- Šetrí palivo v porovnaní s klasickým HPS, pretože elektrické čerpadlo nezaťažuje motor
- Účinok posilňovača je nezávislý od otáčok motora na rozdiel od mechanického HPS.
- Umožňuje jednoduchšiu reguláciu sily posilňovania pomocou elektroniky v porovnaní s HPS.

### Nevýhody:

- Systém stále vyžaduje hydraulický okruh a údržbu, na rozdiel od plne elektrického EPS.
- Konštrukcia je zložitejšia (kombinuje hydrauliku a elektroniku) v porovnaní s jednoduchším HPS alebo EPS.

### Použitie:

Ťažké úžitkové vozidlá a niektoré osobné automobily ako prechodná technológia medzi HPS a EPS.

## Elektronický posilňovač riadenia (EPS)

EPS (Electric Power Steering) je moderný systém posilňovania riadenia pomocou elektromotora. V súčasnosti sa používa vo väčšine nových osobných automobilov.

{{< figure src="eps-schema.png" alt="Schéma elektronického posilňovača riadenia" width="70%" caption="Obr. 12.12 - Schéma elektronického posilňovača riadenia" >}}

### Hlavné časti:

- Jednosmerný elektromotor (klasický alebo bezkartáčový) 
- Riadiaca jednotka (ECU) 
- Snímač krútiaceho momentu 
- Snímač uhla natočenia volantu 
- Prevodovka elektromotora

### Princíp činnosti:

1. Snímač krútiaceho momentu meria silu, ktorou vodič pôsobí na volant.
2. Snímač uhla natočenia určuje polohu a smer otáčania volantu.
3. Riadiaca jednotka vyhodnocuje údaje zo snímačov a z ďalších systémov vozidla (rýchlosť, otáčky motora).
4. Na základe vyhodnotenia ECU aktivuje elektromotor, ktorý poskytuje potrebnú pomocnú silu.

### Typy EPS podľa umiestnenia elektromotora:

1. **C-EPS (Column-mounted)** - motor pripojený k stĺpiku riadenia. Vyznačuje sa kompaktnou konštrukciou a nízkymi výrobnými nákladmi. Poskytuje pomocnú silu do 11 kN, preto sa používa najmä v malých a kompaktných vozidlách.

2. **P-EPS (Pinion-mounted)** - motor je umiestnený na pastorku. Vďaka priamemu pôsobeniu na pastorok ponúka lepší pocit z riadenia a nižšiu hlučnosť, keďže motor je umiestnený mimo kabíny. Pomocná sila dosahuje až 12 kN, čo ho robí vhodným pre stredne veľké vozidlá a SUV.

3. **R-EPS (Rack-mounted)** - motor je umiestnený priamo na hrebeni. Tento typ poskytuje najvyššiu pomocnú silu (až 16 kN), najpresnejšie riadenie a najnižšiu hlučnosť. Používa sa v luxusných vozidlách, veľkých SUV a športových automobiloch.

{{< figure src="typy-eps.png" alt="Obrázok porovnania systémov C-EPS, P-EPS a R-EPS" width="70%" caption="Obr. 12.13 - Porovnanie systémov C-EPS, P-EPS a R-EPS" >}}

### Výhody:

- Je úplne bezúdržbový a nehrozí únik oleja, na rozdiel od hydraulických systémov.
- Umožňuje integráciu pokročilých asistenčných systémov (LKA, parkovací asistent)
- Funguje aj pri vypnutom spaľovacom motore, na rozdiel od HPS.

### Nevýhody:

- Poskytuje menej prirodzený cit vo volante (spätná väzba) v porovnaní s hydraulickým HPS.
- Opravy sú nákladnejšie.
- Má menšiu maximálnu pomocnú silu ako HPS.

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