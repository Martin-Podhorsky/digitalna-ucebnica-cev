"""
Generátor pracovného listu: Pruženie – pneumatické, hydropneumatické a gumové pruženie

Použitie:  python generate_worksheet_pruzenie2.py
Výstup:    pracovny-list-pruzenie2.pdf

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
OUTPUT = os.path.join(BASE_DIR, "Pracovny-list_pneu-hydropneu-gumove.pdf")

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

BL = "_______________"


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


def pn_row(statement):
    t = Table(
        [[Paragraph(statement, s_pn), Paragraph("<b>Pravda / Nepravda</b>", s_pnr)]],
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
        "Pracovný list CEV: Pneumatické, hydropneumatické a gumové pruženie",
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
    #  Q1 – Label pneumatic suspension diagram (all 8 parts)
    # ================================================================
    story.append(Paragraph(
        "1) Popíš časti pneumatického pruženia:", s_q,
    ))
    story.append(scaled_img(PNEUM_IMG, UW * 0.85, max_h=8.2 * cm))
    story.append(Spacer(1, 3))

    rows = []
    for i in range(1, 9, 2):
        left = Paragraph(f"<b>{i}</b> – {'_' * 42}", s_ans)
        right = Paragraph(f"<b>{i+1}</b> – {'_' * 42}", s_ans)
        rows.append([left, right])
    t = Table(rows, colWidths=[UW * 0.5] * 2)
    t.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Fill in the blanks (pneumatické pruženie – principle)
    # ================================================================
    story.append(Paragraph("2) Doplň do textu (pneumatické pruženie):", s_q))
    story.append(Paragraph(
        f"Snímače výšky sledujú {BL}. Keď sa zmení zaťaženie "
        f"(napr. do vozidla nastúpi ďalší cestujúci), {BL} vyhodnotí "
        f"údaje zo snímačov a aktivovaním {BL} upraví tlak vzduchu "
        f"v mechoch.",
        s_body,
    ))

    # ================================================================
    #  Q3 – Fill in the blanks (hydropneumatické pruženie)
    # ================================================================
    story.append(Paragraph("3) Doplň do textu (hydropneumatické pruženie):", s_q))
    story.append(Paragraph(
        f"Hydropneumatické pruženie kombinuje {BL}. "
        f"Vyvinula ho spoločnosť {BL}. "
        f"Vo vnútri hydropneumatickej gule sa nachádza {BL} "
        f"a {BL}, oddelené {BL}. Tlmenie je "
        f"zabezpečené {BL}.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q4 – Match properties/characteristics to suspension types
    # ================================================================
    story.append(Paragraph(
        "4) Priraď vlastnosť/charakteristiku k správnemu druhu pruženia (zaškrtni):", s_q,
    ))
    props = [
        "Stála svetlá výška bez ohľadu na zaťaženie",
        "Progresívna charakteristika",
        "Samotlmiaci efekt",
        "Izolácia hluku a vibrácií",
        "Vysoké servisné náklady",
        "Nízka cena a jednoduchá výroba",
    ]
    match_data = [[
        Paragraph("<b>Vlastnosť / charakteristika</b>", s_table_b),
        Paragraph("<b>Pneum.</b>", s_table_b),
        Paragraph("<b>Hydropn.</b>", s_table_b),
        Paragraph("<b>Gumové</b>", s_table_b),
    ]]
    for p in props:
        match_data.append([
            Paragraph(p, s_table),
            Paragraph("", s_table_c),
            Paragraph("", s_table_c),
            Paragraph("", s_table_c),
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

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q5 – True / False
    # ================================================================
    story.append(Paragraph("5) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt in [
        "Pneumatické pruženie sa používa výhradne na malých "
        "osobných automobiloch.",
        "Silentblok je jedným z príkladov gumového pruženia.",
        "Hydropneumatické pruženie nepotrebuje samostatné tlmiče, pretože "
        "tlmenie zabezpečujú jednocestné ventily.",
        "Pri pneumatickom pružení sa vlnovcové mechy používajú prevažne "
        "v nákladných automobiloch a autobusoch.",
        "Starnutie gumy je spôsobené UV žiarením.",
    ]:
        story.append(pn_row(stmt))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – Short answers
    # ================================================================
    story.append(Paragraph("6) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Uveď 4 výhody pneumatického pruženia.",
        s_body,
    ))
    for _ in range(3):
        story += answer_line()
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Prečo sa v súčasnosti od hydropneumatického pruženia "
        "postupne upúšťa?",
        s_body,
    ))
    for _ in range(3):
        story += answer_line()

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
