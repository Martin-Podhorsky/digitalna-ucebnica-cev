---
linkTitle: "10. 8 Vzduchotlakové brzdy"
title: "Vzduchotlakové (strojové) brzdy"
weight: 8
type: docs
sidebar:
  open: false
---

Vzduchotlakový brzdový systém je typ brzdy, pri ktorom sa na ovládanie bŕzd používa stlačený vzduch namiesto brzdovej kvapaliny. Používajú sa na ťažkých nákladných vozidlách, autobusoch a súpravách s prívesmi, kde hydraulický systém by nevyvinul dostatočnú brzdnú silu.

{{< figure src="air-brake.png" alt="Kotúčová vzduchová brzda" width="60%" caption="Obr. 10.19 - Kotúčová vzduchová brzda" >}}

## Princíp činnosti

Typický prevádzkový tlak je približne 6,9 až 8,3 bar (100-120 psi). Systém je rozdelený na **zásobovací systém** (výroba a skladovanie vzduchu) a **riadiaci systém** (ovládanie bŕzd).

### Prevádzková brzda:

Keď vodič stlačí brzdový pedál, vzduch pod tlakom je vedený zo zásobníka do brzdových komôr pri kolesách. Tlak vzduchu posunie membrány alebo piesty, ktoré pritlačia brzdové platničky alebo čeľuste na kotúče/bubny. Po uvoľnení pedála sa stlačený vzduch vypustí do atmosféry a vratné pružiny odtiahnu brzdy.

### Parkovacie brzdy:

Parkovacie brzdy fungují opačne - sú držané v zapnutej polohe silnou pružinou. Vzduch pod tlakom stláča pružinu a uvoľňuje brzdu. Pri stlačení ovládacej páky sa vzduch vypustí a pružina zabrzdi vozidlo. **Náhla strata tlaku vzduchu má za následok okamžité zapnutie parkovacej brzdy** - dôležitá bezpečnostná funkcia.

## Hlavné časti

{{< figure src="air-brake-scheme.png" alt="Časti systému vzduchových bŕzd" width="100%" caption="Obr. 10.20 - Časti systému vzduchových bŕzd" >}}

### Zásobovací systém:

1 - **Kompresor vzduchu** -- stláča atmosférický vzduch a dodáva ho do systému. Je poháňaný motorom vozidla cez remeň alebo ozubené kolesá.<br>
2 - **Regulátor tlaku** -- riadi činnosť kompresora. Keď tlak klesne pod cca 6,9 bar, zapne kompresor. Keď dosiahne cca 8,3 bar, vypne ho. Tým udržiava tlak v požadovanom rozsahu.<br>
3 - **Sušič vzduchu** -- odstraňuje vlhkosť a olejové pary zo stlačeného vzduchu. Obsahuje vysúšacie činidlo (silikagél). Vlhkosť by mohla v zime zamrznúť a zablokovať ventily/potrubie.<br>
4 a 6 - **Zásobníky vzduchu** (vzduchojemy):<br>
   - **Mokrá nádrž** (4) -- prvý zásobník za sušičom. Zachytáva zvyškovú vlhkosť a olej, ktoré sa pravidelne vypúšťajú cez výpustný kohút.
   - **Prevádzkové zásobníky** (6) -- skladujú suchý vzduch pre brzdové okruhy. Poskytujú rezervu vzduchu na niekoľko brzdení aj pri vypnutom motore.
5 - **Štvorkanálový ochranný ventil** -- rozdeľuje vzduch do štyroch samostatných okruhov (predná náprava, zadná náprava, príves, pomocné zariadenia). Pri poruche jedného okruhu automaticky uzavrie poškodený okruh a ostatné zostanú funkčné.<br>

### Riadiaci systém:

7 - **Ovládací ventil parkovacej brzdy** -- páka alebo tlačidlo v kabíne, ktorým vodič ovláda parkovaciu brzdu. V polohe "zabrzdené" vypúšťa vzduch z pružinových komôr.<br>
8 - **Bezpečnostný ventil parkovacej brzdy** -- automaticky aktivuje parkovaciu brzdu, ak tlak v systéme klesne pod bezpečnú úroveň (cca 4,5 bar). Chráni pred jazdou s nedostatočným tlakom.<br>
9 - **Brzdový pedál** (brzdový ventil) -- vodičom ovládaný ventil, ktorý dávkuje vzduch do brzdových komôr úmerne k sile stlačenia pedála.<br>
10 a 12 - **Brzdové komory:**<br>
   - **Membránové komory** (10) -- prevádzkové brzdy. Tlak vzduchu tlačí na membránu, ktorá cez tyč a páku aktivuje rozpernú vačku alebo strmeň brzdy.
   - **Pružinové komory** (12) -- parkovacie a núdzové brzdy. Silná pružina je počas jazdy stlačená vzduchom. Pri strate tlaku sa pružina uvoľní a zabrzdí vozidlo.
   
11 - **Relé ventil** -- urýchľuje plnenie a vypúšťanie vzduchu z brzdových komôr. Je umiestnený blízko zadných kolies, aby sa skrátila dráha vzduchu a znížilo oneskorenie brzdenia.<br>
13 - **Potrubia a hadice** -- rozvod stlačeného vzduchu. Oceľové potrubia na pevných častiach, gumové hadice na pohyblivých spojeniach.<br>

## Výhody vzduchotlakových bŕzd:

- **Veľká brzdná sila** -- vzduchové brzdy dokážu generovať oveľa vyššiu silu potrebnú na zastavenie ťažkých nákladov než bežné hydraulické brzdy.
- **Bezpečnostný mechanizmus** -- ak dôjde k strate tlaku vzduchu (napr. pri rozpojení hadíc alebo poruche), pružiny v brzdovom valci automaticky zabrzdia kolesá. Na rozdiel od nich, pri úniku kvapaliny v hydraulickom systéme brzdy úplne zlyhajú.
- **Odolnosť voči malým únikom** -- menší únik vzduchu nie je kritický, pretože kompresor neustále dopĺňa zásobu. V hydraulickom systéme aj malá netesnosť vedie k strate tlaku a zlyhaniu.
- **Jednoduché prepojenie s prívesmi** -- vzduchové hadice sa ľahko spájajú a odpájajú pomocou rýchlospojok bez rizika zavzdušnenia systému, čo je pri hydraulike problém.
- **Neobmedzené médium** -- vzduch je všade okolo nás a je zadarmo. Na rozdiel od hydraulického oleja, vzduch pri úniku neznečisťuje životné prostredie a jeho zásoba je prakticky nevyčerpateľná.
- **Viacúčelovosť** -- stlačený vzduch z nádrží vozidla možno využiť aj na iné účely, napríklad na pohon vzduchového klaksónu, nastavenie sedadiel alebo dohusťovanie pneumatík.
- **Odolnosť voči prehriatiu** -- vzduchové brzdy lepšie znášajú vysoké teploty vznikajúce pri dlhom brzdení (napr. klesanie z kopca), čím sa znižuje riziko "vädnutia" (fading) bŕzd.

## Nevýhody vzduchotlakových bŕzd:

- **Pomalšia reakcia (Brake Lag)** -- vzduch je stlačiteľný, a preto trvá zlomok sekundy dlhšie (približne 0,5 sekundy), kým sa tlak vzduchu prenesie až k brzdám. Hydraulická kvapalina je nestlačiteľná, takže prenos sily je okamžitý.
- **Vysoká cena a zložitosť** -- systém vyžaduje drahé komponenty ako kompresor, vzduchové nádrže, vysúšače vzduchu a komplexnú sieť ventilov. Mechanické a hydraulické brzdy sú konštrukčne oveľa jednoduchšie a lacnejšie na výrobu.
- **Čas potrebný na natlakovanie** -- po dlhšom státí musí vodič počkať niekoľko minút, kým kompresor natlakuje systém na prevádzkovú úroveň. Bez dostatočného tlaku sa parkovacia brzda neuvoľní a vozidlo sa nepohne.
- **Náročná údržba v mrazoch** -- v stlačenom vzduchu sa prirodzene hromadí vlhkosť. Ak zlyhá vysúšač vzduchu, v zime môže vlhkosť v potrubí zamrznúť a vyradiť brzdy z prevádzky.
- **Hlučnosť** -- vzduchové brzdy sú výrazne hlučnejšie. Pri každom uvoľnení brzdy dochádza k hlasnému odfúknutiu vzduchu, čo by v bežnej mestskej premávke osobných áut bolo rušivé.
- **Rozmery a hmotnosť** -- celý systém (nádrže, kompresor) zaberá veľa miesta a zvyšuje celkovú hmotnosť vozidla, čo je pri menších autách nežiaduce.
- **Imobilizácia pri poruche** -- ak dôjde k veľkému úniku vzduchu alebo roztrhnutiu hadice, bezpečnostný systém kolesá okamžite zablokuje. Vozidlo je potom nemožné odtiahnuť bez manuálneho odblokovania brzdových valcov.

## Dvojokruhová vzduchotlaková sústava

Pre bezpečnosť sú moderné vzduchotlakové brzdové systémy vždy dvojokruhové - majú dva nezávislé brzdové okruhy s oddelenými zásobníkmi.

**Typické usporiadanie:**
- **Primárny okruh:** zadná náprava ťahača
- **Sekundárny okruh:** predná náprava ťahača + brzdy prívesa

Pri poruche jedného okruhu zostáva druhý plne funkčný. Štvorkanálový ochranný ventil automaticky izoluje poškodený okruh, čím sa zabráni strate tlaku v celom systéme.

Nasledujúce učivo:
{{< cards >}}
  {{< card url="02-pruzenie-tlmenie/_index" title="Pruženie a Tlmenie" subtitle="Princíp činnosti, Konštrukcia, výhody, nevýhody...">}}
{{< /cards >}}