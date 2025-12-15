---
title: "Geometria riadenia kolies"
type: docs
weight: 3
sidebar:
  open: false
---

Geometria riadenia je súbor parametrov, ktoré určujú postavenie kolies voči vozovke, rámu vozidla a voči sebe navzájom.

Správne nastavená geometria kolies:
- Zaisťuje pravidelné odvaľovanie kolies po vozovke (bez šmýkania)
- Znižuje opotrebenie pneumatík a spotrebu paliva
- Zaisťuje správnu smerovú stabilitu (jazda v priamom smere)
- Zabraňuje kmitaniu (rozkmitaniu) kolies
- Samovoľne vracia kolesá do priameho smeru po vychýlení (zo zákruty)
- Zlepšuje ovládateľnosť vozidla

Geometriu tvoria tieto hlavné parametre:
1. Zbiehavosť alebo rozbiehavosť kolies ($\delta$)
2. Odklon/príklon kolesa ($\alpha$)
3. Príklon osi riadenia ($\gamma$)
4. Záklon osi riadenia ($\beta$)
5. Závlek kolesa ($n_k$)
6. Polomer riadenia ($r_0$)
7. Rozchod kolies
8. Rázvor náprav
9. Diferenčný uhol (Ackermannova podmienka)

---

### Zbiehavosť a rozbiehavosť kolies

Zbiehavosť je stav, kedy sú predné časti kolies jednej nápravy k sebe bližšie ako zadné časti (pri pohľade zhora). Rozbiehavosť je opačný stav (kolesá sú "otvorené" von).

{{< figure src="toe-in-toe-out.png" alt="Zbiehavosť a rozbiehavosť kolies" width="45%" caption="Obr. 12.X - Zbiehavosť a rozbiehavosť kolies" >}}

**Vlastnosti a vplyv:**
- **Zbiehavosť (Toe-in):**
  - Zlepšuje smerovú stabilitu pri jazde v priamom smere (kolesá sa snažia "ísť k sebe", čo stabilizuje vozidlo).
  - Kompenzuje vôle v riadení a silách, ktoré pri jazde tlačia kolesá do rozbiehavosti (najmä pri zadnom náhone).
  - Príliš veľká zbiehavosť spôsobuje opotrebenie vonkajších hrán pneumatík.
- **Rozbiehavosť (Toe-out):**
  - Zlepšuje reakciu vozidla pri nájazde do zákruty (ochota zatáčať).
  - Bežná u pretekárskych áut alebo na prednej náprave áut s predným náhonom (kde ťah motora sťahuje kolesá do zbiehavosti).
  - Príliš veľká rozbiehavosť spôsobuje nestabilitu v priamom smere a opotrebenie vnútorných hrán pneumatík.

### Odklon/príklon kolesa ($\alpha$)

Odklon kolesa (Camber) je uhol, ktorý zviera rovina kolesa so zvislicou pri pohľade spredu alebo zozadu.

{{< figure src="odklon-priklon.jpg" alt="Odklon/príklon kolesa ($\alpha$)" width="45%" caption="Obr. 12.X - Odklon/príklon kolesa ($\alpha$)" >}}

- **Negatívny odklon (príklon / Negative Camber):** Vrch kolesa smeruje dovnútra.
  - Zvyšuje priľnavosť v zákrutách (pretože pri náklone karosérie sa vonkajšie zaťažené koleso dostane do kolmej polohy voči vozovke a má väčšiu styčnú plochu).
  - Štandard pre moderné osobné a športové autá.
  - Príliš veľký negatívny odklon zhoršuje brzdnú dráhu a akceleráciu v priamom smere a ničí vnútornú stranu pneumatík.
- **Pozitívny odklon (odklon / Positive Camber):** Vrch kolesa smeruje von.
  - Používal sa pri starších vozidlách a nákladných autách na zníženie sily potrebnej na riadenie.
  - Pri zaťažení vozidla nákladom sa kolesá vyrovnajú do nuly.

### Príklon osi riadenia ($\gamma$)

Príklon osi riadenia (Kingpin Inclination - KPI / SAI) je uhol medzi osou čapu riadenia (os okolo ktorej sa koleso otáča pri riadení) a zvislicou pri pohľade spredu.

{{< figure src="priklon-osi-riadenia.jpg" alt="Príklon osi riadenia ($\gamma$)" width="45%" caption="Obr. 12.X - Príklon osi riadenia ($\gamma$)" >}}

**Funkcia:**
- Pomáha vracať kolesá do priameho smeru (pri zatočení sa vďaka tomuto uhlu predná časť vozidla mierne nadvihne, a váha vozidla sa snaží vrátiť kolesá späť, aby auto "kleslo").
- Znižuje polomer riadenia (viď nižšie).
- Hodnota býva v rozmedzí 5° až 15°.

### Záklon osi riadenia ($\delta$)

Záklon osi riadenia (Caster) je uhol medzi osou čapu riadenia a zvislicou pri pohľade zboku vozidla.

{{< figure src="záklon-osi-riadenia.png" alt="Príklon osi riadenia ($\gamma$)" width="40%" caption="Obr. 12.X - Záklon osi riadenia ($\delta$)" >}}

- **Pozitívny záklon:** Os čapu je naklonená dozadu (horný bod je viac vzadu ako spodný).
  - Bod, okolo ktorého sa koleso otáča, je pred bodom dotyku pneumatiky s vozovkou.
  - Vytvára tzv. **vlečný efekt** (ako kolieska na nákupnom vozíku), čo kolesá stabilizuje.
  - **Hlavný prvok pre smerovú stabilitu** a vracanie volantu.
  - Zvyšuje silu potrebnú na zatočenie volantom.

### Závlek kolesa ($n_k$)

Závlek (Mechanical Trail) je vzdialenosť na vozovke medzi predĺženou osou riadenia a stredom dotykovej plochy pneumatiky.

- Je priamym dôsledkom záklonu osi riadenia (Caster).
- Práve na ramene tejto vzdialenosti pôsobia bočné sily, ktoré vytvárajú "samo-zrovnávací moment" vracajúci volant do stredu.
- Väčší závlek = lepšia stabilita, ale ťažšie riadenie.

{{< figure src="závlek-kolesa.png" alt="Závlek kolesa ($n_k$)" width="40%" caption="Obr. 12.X - Závlek kolesa ($n_k$)" >}}

### Polomer riadenia ($r_0$)

Polomer riadenia (Scrub Radius) je vzdialenosť medzi stredom odtlačku pneumatiky a priesečníkom osi riadenia s vozovkou.

{{< figure src="polomer-riadenia.jpg" alt="Polomer riadenia ($r_0$)" width="85%" caption="Obr. 12.X - Polomer riadenia ($r_0$)" >}}

- **Pozitívny polomer:** Os riadenia pretína vozovku *vnútri* od stredu pneumatiky.
  - Poskytuje dobrú spätnú väzbu do volantu (vodič cíti povrch).
  - Nevýhoda: Pri nerovnostiach alebo defekte môže volant "kopnúť" alebo sa vytrhnúť z ruky.
- **Negatívny polomer:** Os riadenia pretína vozovku *vonku* od stredu pneumatiky.
  - **Bezpečnejší pre moderné autá.**
  - Pri brzdení na povrchu s rôznou priľnavosťou (napr. ľad na jednej strane) alebo pri výpadku jedného brzdového okruhu auto automaticky kontra-uje a udržuje priamy smer.
  - Bežný u áut s predným náhonom a ABS.
- **Nulový polomer:** Os pretína stred pneumatiky.
  - Koleso sa na mieste len točí okolo stredu (neodvaľuje sa), čo spôsobuje veľké trenie a namáhanie čapov (tzv. "drhnutie" - scrub).

### Diferenčný uhol (Ackermannova geometria)

Pri prejazde zákrutou musí vnútorné koleso opísať menší polomer ako vonkajšie koleso. Preto musí byť **vnútorné koleso natočené viac** ako vonkajšie.

{{< figure src="diferencny-uhol.jpg" alt="Diferenčný uhol (Ackermannova geometria)" width="80%" caption="Obr. 12.X - Diferenčný uhol (Ackermannova geometria)" >}}

- Ak by boli kolesá natočené rovnako, jedno z nich by sa muselo šmýkať, čo by zhoršilo ovládateľnosť a ničilo pneumatiky.
- Tento rozdiel uhlov sa nazýva **diferenčný uhol**.
- Dosahuje sa lichobežníkovou konštrukciou riadiaceho mechanizmu (spojovacie tyče a páky riadenia netvoria obdĺžnik, ale lichobežník).

### Rozchod kolies

- Vzdialenosť medzi stredmi pneumatík na jednej náprave.
- Širší rozchod zvyšuje stabilitu proti prevráteniu v zákrutách.

{{< figure src="rozchod.jpg" alt="Rozchod kolies" width="50%" caption="Obr. 12.X - Rozchod kolies" >}}

### Rázvor náprav

- Vzdialenosť medzi stredmi predných a zadných kolies.
- **Dlhý rázvor:** Lepšia smerová stabilita, viac miesta pre posádku, ale väčší polomer otáčania (horšia manévrovateľnosť v meste).
- **Krátky rázvor:** Auto je "hravejšie", ochotnejšie zatáča, ale menej stabilné pri vysokej rýchlosti.

{{< figure src="razvor.jpg" alt="Rázvor náprav" width="70%" caption="Obr. 12.X - Rázvor náprav" >}}