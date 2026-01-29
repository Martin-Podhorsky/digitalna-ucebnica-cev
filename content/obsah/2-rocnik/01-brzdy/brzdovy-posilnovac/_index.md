---
linkTitle: "10.4 Brzdový posilňovač"
title: "Brzdový posilňovač"
weight: 4
type: docs
sidebar:
  open: false
---

Brzdový posilňovač je zariadenie zosilňujúce silu, ktorú vodič vyvinie stlačením brzdového pedálu pri brzdení. Tím pádom taktiež znižuje silu, ktorú musí vodič pri brzdení na pedál vyvinúť. Zosílenie býva zvyčajne od 300% do 500%.

## Podtlakový brzdový posilňovač

Tento typ brzdového posilňovača využíva na zosílenie podtlak vytvorený v sacom potrubí motora (alebo vo výveve).

### Hlavné časti

{{< figure src="brake-booster.png" alt="Schéma podtlakového brzdového posilňovača" width="80%" caption="Obr. 10.14 - Schéma podtlakového brzdového posilňovača" >}}

1 - **Podtlaková komora** -- časť posilňovača, v ktorej je vytváraný podtlak. <br>
2 - **Podtlaková prípojka** -- prepojenie so saním alebo vývevou, ktoré vytvárajú v podtlakovej komore podtlak (vysávajú z nej vzduch).<br>
3 - **Piest** -- pohyblivá časť.<br>
4 - **Pružina** -- po ukončení brzdenia vracia piest späť na svoje pôvodné miesto.<br>
5 - **Membrána** -- oddeľuje podtlakovú komoru od pracovnej a zároveň umožňuje pohyb piestu.<br>
6 - **Brzdový pedál** -- vodič ním ovláda brzdové ústrojenstvo; jeho stlačením je vytvorený tlak, ktorý posilňovač zosíli.<br>
7 - **Piestnica** -- prenáša tlak vytvorený zošliapnutím pedálu vodorovným smerom.<br>
8 - **Tlačná pružina** -- Tlačí na tanierový ventil, ktorý pri stlačením brzdového pedálu uzatvára podtlakový (prepúšťací) kanál. Zároveň vracia brzdový pedál do pôvodnej polohy po jeho zošliapnutí.<br>
9 - **Tanierový ventil** -- pri stlačením brzdového pedálu uzatvára podtlakový (prepúšťací) kanál.<br>
10 - **Prepúšťací kanál** -- keď je brzdový pedál v základnej pozícii, prepúšťa podtlak z podtlakovej do pracovnej komory. Pri zošliapnutí pedála je tento kanál uzatvorený tanierovým ventilom a do pracovnej komory sa dostáva vzduch s atmosferickým tlakom. Tým pádom je v pracovnej komore väčší tlak, ako v podtlakovej, čím je celý piest tlačený požadovaným smerom.<br>
11 - **Atmosferický kanál** -- v základnej pozíci je zablokovaný vložkou ventilu, ktorá je pripevnená ku piestnici. Tá sa pri zošliapnutí brzdového pedála hýbe spolu s piestnicou a otvára tento kanál.<br>
12 - **Vložka ventilu** -- otvára a zatvára atmosferický kanál a jej širšia časť taktiež udržuje piesticu v požadovanej polohe (ak by tam nebola, piestnica by mohla trieť o tanierový ventil).<br>
13 - **Čistič** -- zabraňuje vniku nečistôt.<br>
14 - **Pracovná komora** -- v základnej polohe brzdového pedála je v nej podtlak a pri stlačení sa do nej dostáva vzduch z okolitého prostredia.<br>
15 - **Reakčný kotúč** -- je vložený v strede piestu, ktorý ho posúva požadovaným smerom silou vytvorenou rozdielmi tlakov v podtlakovej a pracovnej komore.<br>
16 - **Tlačná tyč** -- pripevnená ku reakčnému kotúču. Prenáša výsledný tlak do hlavného brzdového valca.<br>

### Princíp činnosti:

Keď vodič nestláča brzdový pedál, v podtlakovej aj v pracovnej komore je rovnaký tlak (podtlak). Pri stlačení pedála sa do pracovnej komory vpustí atmosférický tlak a zablokuje sa prepúšťací kanál. Rozdiel tlakov (podtlak vs. atmosférický tlak) vytvára silu, ktorá tlačí na piest a prenáša sa do hlavného brzdového valca pomocou tlačnej tyče.

{{< figure src="brake-booster-active.png" alt="Podtlakový brzdový posilňovač pri plnom brzdení" width="60%" caption="Obr. 10.15 - Podtlakový brzdový posilňovač pri plnom brzdení" >}}

## Elektronicky riadený podtlakový brzdový posilňovač (BAS)

Mnoho vodičov pri kritických situáciach reaguje síce rýchlo, ale brzdový pedál nezošliapnu dostatočnou silou. To má za následok to, že sa v brzdovom systéme nevyvinie dostatočný tlak a výrazne sa predĺži brzdná dráha. Elektronicky riadený podtlakový posilňovač sa snaží tento problém vyriešiť tým, že v takýchto prípadoch zabezpečí maximálny brzdný účinok.

### Hlavné časti:

{{< figure src="BAS.png" alt="Schéma elektronicky riadeného podtlakového brzdového posilňovača" width=70%" caption="Obr. 10.16 - Schéma elektronicky riadeného podtlakového brzdového posilňovača" >}}

1 - **Snímač polohy pracovného piestu** <br>
2 - **Membrána** <br>
3 - **Magnet** <br>
4 - **Vypínač systému** <br>
5 - **Pracovná komora** <br>
6 - **Podtlaková komora** <br>
7 - **Riadiaca jednotka**

### Princíp činnosti:

Systém vyhodnocuje rýchlosť stláčania brzdového pedála. Pri zistení náhlého, rýchleho stlačenia (typické pre núdzovú situáciu) systém automaticky zvyšuje brzdný tlak na maximum.

---

Nasledujúce učivo:
{{< cards >}}
  {{< card url="/obsah/2-rocnik/01-brzdy/ABS" title="Systém ABS" subtitle="Princíp činnosti, význam, konštrukcia...">}}
{{< /cards >}}

---

{{< spoiler text="Zdroje" >}}
- FAKTOR, I., 2003, Cestné vozidlá II. Bratislava: EXPOL PEDAGOGIKA. ISBN 978-80-8091-351-9.
{{< /spoiler >}}