---
linkTitle: "10.5 Systém ABS"
title: "Systém ABS"
weight: 5
type: docs
sidebar:
  open: false
---

ABS (Anti-lock Braking System) je elektronický bezpečnostný systém, ktorý zabraňuje zablokovaniu kolies počas brzdenia. Zablokované kolesá strácajú priľnavosť k vozovke a vozidlo sa stáva neovládateľným - vodič nemôže zmeniť smer jazdy ani pri otáčaní volantom. ABS tento problém rieši automatickou reguláciou brzdného tlaku na jednotlivých kolesách.

## Princíp činnosti

Systém ABS neustále monitoruje rýchlosť otáčania každého kolesa pomocou snímačov. Tieto údaje porovnáva elektronická riadiaca jednotka (ECU) s aktuálnou rýchlosťou vozidla a rýchlosťou ostatných kolies. 

Keď ECU zistí, že niektoré koleso sa spomaľuje rýchlejšie než ostatné (hrozí zablokovanie), okamžite zníži brzdný tlak na tomto kolese pomocou hydraulických ventilov. Tým umožní kolesu opätovne sa roztočiť a obnoviť priľnavosť k vozovke. Akonáhle sa koleso znovu roztočí, systém opäť zvýši brzdný tlak. Tento proces sa opakuje niekoľkokrát za sekundu, čím sa zabezpečí optimálna brzdná sila bez straty ovládateľnosti vozidla.

Vodič tento proces vníma ako pulzovanie brzdového pedála a charakteristický zvuk z podvozku.

### Funkčný cyklus ABS:

1. **Normálne brzdenie** -- Vodič stlačí brzdový pedál, brzdný tlak sa zvyšuje vo všetkých kolesách.
2. **Detekcia hrozby zablokovania** -- Snímače detegujú, že niektoré koleso sa spomaľuje príliš rýchlo oproti ostatným.
3. **Udržiavacia fáza** -- ECU aktivuje ventily a brzdný tlak sa drží konštantný, aby sa zabránilo ďalšiemu spomaleniu kolesa.
4. **Odľahčovacia fáza** -- Ak koleso stále spomaľuje, systém zníži brzdný tlak, čím umožní kolesu opätovne sa roztočiť.
5. **Zvyšovacia fáza** -- Po obnovení rotácie kolesa systém opäť postupne zvyšuje brzdný tlak.
6. **Opakovanie cyklu** -- Celý proces sa opakuje 4 až 15-krát za sekundu, až kým trvá brzdenie.

## Hlavné časti

{{< figure src="ABS.png" alt="Schéma systému ABS" width="80%" caption="Obr. 10.17 - Schéma systému ABS" >}}

1 - **Snímače otáčok** -- sú umiestnené pri každom kolese a posielajú napäťové signály riadiacej jednotke. Najčastejšie ide o indukčné alebo Hallove snímače. <br>
2 - **Elektronická riadiaca jednotka (ECU)** -- dostáva signály vo forme napätia od snímačov otáčok a snímača rýchlosti vozidla v prípade, že vyhodnotí riziko zablokovania niektorého z kolies (prudký pokles otáčok kolesa vzhľadom na rýchlosť vozidla), posiela príkaz hydraulickej riadiacej jednotke na zníženie tlaku na príslušnom kolese.<br>
3 - **Hydraulická riadiaca jednotka (HCU)** -- obsahuje elektromagnetické ventily a čerpadlo. Ventily regulujú tok brzdovej kvapaliny k jednotlivým kolesám podľa pokynov ECU. Čerpadlo (spätná pumpa) slúži na odčerpávanie brzdovej kvapaliny od brzdových valčekov späť do hlavného brzdového valca proti tlaku brzdového pedála (to je to, čo spôsobuje tzv. „kopanie“ od pedála), aby umožnilo opätovné zvýšenie tlaku. Táto jednotka je zvyčajne umiestnená v motorovom priestore medzi hlavným brzdovým valcom a kolesami.<br>

## Výhody ABS:

- **Zachovanie riaditeľnosti** -- aj počas prudkého brzdenia môže vodič ovládať smer jazdy, pretože kolesá sa neblokujú a pneumatiky si udržiavajú priľnavosť k vozovke
- **Skrátenie brzdnej dráhy** -- na suchých a mokrých povrchoch dokáže ABS skrátiť brzdnú dráhu oproti vozidlám bez tohto systému, pretože optimalizuje brzdnú silu
- **Stabilita vozidla** -- vozidlo zostáva stabilné a nepodliehá šmyku ani vybočovaniu z dráhy
- **Možnosť brzdenia a riadenia súčasne** -- vodič môže brzdiť naplno a zároveň sa vyhýbať prekážkam
- **Rovnomerné opotrebenie pneumatík** -- zabránením zablokovania kolies sa znižuje nerovnomerné opotrebenie pneumatík
- **Zníženie stresu vodiča** -- vodič nemusí ovládať techniku kadencovaného brzdenia, systém to robí automaticky

## Nevýhody ABS:

- **Predĺžená brzdná dráha na sypkých povrchoch** -- na štrku, hlbokom snehu alebo ľade môže byť brzdná dráha dlhšia ako pri zablokovaných kolesách, ktoré by sa "zakopali" do podkladu. Napriek tomu ABS zachováva ovládateľnosť vozidla.
- **Vyššia obstarávacia cena** -- vozidlá s ABS sú drahšie na výrobu a tým pádom aj na nákup
- **Zložitejšia konštrukcia** -- systém obsahuje množstvo elektronických a hydraulických komponentov, čo zvyšuje komplexnosť
- **Potreba špecializovaného servisu** -- diagnostika a oprava vyžaduje špecializované zariadenia a vyškolených technikov
- **Falošný pocit bezpečnosti** -- niektorí vodiči sa spoliehajú na ABS a podceňujú bezpečnú vzdialenosť alebo prispôsobenie rýchlosti podmienkam

## Legislatíva

V Európskej únii je systém ABS povinnou výbavou všetkých nových osobných automobilov od roku 2004. Od roku 2016 musia byť všetky nové motocykle s objemom valcov nad 125 cm³ vybavené systémom ABS alebo kombinovaným brzdovým systémom (CBS). V mnohých krajinách sa ABS stal štandardom bezpečnosti a jeho prítomnosť výrazne prispieva k zníženiu počtu dopravných nehôd.

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="ASR" title="Regulácia preklzu kolies (ASR)" subtitle="Princíp činnosti, Konštrukcia, výhody, nevýhody...">}}
{{< /cards >}}