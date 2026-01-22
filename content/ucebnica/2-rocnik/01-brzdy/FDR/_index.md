---
linkTitle: "10.7 FDR"
title: "Elektronická kontrola stability (ESP/FDR)"
weight: 7
type: docs
sidebar:
  open: false
---

FDR (Fahrdynamikregelung) alebo ESP (Electronic Stability Program) je komplexný elektronický bezpečnostný systém, ktorý pomáha vodičovi udržať vozidlo pod kontrolou v zákrutách a pri prudkých zmenách smeru vo vysokých rýchlostiach.

{{< youtube WPEaJv3pduI >}}

## Princíp činnosti

Systém FDR nepretržite monitoruje a vyhodnocuje kľúčové parametre jazdy:
- **Uhol natočenia volantu**
- **Rýchlosť vozidla**
- **Priečne zrýchlenie vozidla** 
- **Uhlovú rýchlosť otáčania vozidla**
- **Otáčky všetkých kolies**

Riadiaca jednotka porovnáva zámer vodiča (uhol natočenia volantu) so skutočným správaním vozidla (ostatné snímače). Ak zistí rozdiel - skutočný smer pohybu vozidla nie je totožný s uhlom natočenia volantu  - systém okamžite zasahuje.

### Spôsob zásahu:

Keď FDR detekuje nebezpečenstvo, automaticky:
1. **Pribrzdi vybrané koleso/kolesá** - selektívnym brzdením jednotlivých kolies koriguje smer jazdy
2. **Zníži výkon motora** - obmedzí prívod paliva alebo oneskorí zápal

### Situácie, kedy FDR zasahuje:

**Pretáčavosť (oversteer)**
- systém pribrzdi predné vonkajšie koleso

**Nedotáčavosť (understeer)**
- systém pribrzdi zadné vnútorné koleso

**Preklz pri rozjazde**
- Aktivuje sa funkcia ASR

**Blokovanie pri brzdení**
- Aktivuje sa funkcia ABS

## Hlavné časti systému FDR/ESP

1. **Všetky komponenty ABS a ASR** -- snímače otáčok kolies, hydraulická riadiaca jednotka, riadiaca jednotka motora
2. **Snímač uhla natočenia volantu** -- dáva riadiacej jednotke údaj o požadovanom smere jazdy
3. **Snímač priečneho zrýchlenia** --  dáva riadiacej jednotke údaj o tom, či je vozidlo v šmyku
4. **Snímač uhlovej rýchlosti (gyroskop)** -- meria rýchlosť otáčania vozidla okolo zvislej osi
5. **Výkonná riadiaca jednotka** -- spracováva údaje zo všetkých snímačov a rozhoduje o zásahu
6. **Kontrolka ESP** -- informuje vodiča o aktivácii systému alebo jeho poruche
7. **Vypínač ESP** -- umožňuje dočasné vypnutie systému

## Výhody:

- **Štatisticky preukazné zníženie nehôd** -- ESP dokáže zabrániť až 80% nehodám spôsobeným šmykom.
- **Zjednotenie všetkých asistenčných systémov** -- ABS, ASR a MSR pracujú spoločne a synchronizovane

## Nevýhody:

- **Vyššie výrobné náklady** -- pokročilé senzory a riadiace jednotky zvyšujú cenu vozidla
- **Zložitejšia konštrukcia** -- viac komponentov znamená vyššiu komplexitu systému
- **Nákladnejšia údržba a opravy** -- diagnostika a oprava vyžaduje špecializované zariadenia

## Legislatíva

Systém FDR je v Európskej únii povinný od novembra 2011 pre nové modely vozidiel a od novembra 2014 pre všetky nové registrácie osobných automobilov a ľahkých úžitkových vozidiel. Táto legislatíva bola zavedená na základe preukázaného prínosu systému k zníženiu počtu dopravných nehôd.

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="/ucebnica/2-rocnik/01-brzdy/vzduchove-brzdy" title="Vzduchotlakové (strojové) brzdy" subtitle="Konštrukcia, vlastnosti, výhody, nevýhody...">}}
{{< /cards >}}

---

{{< spoiler text="Zdroje" >}}
- FAKTOR, I., 2003, Cestné vozidlá II. Bratislava: EXPOL PEDAGOGIKA. ISBN 978-80-8091-351-9.
{{< /spoiler >}}