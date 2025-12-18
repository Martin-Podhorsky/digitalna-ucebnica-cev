---
title: "Geometria riadenia kolies"
type: docs
weight: 3
sidebar:
  open: false
---

Geometria riadenia je súbor nastavení, ktoré určujú, ako sú kolesá naklonené a natočené voči vozovke a karosérii.

Predstav si to takto: keby si kolesá nasadil "len tak", auto by sa ťažko riadilo, pneumatiky by sa rýchlo opotrebovali a auto by "ťahalo" do strany. Preto inžinieri kolesá úmyselne mierne nakláňajú a natáčajú podľa presných uhlov.

Správne nastavená geometria kolies:
- Zabezpečuje, že sa pneumatiky odvaľujú čisto po vozovke (nešmýkajú sa do strany)
- Predlžuje životnosť pneumatík a znižuje spotrebu paliva
- Auto ide rovno bez toho, aby si musel neustále korigovať volant
- Po prejazde zákrutou sa volant sám vráti do stredu
- Auto lepšie reaguje na pohyby volantom

Geometriu tvoria tieto hlavné parametre:
1. Zbiehavosť alebo rozbiehavosť kolies ($\delta$)
2. Odklon/príklon kolesa ($\alpha$)
3. Príklon osi riadenia ($\sigma$)
4. Záklon osi riadenia ($\tau$)
5. Závlek kolesa ($n_k$)
6. Polomer riadenia ($r_0$)
7. Rozchod kolies
8. Rázvor náprav
9. Diferenčný uhol (Ackermannova geometria)

---

## Zbiehavosť alebo rozbiehavosť kolies ($\delta$)

Keď sa pozrieš na auto zhora, kolesá nemusia byť úplne rovnobežné. Môžu byť mierne natočené dovnútra alebo von.

- **Zbiehavosť (Toe-in):** Predné hrany kolies sú bližšie k sebe ako zadné. Kolesá akoby "pozerali" na seba.
- **Rozbiehavosť (Toe-out):** Predné hrany kolies sú ďalej od seba. Kolesá akoby "pozerali" od seba.

{{< figure src="toe-in-toe-out.png" alt="Zbiehavosť a rozbiehavosť kolies" width="45%" caption="Obr. 12.14 - Zbiehavosť a rozbiehavosť kolies" >}}

### Vplyv

**Zbiehavosť (Toe-in) – kolesá natočené dovnútra:**
- Auto lepšie drží priamy smer. Nemusíš neustále korigovať volant.
- Prečo to funguje? Počas jazdy rôzne sily tlačia kolesá von (napríklad odpor vzduchu, nerovnosti). Zbiehavosť to vopred vyrovnáva – kolesá sú nastavené mierne dovnútra, takže počas jazdy sa "vyrovnajú" do ideálnej polohy.
- **Pozor:** Ak je zbiehavosť príliš veľká, pneumatiky sa opotrebúvajú na vonkajších hranách.

**Rozbiehavosť (Toe-out) – kolesá natočené von:**
- Auto ochotnejšie zatáča. Reaguje rýchlejšie, keď otočíš volantom.
- Používa sa hlavne na pretekárskych autách alebo na autách s predným náhonom (motor poháňa predné kolesá). Pri akcelerácii ťah motora sťahuje kolesá k sebe, takže rozbiehavosť to kompenzuje.
- **Pozor:** Ak je rozbiehavosť príliš veľká, auto je nestabilné v priamom smere a pneumatiky sa opotrebúvajú na vnútorných hranách.

## Odklon/príklon kolesa ($\alpha$)

Keď sa pozrieš na auto spredu, kolesá nemusia stáť úplne zvisle. Môžu byť naklonené dovnútra alebo von.

- **Negatívny odklon (príklon):** Vrch kolesa je naklonený dovnútra k autu. Koleso vyzerá ako písmeno "/" (ľavé) alebo "\\" (pravé).
- **Pozitívny odklon:** Vrch kolesa je naklonený von od auta.

{{< figure src="odklon-priklon.jpg" alt="Odklon/príklon kolesa ($\alpha$)" width="45%" caption="Obr. 12.15 - Odklon/príklon kolesa ($\alpha$)" >}}

### Vplyv

**Negatívny odklon – vrch kolesa dovnútra:**
- Lepšia priľnavosť v zákrutách. Keď auto zatáča, karoséria sa nakláňa von. Vonkajšie koleso (ktoré nesie väčšinu váhy) sa vďaka náklonu "vyrovná" a celá plocha pneumatiky sa oprie o vozovku.
- Väčšina moderných áut má mierny negatívny odklon.
- **Pozor:** Príliš veľký negatívny odklon znamená, že v priamom smere sa pneumatika dotýka vozovky len vnútornou hranou. To zhoršuje brzdenie, akceleráciu a rýchlo ničí vnútornú stranu pneumatiky.

**Pozitívny odklon – vrch kolesa von:**
- Používal sa na starších autách a nákladiakoch. Dôvod? Znižoval silu potrebnú na otáčanie volantom (vtedy neboli posilňovače).
- Keď sa nákladiak naloží ťažkým nákladom, kolesá sa pod váhou "vyrovnajú" do zvislej polohy.

## Príklon osi riadenia ($\sigma$)

Os riadenia je pomyselná čiara, okolo ktorej sa koleso otáča, keď točíš volantom. Táto os nie je zvislá – je naklonená dovnútra (horný koniec je bližšie k stredu auta).

{{< figure src="priklon-osi-riadenia.jpg" alt="Príklon osi riadenia ($\sigma$)" width="45%" caption="Obr. 12.X - Príklon osi riadenia ($\sigma$)" >}}

### Vplyv

- **Volant sa sám vracia do stredu.** Keď zatočíš, predná časť auta sa vďaka tomuto náklonu mierne nadvihne. Keď pustíš volant, váha auta tlačí prednú časť späť dole, a tým sa kolesá vrátia do priameho smeru.
- Zmenšuje polomer riadenia (vysvetlené nižšie).
- Typická hodnota: 5° až 15°.

## Záklon osi riadenia ($\tau$)

Záklon je ďalší uhol tej istej osi riadenia, ale teraz pri pohľade zboku. Os riadenia je naklonená dozadu – horný koniec je viac vzadu ako spodný.

{{< figure src="záklon-osi-riadenia.png" alt="Záklon osi riadenia ($\tau$)" width="40%" caption="Obr. 12.X - Záklon osi riadenia ($\tau$)" >}}

### Vplyv

**Pozitívny záklon – os naklonená dozadu:**
- Toto je **hlavný dôvod, prečo auto ide rovno a volant sa vracia do stredu**.
- Funguje to ako koliesko na nákupnom vozíku. Koliesko sa vždy samo natočí v smere jazdy, pretože bod otáčania je pred bodom dotyku s podlahou. Rovnaký princíp platí aj pre predné kolesá auta.
- Väčší záklon = stabilnejšia jazda, ale ťažšie otáčanie volantom.

## Závlek kolesa ($n_k$)

Závlek je vzdialenosť na zemi medzi dvoma bodmi:
1. Bod, kde by predĺžená os riadenia pretla vozovku
2. Stred dotykovej plochy pneumatiky

{{< figure src="závlek-kolesa.png" alt="Závlek kolesa ($n_k$)" width="40%" caption="Obr. 12.X - Závlek kolesa ($n_k$)" >}}

### Vplyv

- Závlek vzniká ako dôsledok záklonu osi riadenia.
- Predstav si to tak: pneumatika je "vlečená" za osou riadenia, podobne ako prikolica za autom. Toto "vlečenie" vytvára stabilizačný efekt.
- Čím väčší závlek, tým stabilnejšie auto ide rovno a tým silnejšie sa volant vracia do stredu. Ale zároveň je ťažšie volantom otáčať.

## Polomer riadenia ($r_0$)

Polomer riadenia (scrub radius) je vzdialenosť medzi:
1. Stredom dotykovej plochy pneumatiky
2. Bodom, kde os riadenia pretína vozovku

{{< figure src="polomer-riadenia.jpg" alt="Polomer riadenia ($r_0$)" width="85%" caption="Obr. 12.X - Polomer riadenia ($r_0$)" >}}

### Vplyv

**Pozitívny polomer – os pretína vozovku bližšie k stredu auta ako pneumatika:**
- Vodič lepšie cíti povrch cesty cez volant.
- **Nevýhoda:** Pri náraze do diery alebo defekte môže volant prudko "kopnúť" alebo sa vytrhnúť z rúk.

**Negatívny polomer – os pretína vozovku ďalej od stredu auta ako pneumatika:**
- **Bezpečnejší pre moderné autá.**
- Príklad: Ak brzdíš a jedna strana auta je na ľade a druhá na asfalte, auto sa samo koriguje a udržuje priamy smer. Pri pozitívnom polomere by ťa to stiahlo do strany.
- Štandardné nastavenie pre autá s predným náhonom a ABS.

**Nulový polomer – os pretína presne stred pneumatiky:**
- Najľahšie sa otáča volantom (najmä na mieste).
- **Nevýhoda:** Vodič menej cíti, čo sa deje s kolesami. Auto je citlivejšie na nerovnosti.

## Diferenčný uhol (Ackermannova geometria)

Keď auto zatáča, vnútorné koleso opisuje menší kruh ako vonkajšie koleso (je bližšie k stredu otáčania). Preto musí byť **vnútorné koleso natočené viac** ako vonkajšie.

{{< figure src="diferencny-uhol.jpg" alt="Diferenčný uhol (Ackermannova geometria)" width="80%" caption="Obr. 12.X - Diferenčný uhol (Ackermannova geometria)" >}}

### Vplyv

- Keby boli obe kolesá natočené rovnako, jedno z nich by sa muselo šmýkať po vozovke. To by ničilo pneumatiky a zhoršovalo ovládanie.
- Rozdiel v uhle natočenia sa nazýva **diferenčný uhol**.
- Dosahuje sa špeciálnou konštrukciou riadiacich tyčí – netvoria obdĺžnik, ale lichobežník. Vďaka tomu sa vnútorné koleso automaticky natočí viac.

## Rozchod kolies

Rozchod je vzdialenosť medzi stredmi ľavej a pravej pneumatiky na jednej náprave.

{{< figure src="rozchod.jpg" alt="Rozchod kolies" width="50%" caption="Obr. 12.X - Rozchod kolies" >}}

### Vplyv

- Širší rozchod = auto je stabilnejšie v zákrutách a ťažšie sa prevráti.
- Užší rozchod = auto sa zmestí do užších priestorov, ale je menej stabilné.

## Rázvor náprav

Rázvor je vzdialenosť medzi stredmi prednej a zadnej nápravy (alebo jednoducho: ako ďaleko sú predné kolesá od zadných).

{{< figure src="razvor.jpg" alt="Rázvor náprav" width="70%" caption="Obr. 12.X - Rázvor náprav" >}}

### Vplyv

- **Dlhý rázvor:** Auto lepšie drží priamy smer pri vysokej rýchlosti. Viac miesta pre cestujúcich. Ale horšie sa s ním manévruje v meste (väčší polomer otáčania).
- **Krátky rázvor:** Auto je "hravejšie" a ochotnejšie zatáča. Ľahšie sa parkuje. Ale pri vysokej rýchlosti je menej stabilné.
