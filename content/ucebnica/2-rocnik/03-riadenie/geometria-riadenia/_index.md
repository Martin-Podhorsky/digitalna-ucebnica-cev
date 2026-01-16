---
linkTitle: "12.3 Geometria riadenia kolies"
title: "Geometria riadenia kolies"
type: docs
weight: 3
sidebar:
  open: false
---

Geometria riadenia je súbor nastavení, ktoré určujú, ako sú kolesá naklonené a natočené voči vozovke a karosérii.

Správne nastavená geometria kolies zabezpečuje, že:
- Sa pneumatiky odvaľujú po vozovke rovnomerne (nešmýkajú sa do strán), čím sa predlžuje ich životnosť a znižuje sa spotreba paliva
- Auto ide rovno bez toho, aby vodič musel neustále korigovať volant
- Po prejazde zákrutou sa kolesá samé vrátia do priameho smeru
- Auto lepšie reaguje na pohyby volantom

**Hlavné parametre:**
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

## Zbiehavosť alebo rozbiehavosť kolies

Zbiehavosť alebo rozbiehavosť kolies je to rozdiel vzdialeností prednej časti kolies a zadnej časti kolies
  - Ak je predná časť kolies k sebe bližšie ako zadná (kolesá sa akoby "pozerajú" na seba), hovoríme o zbiehavosti
  - Ak je zadná časť kolies k sebe bližšie ako predná (kolesá sa akoby "pozerajú" od seba), hovoríme o rozbiehavosti

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

## Odklon/príklon kolesa

Odklon/príklon kolesa je náklon kolesa dovnútra alebo von od zvislice pri pohľade spredu alebo zozadu.

{{< figure src="odklon-priklon.jpg" alt="Odklon/príklon kolesa ($\alpha$)" width="45%" caption="Obr. 12.15 - Odklon/príklon kolesa ($\alpha$)" >}}

Spôsobuje vznik axiálnej sily, ktorá pôsobí na ložiská kolies, kde vymedzuje vôlu. Axiálna sila taktiež bráni kmitaniu kolies. Väčšina automobilov má na prednej náprave odklon od uhla 0° 20’d o 2° pretože zlepšuje smerovú stabilitu

### Vplyv

**Príklon:**
- Lepšia priľnavosť v zákrutách. Keď auto zatáča, karoséria sa nakláňa von. Vonkajšie koleso (ktoré nesie väčšinu váhy) sa vďaka náklonu "vyrovná" a celá plocha pneumatiky sa oprie o vozovku.
- **Pozor:** Príliš veľký negatívny odklon znamená, že v priamom smere sa pneumatika dotýka vozovky len vnútornou hranou. To zhoršuje brzdenie, akceleráciu a rýchlo ničí vnútornú stranu pneumatiky.

**Odklon:**
- Používal sa na starších autách a nákladiakoch, pretože znižoval silu potrebnú na otáčanie volantom (vtedy neboli posilňovače). Keď sa nákladiak naložil ťažkým nákladom, kolesá sa pod váhou "vyrovnali" do zvislej polohy.

## Príklon osi riadenia

Príklon osi riadenia je uhol medzi osou čapu riadenia a zvislicou pri pohľade spredu alebo zozadu.

{{< figure src="priklon-osi-riadenia.png" alt="Príklon osi riadenia ($\sigma$)" width="100%" caption="Obr. 12.16 - Príklon osi riadenia ($\sigma$)" >}}

Zlepšuje stabilitu vozidla a zabezpečuje samovoľné vracanie sa kolies po vychýlení do priameho smeru. Pri väčšine vozidiel býva v rozmedzí 3° až 10°.

### Vplyv

- Zlepšuje stabilitu vozidla a zabezpečuje samovoľné vracanie sa kolies po vychýlení do priameho smeru
- Pri väčšine vozidiel býva v rozmedzí 3° až 10°

## Záklon osi riadenia

Záklon osi riadenia je uhol medzi osou čapu riadenia a zvislicou, pri pohľade zboku vozidla.

{{< figure src="záklon-osi-riadenia.png" alt="Záklon osi riadenia ($\tau$)" width="40%" caption="Obr. 12.17 - Záklon osi riadenia ($\tau$)" >}}

### Vplyv

-	Zabezpečuje smerovú stabilitu a je hlavným dôvodom pre vracanie sa kolies/kolesa do priameho smeru po vychýlení
-	Taktiež vymedzuje vôlu v kĺboch spojovacích tyčí
- Čím väčší záklon, tým stabilnejšia jazda, ale tým ťažšie otáčanie volantom

## Závlek kolesa

Závlek je vzdialenosť na zemi medzi bodom, kde by predĺžená os riadenia pretla vozovku a stredom dotykovej plochy pneumatiky.

{{< figure src="závlek-kolesa.png" alt="Závlek kolesa ($n_k$)" width="40%" caption="Obr. 12.18 - Závlek kolesa ($n_k$)" >}}

### Vplyv

- Závlek vzniká ako dôsledok záklonu osi riadenia, takže vplyv je rovnaký

## Polomer riadenia

Polomer riadenia je vzdialenosť medzi predĺženou osou čapu riadenia a stredom odtlačku pneumatiky na vozovke.


{{< figure src="polomer-riadenia.jpg" alt="Polomer riadenia ($r_0$)" width="85%" caption="Obr. 12.19 - Polomer riadenia ($r_0$)" >}}

### Vplyv

**Pozitívny polomer** – os pretína vozovku bližšie k stredu auta ako pneumatika:
- Vodič lepšie cíti povrch cesty cez volant
- To tiež znamená, že pri náraze do diery alebo defekte môže volant prudko "kopnúť" a vytrhnúť sa z rúk
- Uľahčuje otáčanie volantom (najmä na mieste). Pretože koleso s pozitívnym polomerom riadenia sa neotáča na mieste, ale mierne sa odvaľuje (opisuje oblúk), čo znižuje odpor pri zatáčaní (v prípade, ak vozidlo práve nebrzdí).
- U vozidiel s predným náhonom výrazne zosilňuje nežiaduce sily v riadení pri prudkej akcelerácii (pocit ťahania vo volante alebo vychýlenie vozidla zo chcenej dráhy)

**Negatívny polomer** – os pretína vozovku ďalej od stredu auta ako pneumatika:
- Vodič menej cíti povrch cesty a riadenie je tuhšie
- Ak kolesá na ľavej a pravej strane brzdia s rôznou intenzitou (napr. jedno koleso je na asfalte a druhé na ľade), negatívny polomer riadenia vytvára silu, ktorá koleso s vyššou priľnavosťou natáča smerom k stredu vozidla. To automaticky kompenzuje ťahanie vozidla do strany a pomáha udržať priamy smer.
- U vozidiel s predným náhonom pomáha minimalizovať nežiaduce sily v riadení pri prudkej akcelerácii
- Kvôli tomu je štandardom pre autá s predným náhonom a s funkciou ABS

**Nulový polomer** – os pretína presne stred pneumatiky:
- Vodič vôbec necíti povrch cesty (riadenie je akokeby "mŕtve"). Tým pádom sa ani žiadne nárazy neprenášajú na volant.
- Volant sa pri státi veľmi ťažko otáča, pretože sa celá styčná plocha pneumatiky otáča v jednom bode namiesto toho, aby sa mierne odvaľovala
- Pri prudkom brzdení môže byť auto s nulovým polomerom „nervózne“. Aj malé nerovnosti vozovky môžu spôsobiť náhle zmeny smeru, pretože riadeniu chýba stabilizujúca sila, ktorú poskytuje aspoň malý pozitívny alebo negatívny polomer.

## Diferenčný uhol (Ackermannova geometria)

Diferenčný uhol je rozdiel medzi uhlom natočenia vonkajšieho a vnútorného kolesa pri prejazde zákrutou.

{{< figure src="diferencny-uhol.jpg" alt="Diferenčný uhol (Ackermannova geometria)" width="80%" caption="Obr. 12.20 - Diferenčný uhol (Ackermannova geometria)" >}}

### Vplyv

- Správny diferenčný uhol zabezpečuje, že sa kolesá odvaľujú rovnomerne bez toho, aby ich "tlačilo" do strany, čím by vznikalo nadmerné zahrievanie a opotrebenie pneumatík (v každej zákrute by ste počuli pískanie pneumatík)
- Zmenšuje polomer otáčania

## Rozchod kolies

Rozchod kolies je vzdialenosť medzi stredmi ľavej a pravej pneumatiky na jednej náprave.

{{< figure src="rozchod.jpg" alt="Rozchod kolies" width="50%" caption="Obr. 12.21 - Rozchod kolies" >}}

### Vplyv

-	Širší rozchod kolies zvyšuje celkovú stabilitu vozidla a znižuje pravdepodobnosť prevrátenia, najmä počas zákrut
-	Užší rozchod môže zasa v určitých situáciách zlepšiť manévrovateľnosť a odozvu riadenia, pretože znižuje námahu potrebnú na otáčanie kolies

## Rázvor náprav

Rázvor náprav je vzdialenosť medzi osami prednej a zadnej nápravy.

{{< figure src="razvor.jpg" alt="Rázvor náprav" width="70%" caption="Obr. 12.22 - Rázvor náprav" >}}

### Vplyv

- **Dlhý rázvor:** Auto lepšie drží priamy smer pri vysokej rýchlosti. Viac miesta pre cestujúcich. Ale horšie sa s ním manévruje v meste (väčší polomer otáčania).
- **Krátky rázvor:** Auto je "hravejšie" a ochotnejšie zatáča. Ľahšie sa parkuje. Ale pri vysokej rýchlosti je menej stabilné.

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="/ucebnica/2-rocnik/04-privesy-navesy/" title="Prívesy a návesy" subtitle="Rozdieľ medzi prívesom a návesom, rozdelenie, konštrukcia, dopad na jazdnú súpravu...">}}
{{< /cards >}}

---

{{< spoiler text="Zdroje" >}}
- FAKTOR, I., 2003, Cestné vozidlá II. Bratislava: EXPOL PEDAGOGIKA. ISBN 978-80-8091-351-9.
- https://lubomir-mazur.webnode.sk/automobily/a2-rocnik/geometria-riadenia/
{{< /spoiler >}}