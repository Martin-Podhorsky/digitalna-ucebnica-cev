---
linkTitle: "10.6 ASR"
title: "Regulácia preklzu kolies (ASR)"
weight: 6
type: docs
sidebar:
  open: false
---

ASR (Anti-Slip Regulation) alebo TCS (Traction Control System) je aktívny bezpečnostný systém, ktorý zabraňuje preklzu hnacích kolies pri rozjazde a akcelerácii.

{{< figure src="ASR.jpg" alt="Systém ASR" width="80%" caption="Obr. 10.18 - Systém ASR" >}}

## Princíp činnosti

ASR pracuje v úzkej súčinnosti so systémom ABS a riadiacou jednotkou motora (ECU). Systém využíva tie isté snímače otáčok kolies ako ABS, ktoré neustále monitorujú rýchlosť otáčania každého kolesa.

Keď riadiaca jednotka zistí, že niektoré z hnacích kolies sa otáča výrazne rýchlejšie než nehnané kolesá (alebo než druhé hnacie koleso), systém vyhodnotí túto situáciu ako preklz a okamžite aktivuje reguláciu.

### Metódy regulácie:

ASR zabraňuje preklzu hnacích kolies dvoma hlavnými spôsobmi:

#### 1. Zníženie výkonu motora (EMS)
- Znížením dávky paliva alebo dočasním vypnutím vstrekovania do niektorých valcov
- Oneskorením iskry alebo jej vynechávaním v niektorých valcoch (benzínové motory)
- Dočasným znížením prívodu vzduchu pomocou dodatočného prikrytia škrtiacej klapky (benzínové motory)

#### 2. Pribrzdenie preklzujúceho kolesa
- Automatickým aktivovaním ABS bez toho, aby sa vodič dotkol brzdového pedála

Vodič tento proces vníma ako krátkodobé obmedzenie výkonu a prípadne pulzovanie z podvozku. Na prístrojovej doske sa rozsvieti kontrolka ASR.

## Hlavné časti systému ASR

1 - **Snímače otáčok kolies** – zdieľané so systémom ABS, merajú rýchlosť otáčania každého kolesa. <br>
2 - **Hydraulická riadiaca jednotka (HCU)** – zdieľaná s ABS, reguluje brzdný tlak na jednotlivých kolesách. <br>
3 - **Elektronická riadiaca jednotka ASR (ECU)** – vyhodnocuje dáta zo snímačov a rozhoduje o spôsobe zásahu. <br>
4 - **Riadiaca jednotka motora (ECU motora)** – na pokyn od ASR znižuje výkon motora.

## Výhody:

- **Zlepšená trakcia** - zabraňuje prešmykovaniu kolies pri zrýchľovaní na klzkom povrchu
- **Zvýšená stabilita** - vozidlo zostáva stabilné a ovládateľné aj pri rozdielnej priľnavosti kolies
- **Kratšia dráha zrýchlenia** - optimálny prenos výkonu na vozovku
- **Znížené opotrebenie pneumatík** - zabránením preklzu sa znižuje nerovnomerné opotrebenie
- **Ochrana pohonného ústrojenstva** - minimalizuje zaťaženie diferenciálu a prevodovky
- **Lepšia ovládateľnosť v zákrutách** - zabraňuje šmyku pri akcelerácii v zatáčke

## Nevýhody:

- **Obmedzenie výkonu** - v niektorých situáciách môže ASR znížiť výkon, čo môže byť nevýhodné pri potrebe rýchleho zrýchlenia
- **Problémy v hlbokom snehu** - systém môže zabrániť "zakopaniu" kolies, čo niekedy pomáha pri rozjazde
- **Pocit zásahu do ovládania** - niektorí vodiči vnímajú aktiváciu ASR ako rušivú
- **Možnosť vypnutia potrebná** - v určitých podmienkach (hlboký sneh, blato, štrk) môže byť potrebné ASR vypnúť

## MSR - Regulácia brzdného momentu motora

MSR (Motor Schleppmoment Regelung) je doplnková funkcia systému ASR, ktorá rieši opačný problém - zablokovanie hnacích kolies pri brzdení motorom.

### Princíp činnosti:

Pri prudkom znížení otáčok motora (napríklad pri radení na nižší prevod na klzkom povrchu) môže brzdný účinok motora spôsobiť zablokovanie hnacích kolies. MSR tomuto zabráňuje tým, že:
- Zvýši otáčky motora (pootvorí škrtiacu klapku)
- Alebo zníži brzdný účinok kontrolovaným pribrzdením predných nehnacích kolies

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="FDR" title="Elektronická kontrola stability (ESP/FDR)" subtitle="Princíp činnosti, Konštrukcia, výhody, nevýhody...">}}
{{< /cards >}}