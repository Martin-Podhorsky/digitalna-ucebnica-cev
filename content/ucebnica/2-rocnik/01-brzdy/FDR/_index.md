---
linkTitle: "10.7 FDR"
title: "Elektronická kontrola stability (ESP/FDR)"
weight: 7
type: docs
sidebar:
  open: false
---

FDR (Fahrdynamikregelung) alebo ESP (Electronic Stability Program) je najkomplexnejší elektronický bezpečnostný systém, ktorý pomáha vodičovi udržať vozidlo pod kontrolou v zákrutách a pri prudkých manévroch.

{{< youtube WPEaJv3pduI >}}

## Princíp činnosti

Systém FDR nepretržite monitoruje a vyhodnocuje kľúčové parametre jazdy:
- **Uhol natočenia volantu**
- **Rýchlosť vozidla**
- **Priečne zrýchlenie vozidla** 
- **Uhlovú rýchlosť otáčania vozidla**
- **Otáčky všetkých kolies**

Riadiaca jednotka porovnáva zámer vodiča (uhol natočenia volantu) so skutočným správaním vozidla (snímače). Ak zistí rozdiel - vozidlo reaguje inak, než by vodič chcel - systém okamžite zasahuje.

### Spôsob zásahu:

Keď FDR detekuje nebezpečenstvo šmyku, automaticky:
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
2. **Snímač uhla natočenia volantu** -- dáva riadiace jednotke údaj o tom, kam chce vodič ísť
3. **Snímač priečneho zrýchlenia** --  dáva riadiace jednotke údaj o tom, či je vozidlo v šmyku
4. **Snímač uhlovej rýchlosti (gyroskop)** - meria rýchlosť otáčania vozidla okolo zvislej osi
5. **Výkonná riadiaca jednotka** -- spracováva údaje zo všetkých snímačov a rozhoduje o zásahu
6. **Kontrolka ESP** - informuje vodiča o aktivácii alebo poruche systému
7. **Vypínač ESP** - umožňuje dočasné vypnutie systému

## Výhody:

- **Štatisticky preukazné zníženie nehôd** - ESP dokáže zabrániť až 80% nehodám spôsobeným šmykom
- **Pomáha zabrániť šmyku alebo prevráteniu** - najmä pri náhlych manévroch
- **Účinné aj pri menej skúsených vodičoch** - systém reaguje rýchlejšie než človek
- **Zjednotenie všetkých asistenčných systémov** - ABS, ASR a MSR pracujú spoločne

## Nevýhody:

- **Vyššie výrobné náklady** - pokročilé senzory a riadiace jednotky zvyšujú cenu vozidla
- **Zložitejšia konštrukcia** - viac komponentov znamená vyššiu komplexnosť systému
- **Nákladnejšia údržba a opravy** - diagnostika a oprava vyžaduje špecializované zariadenia
- **Možnosť pochybenia** - v niektorých situáciách môže systém zasiahnuť nesprávne
- **Závislosť od správnej kalibrácie** - nesprávna kalibrácia môže viesť k nepresným zásahom

## Legislatíva

Systém FDR je v Európskej únii povinný od novembra 2011 pre nové modely vozidiel a od novembra 2014 pre všetky nové registrácie osobných automobilov a ľahkých úžitkových vozidiel. Táto legislatíva bola zavedená na základe preukázaného prínosu systému k zníženiu počtu dopravných nehôd.

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="vzduchove-brzdy" title="Vzduchotlakové (strojové) brzdy" subtitle="Konštrukcia, vlastnosti, výhody, nevýhody...">}}
{{< /cards >}}