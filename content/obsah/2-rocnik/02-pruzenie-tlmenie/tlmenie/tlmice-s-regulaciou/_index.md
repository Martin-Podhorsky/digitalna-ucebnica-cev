---
linkTitle: "11.7.2 Tlmiče s reguláciou"
title: "Tlmiče s reguláciou"
type: docs
weight: 2
sidebar:
  open: false
---

Moderné automobily často používajú tlmiče s možnosťou regulácie tlmiaceho účinku. Tieto systémy umožňujú prispôsobiť charakteristiku tlmenia aktuálnym jazdným podmienkam, čím zlepšujú komfort aj bezpečnosť jazdy.

## Typy regulácie tlmenia

### 1. Manuálna regulácia

Najjednoduchší typ regulácie, kde vodič alebo mechanik môže mechanicky nastaviť tvrdosť tlmenia pomocou nastavovacieho prvku (skrutka, otočný regulátor). Nastavenie sa vykonáva pri stojiacom vozidle a zostáva nemenné počas jazdy.

**Princíp činnosti:** Otáčaním regulátora sa mení prierez prietokového kanála v tlmiči, čím sa ovplyvňuje rýchlosť prúdenia oleja a tým aj tvrdosť tlmenia.

**Použitie:** Športové vozidlá, vozidlá pre motorsport, aftermarket úpravy.

### 2. Poloautomatická regulácia

Vodič môže počas jazdy prepínať medzi niekoľkými prednastavenými režimami tlmenia (napr. Comfort, Normal, Sport) pomocou tlačidla v kabíne. Systém následne upraví tlmenie na všetkých kolesách.

**Princíp činnosti:** Elektromagnetické ventily v tlmičoch menia prierez prietokových kanálov podľa zvoleného režimu. Riadiaca jednotka aktivuje príslušné ventily na základe voľby vodiča.

**Použitie:** Stredná a vyššia trieda vozidiel s voliteľným športovým podvozkom.

### 3. Aktívne (adaptívne) tlmenie

Riadiaca jednotka automaticky a nepretržite upravuje tlmenie každého kolesa nezávisle na základe údajov zo senzorov. Systém reaguje na aktuálne jazdné podmienky v reálnom čase (niekoľkokrát za sekundu).

**Princíp činnosti:** Snímače monitorujú pohyby karosérie, rýchlosť vozidla, uhol natočenia volantu, polohu plynového a brzdového pedálu. Riadiaca jednotka vyhodnocuje tieto údaje a okamžite upravuje tlmenie pomocou rýchlych elektromagnetických ventilov alebo magnetoreologickej kvapaliny.

**Použitie:** Luxusné vozidlá, športové vozidlá, SUV vyššej triedy.

## Technológie adaptívneho tlmenia

### Tlmiče s elektromagnetickými ventilmi (solenoidové)

**Hlavné časti:**
1. Teleskopický tlmič (zvyčajne jednoplášťový)
2. Elektromagnetický (solenoidový) ventil
3. Riadiaca jednotka
4. Snímače (výšky, zrýchlenia, rýchlosti)

**Princíp činnosti:**

Elektromagnetický ventil je umiestnený v pieste tlmiča alebo v jeho tele. Prúd prechádzajúci cievkou ventilu vytvára magnetické pole, ktoré ovláda polohu ihly alebo klapky ventilu. Zmenou prúdu sa mení prierez prietokového otvoru:
- **Väčší prúd** = menší prierez = tvrdšie tlmenie
- **Menší prúd** = väčší prierez = mäkšie tlmenie

Výhodou je rýchla odozva (niekoľko milisekúnd) a možnosť plynulej regulácie v širokom rozsahu.

### Magnetoreologické tlmiče (MagneRide)

{{< figure src="magneride.webp" alt="Magnetoreologický tlmič MagneRide" width="70%" caption="Obr. 11.26 - Magnetoreologický tlmič MagneRide" >}}

**Hlavné časti:**
1. Jednoplášťový tlmič
2. Magnetoreologická kvapalina (olej s kovovými časticami)
3. Elektromagnetické cievky v pieste
4. Riadiaca jednotka
5. Snímače

**Princíp činnosti:**

Magnetoreologická kvapalina obsahuje mikroskopické kovové častice (železný prášok) rozptýlené v syntetickom oleji. V normálnom stave sa častice voľne pohybujú a kvapalina má nízku viskozitu.

Keď elektromagnetická cievka v pieste vytvorí magnetické pole, kovové častice sa zoradia do reťazcov v smere magnetických siločiar. Tieto reťazce vytvárajú odpor proti prúdeniu kvapaliny, čím sa zvyšuje jej zdanlivá viskozita a tým aj tlmiaca sila.

- **Bez magnetického poľa** = nízka viskozita = mäkké tlmenie
- **Silné magnetické pole** = vysoká viskozita = tvrdé tlmenie

**Výhody magnetoreologických tlmičov:**
- Extrémne rýchla odozva (menej ako 1 milisekunda)
- Žiadne mechanické ventily = vyššia spoľahlivosť
- Plynulá regulácia v širokom rozsahu
- Tichá prevádzka

**Nevýhody magnetoreologických tlmičov:**
- Vysoká cena kvapaliny aj tlmičov
- Špeciálna kvapalina vyžaduje pravidelnú výmenu
- Náročná výroba a údržba

## Príklady systémov adaptívneho tlmenia

| Výrobca | Názov systému | Technológia |
| --- | --- | --- |
| Opel, GM | CDC (Continuous Damping Control) | Solenoidové ventily |
| VW, Audi, Škoda | DCC (Dynamic Chassis Control) | Solenoidové ventily |
| Audi, Cadillac, Ferrari, Corvette | MagneRide | Magnetoreologická kvapalina |
| Mercedes-Benz | ADS (Adaptive Damping System) | Solenoidové ventily |
| Porsche | PASM (Porsche Active Suspension Management) | Solenoidové ventily |
| BMW | Adaptive M Suspension | Solenoidové ventily |
| Volvo | Four-C (Continuously Controlled Chassis Concept) | Solenoidové ventily |

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="/obsah/2-rocnik/03-riadenie/" title="Riadenie" subtitle="Spôsoby riadenia, mechanizmus riadenia, hlavné časti, geometria riadenia...">}}
{{< /cards >}}

---

{{< spoiler text="Zdroje" >}}
- FAKTOR, I., 2003, Cestné vozidlá II. Bratislava: EXPOL PEDAGOGIKA. ISBN 978-80-8091-351-9.
- ZF Friedrichshafen AG – Systematic Damping: https://www.zf.com/products/en/cars/stories/systematic_damping.html
- BWI Group – MagneRide Technology: https://www.bwigroup.com/products/magneride
- Audi Technology Portal – Adaptive Damping: https://www.audi-technology-portal.de/en/chassis/suspension-control-systems
- Porsche – PASM Technical Information: https://www.porsche.com/international/models/911/911-carrera-models/chassis/
- Volkswagen – DCC Dynamic Chassis Control: https://www.volkswagen.co.uk/en/technology/chassis.html
- Capital One – What Are Adaptive Dampers: https://www.capitalone.com/cars/learn/finding-the-right-car/what-are-adaptive-dampers-in-your-car/
- ISC Suspension – Monotube vs Twin Tube: https://iscsuspension-na.com/resources/informative-articles/monotube-vs-twin-tube-what-is-the-difference-what-is-better/
- Shock Absorber Pro – Adjustable vs Non-Adjustable: https://shockabsorberpro.com/adjustable-vs-non-adjustable/
{{< /spoiler >}}
