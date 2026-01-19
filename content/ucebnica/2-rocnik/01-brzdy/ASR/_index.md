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

ASR pracuje v úzkej súčinnosti so systémom ABS a riadiacou jednotkou motora. Systém využíva tie isté snímače otáčok kolies ako ABS, ktoré neustále monitorujú rýchlosť otáčania každého kolesa.

Keď riadiaca jednotka zaznamená, že sa niektoré z hnacích kolies otáča výrazne rýchlejšie, ako je rýchlosť vozidla, systém vyhodnotí túto situáciu ako preklz a okamžite aktivuje reguláciu.

### Metódy regulácie:

ASR zabraňuje preklzu hnacích kolies dvoma hlavnými spôsobmi:

#### 1. Zníženie výkonu motora
- Znížením dávky paliva alebo dočasním vypnutím vstrekovania do niektorých valcov
- Oneskorením iskry alebo jej vynechávaním v niektorých valcoch (benzínové motory)
- Dočasným znížením prívodu vzduchu pomocou dodatočného prikrytia škrtiacej klapky (benzínové motory)

#### 2. Pribrzdenie preklzujúceho kolesa
- Automatickým aktivovaním ABS bez toho, aby sa vodič dotkol brzdového pedála

Vodič tento proces vníma ako krátkodobé obmedzenie výkonu a prípadne pulzovanie od podvozku. Na prístrojovej doske sa taktiež rozsvieti kontrolka ASR.

## Hlavné časti systému ASR

1 - **Snímače otáčok kolies** –- zdieľané so systémom ABS, merajú rýchlosť otáčania každého kolesa. <br>
2 - **Hydraulická riadiaca jednotka (HCU)** –- zdieľaná s ABS, reguluje brzdný tlak na jednotlivých kolesách. <br>
3 - **Elektronická riadiaca jednotka ASR** -– vyhodnocuje dáta zo snímačov a rozhoduje o spôsobe zásahu. <br>
4 - **Riadiaca jednotka motora** –- na pokyn od ASR znižuje výkon motora.

## Výhody:

- **Zlepšená trakcia** -- zabraňuje prešmykovaniu kolies pri zrýchľovaní na klzkom povrchu.
- **Kratšia dráha zrýchlenia** -- systém zabezpečuje optimálny prenos krútiaceho momentu od kolies na vozovku.
- **Znížené opotrebenie pneumatík** -- zabránením preklzu sa znižuje nerovnomerné opotrebenie.
- **Ochrana pohonného ústrojenstva** -- znižuje sa zaťaženie diferenciálu a prevodovky.
- **Lepšia ovládateľnosť v zákrutách** -- zabraňuje šmyku pri akcelerácii v zákrute.

## Nevýhody:

- **Problém v určitých podmienkach** -- v snehu, blate, štrku alebo na ľade ASR viac škodí ako pomáha a je potrebné ho vypnúť
- **Pocit zásahu do ovládania** - niektorí vodiči vnímajú aktiváciu ASR ako rušivú

## MSR - Regulácia brzdného momentu motora

MSR (Motor Schleppmoment Regelung) je doplnková funkcia systému ASR, ktorá rieši opačný problém - zablokovanie hnacích kolies pri brzdení motorom.

### Princíp činnosti:

Pri prudkom znížení otáčok motora (napríklad pri radení na nižší prevod na klzkom povrchu) môže brzdný účinok motora spôsobiť zablokovanie hnacích kolies. MSR tomuto zabráňuje tým, že:
- Zvýši otáčky motora (pootvorí škrtiacu klapku)
- Alebo zníži brzdný účinok kontrolovaným pribrzdením predných nehnaných kolies

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="FDR" title="Elektronická kontrola stability (ESP/FDR)" subtitle="Princíp činnosti, Konštrukcia, výhody, nevýhody...">}}
{{< /cards >}}

---

{{< spoiler text="Zdroje" >}}
- FAKTOR, I., 2003, Cestné vozidlá II. Bratislava: EXPOL PEDAGOGIKA. ISBN 978-80-8091-351-9.
- https://www.holtsauto.com/blog/what-is-asr-on-a-car-anti-slip-regulation-explained/
{{< /spoiler >}}