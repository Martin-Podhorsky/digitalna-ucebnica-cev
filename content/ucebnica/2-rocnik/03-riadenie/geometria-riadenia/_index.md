---
linkTitle: "12.3 Geometria riadenia kolies"
title: "Geometria riadenia kolies"
type: docs
weight: 3
sidebar:
  open: false
---

Geometria riadenia je súbor uhlov a rozmerov, ktoré určujú polohu kolies voči vozovke a karosérii vozidla. Tieto parametre majú zásadný vplyv na jazdné vlastnosti, opotrebovanie pneumatík a bezpečnosť jazdy.

Správne nastavená geometria kolies zabezpečuje:
- Rovnomerné odvaľovanie pneumatík po vozovke bez bočného šmyku, čím sa predlžuje ich životnosť a znižuje spotreba paliva
- Stabilitu vozidla v priamom smere
- Samovoľné vracanie kolies do priameho smeru po prejazde zákrutou

**Hlavné parametre:**
1. Zbiehavosť alebo rozbiehavosť kolies ($\delta$)
2. Odklon kolesa ($\alpha$)
3. Príklon osi riadenia ($\sigma$)
4. Záklon osi riadenia ($\tau$)
5. Závlek kolesa ($n_k$)
6. Polomer riadenia ($r_0$)
7. Rozchod kolies
8. Rázvor náprav
9. Diferenčný uhol (Ackermannova geometria)

---

## Zbiehavosť alebo rozbiehavosť kolies

Zbiehavosť alebo rozbiehavosť kolies je rozdiel vzdialeností medzi prednými a zadnými časťami kolies na jednej náprave, meraný v horizontálnej rovine.

- **Zbiehavosť (toe-in):** Predné časti kolies sú k sebe bližšie ako zadné časti
- **Rozbiehavosť (toe-out):** Zadné časti kolies sú k sebe bližšie ako predné časti

{{< figure src="toe-in-toe-out.png" alt="Zbiehavosť a rozbiehavosť kolies" width="45%" caption="Obr. 12.14 - Zbiehavosť a rozbiehavosť kolies" >}}

### Vplyv

**Zbiehavosť (toe-in):**
- Zlepšuje stabilitu vozidla v priamom smere jazdy
- Kompenzuje tendenciu kolies k rozbiehavosti vplyvom valivého odporu a síl pôsobiacich počas jazdy
- Pri nadmernej zbiehavosti dochádza k zvýšenému opotrebovaniu vonkajších hrán pneumatík
- Typická hodnota: 0 až 3 mm (celková zbiehavosť oboch kolies)

**Rozbiehavosť (toe-out):**
- Zlepšuje reakciu vozidla pri zatáčaní
- Používa sa predovšetkým na športových a pretekárskych vozidlách
- Pri nadmernej rozbiehavosti je vozidlo nestabilné v priamom smere a dochádza k opotrebovaniu vnútorných hrán pneumatík

**Poznámka:** Zadná náprava má zvyčajne miernu zbiehavosť pre lepšiu stabilitu. Rozbiehavosť na zadnej náprave spôsobuje nestabilitu (pretáčavosť).

## Odklon kolesa

Odklon kolesa (camber) je uhol medzi rovinou kolesa a zvislicou, meraný pri pohľade spredu alebo zozadu na vozidlo.

- **Pozitívny odklon:** Horná časť kolesa je naklonená von od vozidla
- **Negatívny odklon (príklon):** Horná časť kolesa je naklonená dovnútra k vozidlu

{{< figure src="odklon-priklon.jpg" alt="Odklon kolesa ($\alpha$)" width="45%" caption="Obr. 12.15 - Odklon kolesa ($\alpha$)" >}}

Odklon kolesa spôsobuje vznik axiálnej sily, ktorá pôsobí na ložiská kolies a vymedzuje v nich vôľu. Táto sila tiež bráni nežiaducemu kmitaniu kolies.

### Vplyv

**Negatívny odklon (príklon):**
- Zlepšuje priľnavosť pneumatík v zákrutách, pretože pri náklone karosérie sa vonkajšie koleso (nesúce väčšinu zaťaženia) vyrovná a pneumatika má väčšiu styčnú plochu s vozovkou
- Pri nadmernom negatívnom odklone sa pneumatika v priamom smere dotýka vozovky len vnútornou hranou, čo zhoršuje brzdenie, akceleráciu a spôsobuje rýchle opotrebovanie vnútornej strany pneumatiky
- Typická hodnota pre športové vozidlá: -0,5° až -2°

**Pozitívny odklon:**
- Historicky sa používal na vozidlách bez posilňovača riadenia, pretože znižoval silu potrebnú na otáčanie volantom
- Pri naložení vozidla sa kolesá pod váhou vyrovnajú do zvislej polohy
- Pri nadmernom pozitívnom odklone dochádza k opotrebovaniu vonkajšej hrany pneumatiky

## Príklon osi riadenia

Príklon osi riadenia (SAI - Steering Axis Inclination, tiež KPI - Kingpin Inclination) je uhol medzi osou otáčania kolesa pri riadení a zvislicou, meraný pri pohľade spredu na vozidlo. Os riadenia je naklonená tak, že jej horná časť smeruje k pozdĺžnej osi vozidla.

{{< figure src="priklon-osi-riadenia.png" alt="Príklon osi riadenia ($\sigma$)" width="100%" caption="Obr. 12.16 - Príklon osi riadenia ($\sigma$)" >}}

### Vplyv

- Zabezpečuje samovoľné vracanie kolies do priameho smeru po vychýlení, pretože pri natočení kolesa dochádza k miernemu zdvihnutiu prednej časti vozidla, ktoré sa vplyvom gravitácie snaží vrátiť do pôvodnej polohy
- Zmenšuje polomer riadenia, čím sa znižuje namáhanie riadiacich komponentov
- Spolu s odkonom kolesa vytvára tzv. zahrnutý uhol (included angle), ktorý ovplyvňuje stabilitu a opotrebovanie pneumatík
- Typická hodnota: 5° až 15°

## Záklon osi riadenia

Záklon osi riadenia (caster) je uhol medzi osou otáčania kolesa pri riadení a zvislicou, meraný pri pohľade zboku na vozidlo.

- **Pozitívny záklon:** Horná časť osi riadenia je naklonená dozadu (smerom k zadnej časti vozidla)
- **Negatívny záklon:** Horná časť osi riadenia je naklonená dopredu

{{< figure src="záklon-osi-riadenia.png" alt="Záklon osi riadenia ($\tau$)" width="40%" caption="Obr. 12.17 - Záklon osi riadenia ($\tau$)" >}}

### Vplyv

- Pozitívny záklon je hlavným faktorom zabezpečujúcim samovoľné vracanie kolies do priameho smeru po vychýlení (podobne ako u nákupného vozíka, kde sa kolieska vždy natočia v smere pohybu)
- Zvyšuje stabilitu vozidla pri vyšších rýchlostiach
- Väčší záklon znamená stabilnejšiu jazdu, ale zároveň vyžaduje väčšiu silu na otáčanie volantom
- Nesymetrický záklon (rozdielny na ľavej a pravej strane) spôsobuje ťahanie vozidla do strany
- Typická hodnota pre moderné vozidlá: +3° až +8°

## Závlek kolesa

Závlek kolesa je vzdialenosť medzi bodom, kde predĺžená os riadenia pretína vozovku, a stredom dotykovej plochy pneumatiky, meraná v pozdĺžnom smere vozidla.

{{< figure src="závlek-kolesa.png" alt="Závlek kolesa ($n_k$)" width="40%" caption="Obr. 12.18 - Závlek kolesa ($n_k$)" >}}

### Vplyv

- Závlek je priamym dôsledkom záklonu osi riadenia
- Vytvára stabilizačný moment, ktorý vracia koleso do priameho smeru (stred kontaktnej plochy pneumatiky je "ťahaný" za osou riadenia, podobne ako koliesko nákupného vozíka)
- Väčší závlek znamená väčšiu stabilitu, ale aj väčšiu silu potrebnú na riadenie
- Typická hodnota: 10 až 40 mm

## Polomer riadenia

Polomer riadenia (scrub radius) je vzdialenosť medzi bodom, kde predĺžená os riadenia pretína vozovku, a stredom dotykovej plochy pneumatiky, meraná v priečnom smere vozidla.

{{< figure src="polomer-riadenia.jpg" alt="Polomer riadenia ($r_0$)" width="85%" caption="Obr. 12.19 - Polomer riadenia ($r_0$)" >}}

### Vplyv

**Pozitívny polomer** (os pretína vozovku bližšie k stredu vozidla ako stred pneumatiky):
- Poskytuje lepšiu spätnú väzbu z vozovky cez volant
- Pri náraze do prekážky alebo defekte pneumatiky môže dôjsť k prudkému vytrhnutiu volantu z rúk
- Uľahčuje otáčanie volantom pri státí, pretože koleso sa pri natáčaní mierne odvaľuje
- Pri vozidlách s predným náhonom zosilňuje nežiaduce sily v riadení pri akcelerácii (tzv. torque steer)

**Negatívny polomer** (os pretína vozovku ďalej od stredu vozidla ako stred pneumatiky):
- Znižuje spätnú väzbu z vozovky
- Pri rozdielnej intenzite brzdenia ľavého a pravého kolesa (napr. na povrchu s rozdielnou priľnavosťou) automaticky kompenzuje ťahanie vozidla do strany
- Minimalizuje nežiaduce sily v riadení pri akcelerácii vozidiel s predným náhonom
- Je štandardom pre moderné vozidlá s predným náhonom a systémom ABS

**Nulový polomer** (os pretína presne stred kontaktnej plochy pneumatiky):
- Minimálna spätná väzba z vozovky
- Sťažené otáčanie volantom pri státí, pretože pneumatika sa otáča okolo jedného bodu
- Chýba stabilizačný účinok pri brzdení

## Diferenčný uhol (Ackermannova geometria)

Diferenčný uhol je rozdiel medzi uhlom natočenia vnútorného a vonkajšieho kolesa pri prejazde zákrutou. Vnútorné koleso musí byť natočené o väčší uhol ako vonkajšie, pretože opisuje oblúk s menším polomerom.

{{< figure src="diferencny-uhol.jpg" alt="Diferenčný uhol (Ackermannova geometria)" width="80%" caption="Obr. 12.20 - Diferenčný uhol (Ackermannova geometria)" >}}

### Vplyv

- Správny diferenčný uhol zabezpečuje, že obe kolesá sa odvaľujú po kružniciach so spoločným stredom, bez bočného šmyku
- Zabraňuje nadmernému opotrebovaniu a zahrievaniu pneumatík v zákrutách
- Zmenšuje polomer otáčania vozidla
- Ackermannova geometria sa dosahuje vhodným sklonom riadiacich ramien (lichobežníkové usporiadanie)

## Rozchod kolies

Rozchod kolies je vzdialenosť medzi stredmi styčných plôch ľavej a pravej pneumatiky na jednej náprave.

{{< figure src="rozchod.jpg" alt="Rozchod kolies" width="50%" caption="Obr. 12.21 - Rozchod kolies" >}}

### Vplyv

- Širší rozchod zvyšuje priečnu stabilitu vozidla a znižuje riziko prevrátenia v zákrutách
- Širší rozchod zlepšuje správanie vozidla pri bočnom vetre
- Užší rozchod umožňuje lepšiu manévrovateľnosť v úzkych priestoroch
- Rozchod prednej a zadnej nápravy môže byť rozdielny

## Rázvor náprav

Rázvor náprav je vzdialenosť medzi osami prednej a zadnej nápravy.

{{< figure src="razvor.jpg" alt="Rázvor náprav" width="70%" caption="Obr. 12.22 - Rázvor náprav" >}}

### Vplyv

**Dlhý rázvor:**
- Lepšia stabilita pri vysokých rýchlostiach
- Väčší priestor pre cestujúcich a batožinu
- Plynulejšia jazda cez nerovnosti (menšie kývanie)
- Väčší polomer otáčania, horšia manévrovateľnosť

**Krátky rázvor:**
- Lepšia manévrovateľnosť a menší polomer otáčania
- Rýchlejšia reakcia na pohyby volantom
- Menšia stabilita pri vysokých rýchlostiach
- Výraznejšie kývanie pri prejazde nerovností

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="/ucebnica/2-rocnik/04-privesy-navesy/" title="Prívesy a návesy" subtitle="Rozdiel medzi prívesom a návesom, rozdelenie, konštrukcia, dopad na jazdnú súpravu...">}}
{{< /cards >}}

---

{{< spoiler text="Zdroje" >}}
- FAKTOR, I., 2003, Cestné vozidlá II. Bratislava: EXPOL PEDAGOGIKA. ISBN 978-80-8091-351-9.
- Wikipedia – Wheel alignment: https://en.wikipedia.org/wiki/Wheel_alignment
- Wikipedia – Camber angle: https://en.wikipedia.org/wiki/Camber_angle
- Wikipedia – Caster angle: https://en.wikipedia.org/wiki/Caster_angle
- Wikipedia – Toe (automotive): https://en.wikipedia.org/wiki/Toe_(automotive)
- Wikipedia – Scrub radius: https://en.wikipedia.org/wiki/Scrub_radius
- Wikipedia – Ackermann steering geometry: https://en.wikipedia.org/wiki/Ackermann_steering_geometry
- Street Machine – Wheel Alignment Basics: https://www.streetmachine.com.au/features/wheel-alignment-basics-toe-camber-caster
- Certbolt – Steering Geometry Technical Guide: https://www.certbolt.com/certification/what-is-steering-geometry-an-in-depth-technical-guide/
{{< /spoiler >}}
