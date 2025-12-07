---
title: "Elektronická kontrola stability (ESP/FDR)"
weight: 7
type: docs
sidebar:
  open: false
---

FDR (Fahrdynamikregelung) alebo ESP (Electronic Stability Program) je najkomplexnejší elektronický bezpečnostný systém na zabezpečenie stability vozidla. Kombinuje funkcie ABS, ASR, MSR a pridáva aktívnu kontrolu stability v zákrutách. Systém dokáže rozpoznať a korigovať nebezpečné jazdné situácie skôr, než vodič stihne zareagovat.

{image of ESP/FDR system}

## Princíp činnosti

Systém FDR nepretržite monitoruje a vyhodnocuje kľúčové parametre jazdy:
- **Uhol natočenia volantu** - kam chce vodič smerovať
- **Rýchlosť vozidla** - aktuálna rýchlosť pohybu
- **Priečne zrýchlenie** - bočné sily pôsobiace na vozidlo
- **Uhlovú rýchlosť otáčania** - ako rýchlo sa vozidlo otáča okolo zvislej osi
- **Otáčky všetkých kolies** - skutočný pohyb vozidla

Riadiaca jednotka porovnáva zámer vodiča (uhol natočenia volantu) so skutočným správaním vozidla (snímače). Ak zistí rozdiel - vozidlo reaguje inak, než vodič očakáva - systém okamžite zasahuje.

### Spôsob zásahu:

Keď FDR deteguje nestabilitu, automaticky:
1. **Pribrzdi vybrané koleso/kolesá** - selektívnym brzdením jednotlivých kolies koriguje smer jazdy
2. **Zníži výkon motora** - obmedzí prívod paliva alebo oneskorí zápel
3. **Stabilizuje trajektóriu vozidla** - vráti vozidlo na požadovanú dráhu

#### Situácie, kedy FDR zasahuje:

**Pretáčavosť (oversteer)**
- systém pribrzdi predné vonkajšie koleso

**Nedotáčavosť (understeer)**
- systém pribrzdi zadné vnútorné koleso

**Preklz pri rozjazde**
- Aktivuje sa funkcia ASR

**Blokovanie pri brzdení**
- Aktivuje sa funkcia ABS

## Hlavné časti systému FDR/ESP

1. **Všetky komponenty ABS a ASR** - snímače otáčok kolies, hydraulická jednotka, riadiaca jednotka
2. **Snímač uhla natočenia volantu** - meria, kam vodič chce smerovať
3. **Snímač priečneho zrýchlenia** - meria bočné G-sily pôsobiace na vozidlo
4. **Snímač uhlovej rýchlosti (gyroskop)** - meria rýchlosť otáčania vozidla okolo zvislej osi
5. **Hydraulická jednotka s pumpou** - umožňuje aktívne brzdenie jednotlivých kolies bez stlačenia pedála
6. **Výkonná riadiaca jednotka** - vyhodnocuje všetky signály a riadi zásahy (až 25-krát za sekundu)
7. **Kontrolka ESP** - informuje vodiča o aktivácii alebo poruche systému
8. **Vypínač ESP** - umožňuje dočasné vypnutie systému

## Výhody:

- **Výrazné zvýšenie aktívnej bezpečnosti** - podľa štúdií znižuje riziko smrteľných nehôd až o 40%
- **Prevencia šmykov a prevrátenia** - najmä pri náhlych manévroch a v zákrutách
- **Účinné aj pre menej skúsených vodičov** - systém reaguje rýchlejšie než človek
- **Integrácia všetkých stabilizačných systémov** - ABS, ASR, MSR pracujú koordinovane
- **Štatisticky preukazné zníženie nehôd** - najmä jednostranných havárií a prevrátení
- **Pomoc pri vyhýbaní prekážkam** - umožňuje bezpečnejšie úhybné manévre

## Nevýhody:

- **Vyššie výrobné náklady** - pokročilé senzory a riadiace jednotky zvyšujú cenu vozidla
- **Zložitejšia konštrukcia** - viac komponentov znamená vyššiu komplexnosť systému
- **Nákladnejšia údržba a opravy** - diagnostika a oprava vyžaduje špecializované zariadenia
- **Možnosť falošnej aktivácie** - v extrémnych situáciách môže systém zasiahnuť nesprávne
- **Obmedzenie pri off-road jazde** - na štrku, piesku alebo v blate môže byť ESP kontraproduktívny
- **Pocit straty kontroly** - niektorí skúsení vodiči vnímajú zásahy ESP ako rušivé
- **Potreba vypnutia v špecifických situáciách** - pri jazde so snehovými reťazami, v hlbokom snehu alebo pri ťahaní uviaznutého vozidla
- **Závislosť od kalibrácie** - nesprávna kalibrácia môže viesť k nepresným zásahom

## Legislatíva

Systém FDR je v Európskej únii povinný od roku 2014 pre všetky nové osobné automobily a ľahké úžitkové vozidlá. Táto legislatíva bola zavedená na základe preukázaného prínosu systému k zníženiu počtu dopravných nehôd.

Nasledujúce učivo:
{{< cards >}}
  {{< card url="vzduchove-brzdy" title="Vzduchotlakové (strojové) brzdy" subtitle="Konštrukcia, vlastnosti, výhody, nevýhody...">}}
{{< /cards >}}