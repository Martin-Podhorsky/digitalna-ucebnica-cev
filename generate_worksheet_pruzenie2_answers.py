"""
Generátor odpoveďového hárku: Pneumatické, hydropneumatické a gumové pruženie

Použitie:  python generate_worksheet_pruzenie2_answers.py
Výstup:    pracovny-list-pruzenie2-odpovede.pdf

Požiadavky: pip install reportlab
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import black, HexColor
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle,
    HRFlowable, PageBreak,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "content", "ucivo", "2-rocnik", "02-pruzenie-tlmenie")
PNEUM_IMG = os.path.join(CONTENT_DIR, "pneumaticke-pruzenie", "konstrukcia.png")
OUTPUT = os.path.join(BASE_DIR, "pracovny-list-pruzenie2-odpovede.pdf")

# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
PAGE_W, PAGE_H = A4
MARGIN_LR = 1.5 * cm
MARGIN_TB = 1.2 * cm
UW = PAGE_W - 2 * MARGIN_LR

# ---------------------------------------------------------------------------
# Fonts
# ---------------------------------------------------------------------------
FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont("F", os.path.join(FONT_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("FB", os.path.join(FONT_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("FI", os.path.join(FONT_DIR, "ariali.ttf")))
pdfmetrics.registerFont(TTFont("FBI", os.path.join(FONT_DIR, "arialbi.ttf")))
pdfmetrics.registerFontFamily("F", normal="F", bold="FB", italic="FI", boldItalic="FBI")

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
RED = HexColor("#CC0000")
BLUE = HexColor("#0033AA")
GRAY_BG = HexColor("#F0F0F0")

s_title = ParagraphStyle(
    "Title", fontName="FB", fontSize=14, leading=18,
    alignment=TA_CENTER, spaceAfter=4,
)
s_header = ParagraphStyle("Header", fontName="F", fontSize=10, leading=13)
s_q = ParagraphStyle(
    "Q", fontName="FB", fontSize=11, leading=14,
    spaceBefore=6, spaceAfter=3, textColor=RED,
)
s_body = ParagraphStyle("Body", fontName="F", fontSize=10, leading=14, spaceAfter=1)
s_ans = ParagraphStyle("Ans", fontName="F", fontSize=10, leading=16)
s_pn = ParagraphStyle("PN", fontName="F", fontSize=10, leading=17)
s_pnr = ParagraphStyle(
    "PNR", fontName="FB", fontSize=9, leading=17, alignment=TA_CENTER,
)
s_table = ParagraphStyle("Tbl", fontName="F", fontSize=10, leading=13)
s_table_b = ParagraphStyle("TblB", fontName="FB", fontSize=10, leading=13)
s_table_c = ParagraphStyle(
    "TblC", fontName="F", fontSize=10, leading=13, alignment=TA_CENTER,
)
s_answer_line = ParagraphStyle(
    "AnsLine", fontName="FI", fontSize=10, leading=14, textColor=BLUE,
)

BL = "_______________"


def A(text):
    return f'<i><font color="#0033AA">{text}</font></i>'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def scaled_img(path, max_w, max_h=None):
    reader = ImageReader(path)
    iw, ih = reader.getSize()
    ratio = iw / ih
    nw = min(max_w, iw)
    nh = nw / ratio
    if max_h and nh > max_h:
        nh = max_h
        nw = nh * ratio
    img = Image(path, width=nw, height=nh)
    img.hAlign = "CENTER"
    return img


def pn_row(statement, answer):
    label = "Pravda" if answer else "Nepravda"
    t = Table(
        [[Paragraph(statement, s_pn),
          Paragraph(f'<b>{A(label)}</b>', s_pnr)]],
        colWidths=[UW * 0.73, UW * 0.27],
    )
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, 0), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t


def answer_line():
    return [Spacer(1, 14), HRFlowable(width="100%", thickness=0.5, color=black)]


# ---------------------------------------------------------------------------
# Build the PDF
# ---------------------------------------------------------------------------
def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=MARGIN_LR, rightMargin=MARGIN_LR,
        topMargin=MARGIN_TB, bottomMargin=MARGIN_TB,
    )
    story = []

    # ================================================================
    #  HEADER
    # ================================================================
    story.append(Paragraph(
        "Pracovný list CEV: Pneumatické, hydropneumatické a gumové pruženie – ODPOVEDE",
        s_title,
    ))
    ht = Table(
        [[
            Paragraph("Meno a priezvisko: " + "_" * 40, s_header),
            Paragraph("Dátum: " + "_" * 15, s_header),
            Paragraph("Trieda: " + "_" * 8, s_header),
        ]],
        colWidths=[UW * 0.50, UW * 0.25, UW * 0.25],
    )
    ht.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
    story.append(ht)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1, color=black))
    story.append(Spacer(1, 4))

    # ================================================================
    #  Q1 – Fill in the blanks (general info)
    # ================================================================
    story.append(Paragraph("1) Doplň do textu (všeobecné info):", s_q))
    story.append(Paragraph(
        f"Medzi hlavné požiadavky kladené na pruženie a tlmenie patrí "
        f"stály kontakt kolies s {A('vozovkou')}, absorbcia "
        f"{A('nerovností')} vozovky, "
        f"zabezpečenie stability a {A('komfortu')} jazdy.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Label pneumatic suspension diagram (all 8 parts)
    # ================================================================
    story.append(Paragraph(
        "2) Popíš časti pneumatického pruženia:", s_q,
    ))
    story.append(scaled_img(PNEUM_IMG, UW * 0.75, max_h=6.5 * cm))
    story.append(Spacer(1, 3))

    parts = [
        "Vzduchové mechy (vaky)",
        "Kompresor",
        "Sušič",
        "Zásobník vzduchu (akumulátor)",
        "Vzduchové vedenia",
        "Regulačné ventily",
        "Snímače výšky",
        "Riadiaca jednotka",
    ]
    rows = []
    for i in range(0, 8, 2):
        left = Paragraph(f"<b>{i+1}</b> – {A(parts[i])}", s_ans)
        right = Paragraph(f"<b>{i+2}</b> – {A(parts[i+1])}", s_ans)
        rows.append([left, right])
    t = Table(rows, colWidths=[UW * 0.5] * 2)
    t.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q3 – Fill in the blanks (pneumatické – principle)
    # ================================================================
    story.append(Paragraph("3) Doplň do textu (pneumatické pruženie):", s_q))
    story.append(Paragraph(
        f"Snímače výšky sledujú polohu karosérie voči kolesám. Keď sa zmení "
        f"zaťaženie, {A('riadiaca jednotka')} vyhodnotí údaje a cez "
        f"{A('ventily')} upraví tlak vzduchu "
        f"v mechoch. Keď sa tlak zvýši, vozidlo sa {A('zdvihne')} a pruženie "
        f"{A('stvrdne')}.",
        s_body,
    ))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q4 – Fill in the blanks (hydropneumatické pruženie)
    # ================================================================
    story.append(Paragraph("4) Doplň do textu (hydropneumatické pruženie):", s_q))
    story.append(Paragraph(
        f"Hydropneumatické pruženie kombinuje {A('hydrauliku')} (kvapalinu) "
        f"s {A('pneumatikou')} (plynom). Vyvinula ho spoločnosť "
        f"{A('Citroën')}. "
        f"Vo vnútri hydropneumatickej gule sa nachádza hydraulická kvapalina "
        f"a stlačený {A('dusík')}, oddelené pružnou membránou. Tlmenie je "
        f"zabezpečené prietokom kvapaliny cez {A('jednocestné')} ventily.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q5 – Match properties to suspension types
    # ================================================================
    story.append(Paragraph(
        "5) Priraď vlastnosť k správnemu druhu pruženia (zaškrtni):", s_q,
    ))
    props_answers = [
        ("Stála svetlá výška bez ohľadu na zaťaženie", True, True, False),
        ("Samotlmiaci efekt", False, False, True),
        ("Izolácia hluku a vibrácií", False, False, True),
        ("Progresívna charakteristika", True, True, False),
        ("Prepojenie s brzdami a posilňovačom riadenia", False, True, False),
        ("Nízka cena a jednoduchá výroba", False, False, True),
    ]
    match_data = [[
        Paragraph("<b>Vlastnosť</b>", s_table_b),
        Paragraph("<b>Pneum.</b>", s_table_b),
        Paragraph("<b>Hydropn.</b>", s_table_b),
        Paragraph("<b>Gumové</b>", s_table_b),
    ]]
    for prop, pn, hp, gm in props_answers:
        match_data.append([
            Paragraph(prop, s_table),
            Paragraph(A("✓") if pn else "", s_table_c),
            Paragraph(A("✓") if hp else "", s_table_c),
            Paragraph(A("✓") if gm else "", s_table_c),
        ])
    mt = Table(match_data, colWidths=[UW * 0.52, UW * 0.16, UW * 0.16, UW * 0.16])
    mt.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, black),
        ("BACKGROUND", (0, 0), (-1, 0), GRAY_BG),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ]))
    story.append(mt)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – True / False
    # ================================================================
    story.append(Paragraph("6) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt, ans in [
        ("Pneumatické pruženie sa používa predovšetkým na malých "
         "osobných automobiloch.", False),
        ("Gumové prvky (silentbloky) sa používajú na uloženie motora "
         "a prevodovky.", True),
        ("Hydropneumatické pruženie nepotrebuje samostatné tlmiče, pretože "
         "tlmenie zabezpečujú jednocestné ventily.", True),
        ("Vlnovcové mechy sa používajú v nákladných automobiloch "
         "a autobusoch.", False),
        ("Guma tvrdne v mraze a mäkne v teple.", True),
    ]:
        story.append(pn_row(stmt, ans))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q7 – Short answers
    # ================================================================
    story.append(Paragraph("7) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Uveď 3 výhody pneumatického pruženia.",
        s_body,
    ))
    story.append(Paragraph(
        A("Napr.: Stála svetlá výška (vozidlo si udržiava rovnakú výšku "
          "bez ohľadu na zaťaženie), nastaviteľná výška podvozku, "
          "nastaviteľná tuhosť, vysoký komfort jazdy, progresívna "
          "charakteristika."),
        s_answer_line,
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Prečo sa v súčasnosti od hydropneumatického pruženia "
        "postupne upúšťa?",
        s_body,
    ))
    story.append(Paragraph(
        A("Kvôli vysokým nákladom na výrobu a údržbu. Nahrádza ho "
          "pneumatické pruženie, ktoré je jednoduchšie a lacnejšie "
          "na údržbu."),
        s_answer_line,
    ))

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
