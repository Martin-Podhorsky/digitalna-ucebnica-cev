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

Hydraulický posilňovač riadenia využíva tlak hydraulickej kvapaliny (oleja) na zosílnenie sily, ktorú vodič vyvíja na volant.

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

- **Prirodzená spätná väzba:** Tento posilňovač poskytuje prirodzenejšiu spätnú väzbu z cesty (vodič lepšie cíti povrch) na rozdiel od elektrických posilňovačov (EPS), ktoré môžu pôsobiť umelo.
- **Nižšie výrobné náklady:** Má jednoduchšiu konštrukciu a tým pádom je aj lacnejší na výrobu a prípadnú opravu v porovnaní s elektronickými posilňovačmi.
- **Veľká sila:** Posilňovač dokáže vyvinúť veľmi veľkú pomocnú silu, čož je výhodou pri ťažkých nákladných vozidlách oproti bežným elektronickým posilňovačom.

### Nevýhody:

- **Záťaž motora** Hydraulické čerpadlo beží neustále (aj keď nie je potrebné) a zaťažuje motor.
- **Údržba:** Hydraulika vyžaduje pravidelnú údržbu, pretože hrozí riziko úniku kvapaliny.
- **Závislosť od chodu motora:** Posilňovač je nefunkčný pri vypnutom motore (napr. pri ťahaní vozidla) a jeho účinok sa môže meniť v závislosti od otáčok motora, keďže ním je poháňané čerpadlo.

### Použitie

Staršie osobné automobily, nákladné vozidlá, autobusy a ťažké úžitkové vozidlá.

## Elektrohydraulický posilňovač riadenia (EHPS)

EHPS kombinuje prvky hydraulického a elektrického systému. Namiesto čerpadla poháňaného motorom využíva **elektrické čerpadlo** na generovanie hydraulického tlaku.

### Výhody:

- **Nezaťažuje motor:** Elektrické čerpadlo má samostatný pohon.
- **Nezávislosť od motora:** Účinok a fungovanie posilňovača nie je nezávislý od otáčok motora na rozdiel od HPS.
- **Regulácia:** Tento posilňovač umožňuje jednoduchšiu reguláciu sily posilňovania pomocou regulácie elektronického čerpadla (čo pri HPS nie je možné).

### Nevýhody:

- **Údržba** Systém stále má hydraulický okruh, ktorý vyžaduje údržbu.
- **Zložitejšia konštrukcia:** Kombinácia hydrauliky a elektroniky robí systém zložitejším a viac náchylným na poruchy v porovnaní s jednoduchšími HPS alebo EPS.

### Použitie:

Ťažké úžitkové vozidlá a niektoré osobné automobily ako prechodná technológia medzi HPS a EPS.

## Elektronický posilňovač riadenia (EPS)

EPS (Electric Power Steering) je moderný systém posilňovania riadenia pomocou elektromotora. V súčasnosti sa používa vo väčšine nových osobných automobilov.

{{< figure src="eps-schema.png" alt="Schéma elektronického posilňovača riadenia" width="70%" caption="Obr. 12.12 - Schéma elektronického posilňovača riadenia" >}}

### Hlavné časti:

- Jednosmerný elektromotor (klasický alebo bezkartáčový) 
- Riadiaca jednotka
- Snímač krútiaceho momentu 
- Snímač uhla natočenia volantu 
- Prevodovka elektromotora

### Princíp činnosti:

1. Snímač krútiaceho momentu meria silu, ktorou vodič pôsobí na volant.
2. Snímač uhla natočenia určuje polohu a smer otáčania volantu.
3. Riadiaca jednotka vyhodnocuje údaje zo snímačov a z ďalších systémov vozidla (rýchlosť, otáčky motora).
4. Na základe vyhodnotenia riadiaca jednotka aktivuje elektromotor, ktorý poskytuje potrebnú pomocnú silu.

### Typy EPS podľa umiestnenia elektromotora:

1. **C-EPS (Column-mounted)** - motor pripojený k stĺpiku riadenia. Vyznačuje sa kompaktnou konštrukciou a nízkymi výrobnými nákladmi. Poskytuje pomocnú silu do 11 kN, preto sa používa najmä v malých a kompaktných vozidlách.

2. **P-EPS (Pinion-mounted)** - motor je umiestnený na pastorku. Vďaka priamemu pôsobeniu na pastorok ponúka lepší pocit z riadenia a nižšiu hlučnosť, keďže motor je umiestnený mimo kabíny. Pomocná sila dosahuje až 12 kN, čo ho robí vhodným pre stredne veľké vozidlá a SUV.

3. **R-EPS (Rack-mounted)** - motor je umiestnený priamo na hrebeni. Tento typ poskytuje najvyššiu pomocnú silu (až 16 kN), najpresnejšie riadenie a najnižšiu hlučnosť. Používa sa v luxusných vozidlách, veľkých SUV a športových automobiloch.

{{< figure src="typy-eps.png" alt="Obrázok porovnania systémov C-EPS, P-EPS a R-EPS" width="70%" caption="Obr. 12.13 - Porovnanie systémov C-EPS, P-EPS a R-EPS" >}}

### Výhody:

- **Bezúdržbový:** Elektronický posilňovač riadenia je úplne bezúdržbový a nehrozí u neho únik oleja, na rozdiel od hydraulických systémov.
- **Asistenčné systémy:** Posiňovač umožňuje integráciu pokročilých asistenčných systémov (LKA, parkovací asistent).
- **Nezávislosť od motora:** Posilňovanie funguje aj pri vypnutom spaľovacom motore, na rozdiel od HPS.

### Nevýhody:

- **Menšia spätná väzba:** Poskytuje menej prirodzený cit vo volante v porovnaní s HPS alebo EHPS.
- **Cena:** EPS je drahší na výrobu a taktiež aj na prípadné opravy.
- **Sila:** Má spravidla menšiu maximálnu pomocnú silu ako HPS.

### Funkcie moderných EPS systémov:

- **Premenlivé posilňovanie podľa rýchlosti** -- pri nízkych rýchlostiach (parkovanie) je pomocná sila väčšia (ľahké riadenie), pri vysokých rýchlostiach menšia (tuhšie riadenie pre lepšiu stabilitu).
- **Aktívny návrat volantu** do stredovej polohy.
- **Kompenzácia bočného vetra** -- automatická korekcia jazdy pri nárazoch vetra.
- **Asistent pre udržanie v jazdnom pruhu (LKA)** -- jemné korekcie riadenia.
- **Parkovací asistent** -- automatické natáčanie volantu pri parkovaní.

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="/ucivo/2-rocnik/03-riadenie/geometria-riadenia" title="Geometria riadenia" subtitle="Definícia, jednotlivé parametre, ich vplyv na jazdné vlastnosti...">}}
{{< /cards >}}

---

{{< spoiler text="Zdroje" >}}
- FAKTOR, I., 2003, Cestné vozidlá II. Bratislava: EXPOL PEDAGOGIKA. ISBN 978-80-8091-351-9.
- https://actgroup.ir/electric-power-steering/
- https://en.wikipedia.org/wiki/Power_steering
{{< /spoiler >}}