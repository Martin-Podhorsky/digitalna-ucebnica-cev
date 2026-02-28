"""
Generátor pracovného listu: Pruženie a tlmenie – listové, vinuté pružiny, skrutné tyče

Použitie:  python generate_worksheet_pruzenie.py
Výstup:    pracovny-list-pruzenie.pdf

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
LEAF_IMG = os.path.join(CONTENT_DIR, "listove-pruziny", "listova-pruzina-casti.png")
OUTPUT = os.path.join(BASE_DIR, "pracovny-list-pruzenie.pdf")

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
s_table_c = ParagraphStyle("TblC", fontName="F", fontSize=10, leading=13, alignment=TA_CENTER)

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
        "Pracovný list CEV: Pruženie – listové, vinuté pružiny a skrutné tyče",
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
    story.append(Paragraph("1) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Pruženie a tlmenie vozidla je súbor komponentov, ktoré spájajú "
        f"{BL} vozidla s {BL} tak, že umožnujú ich vzájomné pohybovanie "
        f"sa. Jednou z požiadaviek je stály kontakt kolies s vozovkou, pretože "
        f"je nevyhnutný pre efektívne {BL}, {BL} a prenos hnacích síl. "
        f"Hmotnosť komponentov pod pružinami sa nazýva {BL} hmotnosť.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – List the 6 types of suspension springs
    # ================================================================
    story.append(Paragraph("2) Vymenuj 6 druhov pruženia:", s_q))
    ct = Table(
        [
            [Paragraph(f"1. {'_' * 25}", s_ans),
             Paragraph(f"2. {'_' * 25}", s_ans),
             Paragraph(f"3. {'_' * 25}", s_ans)],
            [Paragraph(f"4. {'_' * 25}", s_ans),
             Paragraph(f"5. {'_' * 25}", s_ans),
             Paragraph(f"6. {'_' * 25}", s_ans)],
        ],
        colWidths=[UW / 3] * 3,
    )
    ct.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(ct)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q3 – Label the leaf spring diagram (all 9 parts)
    # ================================================================
    story.append(Paragraph(
        "3) Popíš časti listovej pružiny:", s_q,
    ))
    story.append(scaled_img(LEAF_IMG, UW * 0.68, max_h=6.5 * cm))
    story.append(Spacer(1, 3))

    rows = []
    for i in range(1, 10, 2):
        left = Paragraph(f"<b>{i}</b> – {'_' * 42}", s_ans)
        if i + 1 <= 9:
            right = Paragraph(f"<b>{i+1}</b> – {'_' * 42}", s_ans)
        else:
            right = Paragraph("", s_ans)
        rows.append([left, right])
    t = Table(rows, colWidths=[UW * 0.5] * 2)
    t.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q4 – Parameters affecting coil spring stiffness
    # ================================================================
    story.append(Paragraph(
        "4) Uveď 4 parametre, ktoré ovplyvňujú tuhosť vinutej pružiny:",
        s_q,
    ))
    pt = Table(
        [
            [Paragraph(f"1. {'_' * 35}", s_ans),
             Paragraph(f"2. {'_' * 35}", s_ans)],
            [Paragraph(f"3. {'_' * 35}", s_ans),
             Paragraph(f"4. {'_' * 35}", s_ans)],
        ],
        colWidths=[UW * 0.5] * 2,
    )
    pt.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(pt)

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q5 – Match properties to spring types
    # ================================================================
    story.append(Paragraph(
        "5) Priraď vlastnosť k správnemu druhu pruženia (zaškrtni):", s_q,
    ))
    props = [
        "Samotlmiaca schopnosť",
        "Najvyšší jazdný komfort",
        "Najvyššia únosnosť",
        "Jednoduché nastavenie výšky podvozku",
        "Samovodiaca funkcia (vedie nápravu)",
        "Najmenšie rozmery a hmotnosť",
    ]
    match_data = [[
        Paragraph("<b>Vlastnosť</b>", s_table_b),
        Paragraph("<b>Listové</b>", s_table_b),
        Paragraph("<b>Vinuté</b>", s_table_b),
        Paragraph("<b>Skrutné</b>", s_table_b),
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
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – True / False
    # ================================================================
    story.append(Paragraph("6) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt in [
        "Listové pružiny sa dnes používajú predovšetkým na osobných "
        "automobiloch.",
        "Trenie medzi listami listovej pružiny spôsobuje jej samotlmiaci "
        "efekt.",
        "Vinuté pružiny dokážu sami o sebe viesť nápravu bez ďalších "
        "komponentov.",
        "Skrutná tyč funguje na princípe odporu voči krúteniu (torzii).",
        "Stabilizačné tyče zmäkčujú pruženie a zvyšujú naklonenie "
        "karosérie v zákrutách.",
    ]:
        story.append(pn_row(stmt))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q7 – Short answers
    # ================================================================
    story.append(Paragraph("7) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Vysvetli princíp fungovania skrutnej (torznej) tyče.",
        s_body,
    ))
    for _ in range(3):
        story += answer_line()
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Na čo slúžia stabilizačné tyče (anti-roll bars)?",
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
