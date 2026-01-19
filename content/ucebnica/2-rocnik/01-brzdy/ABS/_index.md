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

Systém ABS neustále monitoruje rýchlosť otáčania každého kolesa pomocou snímačov. Tieto údaje porovnáva elektronická riadiaca jednotka (ECU) s aktuálnou rýchlosťou vozidla a rýchlosťou ostatných kolies. Keď ECU zistí, že niektoré koleso spomaľuje rýchlejšie, než spomaľuje vozidlo (hrozí zablokovanie), okamžite zníži brzdný tlak na tomto danom kolese pomocou hydraulických ventilov. Tým umožní kolesu opätovne sa roztočiť a obnoviť priľnavosť k vozovke. Akonáhle sa koleso znovu roztočí, systém opäť zvýši brzdný tlak (vráti ho do normálu). Tento proces sa opakuje niekoľkokrát za sekundu, čím sa zabezpečí optimálna brzdná sila bez straty ovládateľnosti vozidla.

Vodič tento proces vníma ako pulzovanie brzdového pedála a charakteristický zvuk z podvozku.

## Hlavné časti

{{< figure src="ABS.png" alt="Schéma systému ABS" width="80%" caption="Obr. 10.17 - Schéma systému ABS" >}}

1 - **Snímače otáčok** -- sú umiestnené pri každom kolese a posielajú napäťové signály riadiacej jednotke. Najčastejšie ide o indukčné alebo Hallove snímače. <br>
2 - **Elektronická riadiaca jednotka (ECU)** -- dostáva signály vo forme napätia od snímačov otáčok a snímača rýchlosti vozidla. V prípade, že vyhodnotí riziko zablokovania niektorého z kolies (prudký pokles otáčok kolesa vzhľadom na rýchlosť vozidla), posiela príkaz hydraulickej riadiacej jednotke na zníženie tlaku na príslušnom kolese.<br>
3 - **Hydraulická riadiaca jednotka (HCU)** -- obsahuje elektromagnetické ventily a čerpadlo. Ventily regulujú tok brzdovej kvapaliny k jednotlivým kolesám podľa pokynov ECU. Čerpadlo (spätná pumpa) slúži na odčerpávanie brzdovej kvapaliny od brzdových valčekov späť do hlavného brzdového valca proti tlaku brzdového pedála (to je to, čo spôsobuje tzv. „kopanie“ od pedála), aby umožnilo opätovné zvýšenie tlaku. Táto jednotka je zvyčajne umiestnená v motorovom priestore medzi hlavným brzdovým valcom a kolesami.<br>

## Výhody ABS:

- **Zachovanie ovládateľnosti** -- aj počas prudkého brzdenia môže vodič meniť smer jazdy (vyhnúť sa prekážke), pretože kolesá si udržiavajú prilnavosť.
- **Skrátenie brzdnej dráhy** -- na suchých a mokrých povrchoch dokáže ABS výrazne skrátiť brzdnú dráhu oproti vozidlám bez tohto systému.
- **Rovnomerné opotrebenie pneumatík** -- zabránením blokovania kolies sa znižuje nerovnomerné opotrebenie pneumatík (spôsobené šmykom).

## Nevýhody ABS:

- Na štrku, hlbokom snehu alebo ľade je brzdná dráha výrazne dlhšia, ako pri vozidlách bez ABS. Na takomto povrchu je potreblepšie systém ABS vypnúť.
- Vozidlá so systémom ABS sú spravidla drahšie.
- Systém obsahuje množstvo elektronických a hydraulických komponentov, čo zvyšuje komplexitu.
- Diagnostika a oprava vyžaduje špecializované zariadenia a vyškolených technikov.

## Legislatíva

V Európskej únii je systém ABS povinnou výbavou všetkých nových osobných automobilov od roku 2004. Od roku 2016 musia byť všetky nové motocykle s objemom valcov nad 125 cm³ vybavené systémom ABS alebo kombinovaným brzdovým systémom (CBS). V mnohých krajinách sa ABS stal štandardom bezpečnosti a jeho prítomnosť výrazne prispieva k zníženiu počtu dopravných nehôd.

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="ASR" title="Regulácia preklzu kolies (ASR)" subtitle="Princíp činnosti, Konštrukcia, výhody, nevýhody...">}}
{{< /cards >}}

---

{{< spoiler text="Zdroje" >}}
- FAKTOR, I., 2003, Cestné vozidlá II. Bratislava: EXPOL PEDAGOGIKA. ISBN 978-80-8091-351-9.
- https://sk.wikipedia.org/wiki/ABS_(vozidlo)
- https://blog.upfix.com/how-anti-lock-braking-systems-enhance-vehicle-safety
{{< /spoiler >}}