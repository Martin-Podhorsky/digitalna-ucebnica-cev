"""
Generátor pracovného listu: Hydraulický brzdový systém a Brzdové posilňovače

Použitie:  python generate_worksheet_hbs_bp.py
Výstup:    pracovny-list-hbs-bp.pdf

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
CONTENT_DIR = os.path.join(BASE_DIR, "content", "ucivo", "2-rocnik", "01-brzdy")
HBS_IMG = os.path.join(CONTENT_DIR, "hydraulicky-brzdovy-system", "hydraulicky-brzdovy-system.png")
OUTPUT = os.path.join(BASE_DIR, "pracovny-list-hbs-bp.pdf")

# ---------------------------------------------------------------------------
# Page setup
# ---------------------------------------------------------------------------
PAGE_W, PAGE_H = A4
MARGIN_LR = 1.5 * cm
MARGIN_TB = 1.2 * cm
UW = PAGE_W - 2 * MARGIN_LR

# ---------------------------------------------------------------------------
# Fonts (Windows Arial with Slovak diacritics support)
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

s_title = ParagraphStyle(
    "Title", fontName="FB", fontSize=14, leading=18,
    alignment=TA_CENTER, spaceAfter=4,
)
s_subtitle = ParagraphStyle(
    "Subtitle", fontName="FB", fontSize=11, leading=14,
    alignment=TA_CENTER, spaceAfter=2, textColor=RED,
)
s_header = ParagraphStyle("Header", fontName="F", fontSize=10, leading=13)
s_q = ParagraphStyle(
    "Q", fontName="FB", fontSize=11, leading=14,
    spaceBefore=6, spaceAfter=3, textColor=RED,
)
s_body = ParagraphStyle("Body", fontName="F", fontSize=10, leading=14, spaceAfter=1)
s_ans = ParagraphStyle("Ans", fontName="F", fontSize=10, leading=16)
s_match = ParagraphStyle("Match", fontName="F", fontSize=9.5, leading=13)
s_pn = ParagraphStyle("PN", fontName="F", fontSize=10, leading=17)
s_pnr = ParagraphStyle(
    "PNR", fontName="FB", fontSize=9, leading=17, alignment=TA_CENTER,
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


def answer_grid(items, cols=2):
    """Create a 2-column grid of numbered answer blanks."""
    rows = []
    for i in range(0, len(items), cols):
        row = []
        for j in range(cols):
            idx = i + j
            if idx < len(items):
                label = items[idx]
                row.append(Paragraph(f"<b>{label}</b> – {'_' * 40}", s_ans))
            else:
                row.append(Paragraph("", s_ans))
        rows.append(row)
    t = Table(rows, colWidths=[UW / cols] * cols)
    t.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


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
        "Pracovný list CEV: Hydraulický brzdový systém a Brzdové posilňovače",
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
    #  Q1 – Label the hydraulic braking system diagram
    # ================================================================
    story.append(Paragraph(
        "1) Popíš schému hydraulického brzdového systému:", s_q,
    ))
    story.append(scaled_img(HBS_IMG, UW * 0.65, max_h=8 * cm))
    story.append(Spacer(1, 3))
    story.append(answer_grid([str(i) for i in range(1, 10)]))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Fill in the blanks (principle of operation)
    # ================================================================
    story.append(Paragraph("2) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Keď vodič stlačí brzdový {BL}, piest v hlavnom brzdovom {BL} "
        f"vytvorí tlak v brzdovej {BL}. Tento tlak sa prenáša {BL} "
        f"do brzdových {BL} pri kolesách, kde posúva piesty. Piesty "
        f"pritláčajú brzdové {BL} na kotúče alebo brzdové {BL} "
        f"na bubny, čím vzniká trenie a {BL} sila.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q3 – Brake circuit arrangements
    # ================================================================
    story.append(Paragraph("3) Brzdové okruhy:", s_q))
    story.append(Paragraph(
        f"a) Koľko nezávislých brzdových okruhov musí mať prevádzková brzda? {BL}",
        s_body,
    ))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "b) Vymenuj 5 typov usporiadania brzdových okruhov:",
        s_body,
    ))
    ct = Table(
        [
            [
                Paragraph(f"1. {'_' * 25}", s_ans),
                Paragraph(f"2. {'_' * 25}", s_ans),
                Paragraph(f"3. {'_' * 25}", s_ans),
            ],
            [
                Paragraph(f"4. {'_' * 25}", s_ans),
                Paragraph(f"5. {'_' * 25}", s_ans),
                Paragraph("", s_ans),
            ],
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
    #  Q4 – True / False
    # ================================================================
    story.append(Paragraph("4) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt in [
        "Prevádzková brzda musí mať vždy dva samostatné brzdové okruhy.",
        "Obmedzovač brzdového účinku reguluje tlak v okruhu predných bŕzd.",
        "Nádržka na brzdovú kvapalinu by mala byť na ľahko dostupnom "
        "a viditeľnom mieste v motorovom priestore.",
        "Hydraulický brzdový systém prenáša brzdnú silu pomocou stlačeného vzduchu.",
    ]:
        story.append(pn_row(stmt))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q5 – Matching: brake booster parts → descriptions
    # ================================================================
    story.append(Paragraph(
        "5) Priraďovanie – priraď k názvu časti podtlakového brzdového "
        "posilňovača správny opis (zapíš písmeno):",
        s_q,
    ))

    parts_col = [
        ("1.", "Podtlaková komora", "___"),
        ("2.", "Membrána", "___"),
        ("3.", "Tanierový ventil", "___"),
        ("4.", "Prepúšťací kanál", "___"),
        ("5.", "Tlačná tyč", "___"),
        ("6.", "Reakčný kotúč", "___"),
    ]
    descs_col = [
        ("A)", "Prenáša výsledný tlak do hlavného brzdového valca."),
        ("B)", "Pri stlačení brzdového pedálu uzatvára prepúšťací kanál."),
        ("C)", "Je vložený v strede piestu; posúvaný silou z rozdielov tlakov."),
        ("D)", "Časť posilňovača, v ktorej je vytváraný podtlak."),
        ("E)", "Oddeľuje podtlakovú komoru od pracovnej a umožňuje pohyb piestu."),
        ("F)", "Prepúšťa podtlak z podtlakovej komory do pracovnej komory."),
    ]

    match_data = []
    header = [
        Paragraph("<b>Č.</b>", s_match),
        Paragraph("<b>Názov časti</b>", s_match),
        Paragraph("<b>Odp.</b>", s_match),
        Paragraph("", s_match),
        Paragraph("<b>Opis</b>", s_match),
    ]
    match_data.append(header)

    for i in range(len(parts_col)):
        num, name, blank = parts_col[i]
        d_letter, d_text = descs_col[i]
        match_data.append([
            Paragraph(num, s_match),
            Paragraph(name, s_match),
            Paragraph(blank, s_match),
            Paragraph(f"<b>{d_letter}</b>", s_match),
            Paragraph(d_text, s_match),
        ])

    col_widths = [0.04 * UW, 0.20 * UW, 0.06 * UW, 0.05 * UW, 0.65 * UW]
    mt = Table(match_data, colWidths=col_widths)
    mt.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("GRID", (0, 0), (2, -1), 0.5, black),
        ("GRID", (3, 0), (4, -1), 0.5, black),
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#F0F0F0")),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(mt)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – Fill in the blanks (brake booster principle)
    # ================================================================
    story.append(Paragraph("6) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Keď vodič nestláča brzdový pedál, v podtlakovej aj v {BL} komore "
        f"je rovnaký tlak ({BL}). Pri stlačení pedála sa do pracovnej komory "
        f"vpustí {BL} tlak a zablokuje sa {BL} kanál. "
        f"Rozdiel tlakov vytvára silu, ktorá tlačí na {BL} a prenáša sa "
        f"do hlavného brzdového valca pomocou {BL} tyče.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q7 – True / False
    # ================================================================
    story.append(Paragraph("7) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt in [
        "Brzdový posilňovač zosilňuje silu vyvinutú vodičom na brzdový pedál.",
        "Podtlakový posilňovač využíva podtlak z výfukového potrubia motora.",
        "Membrána oddeľuje podtlakovú komoru od pracovnej komory.",
        "Zosílenie brzdového posilňovača býva zvyčajne od 300% do 500%.",
        "Tanierový ventil pri stlačení brzdového pedálu otvára prepúšťací kanál.",
    ]:
        story.append(pn_row(stmt))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q8 – Short answers
    # ================================================================
    story.append(Paragraph("8) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Aká je hlavná funkcia brzdového posilňovača?", s_body,
    ))
    for _ in range(3):
        story.append(Spacer(1, 14))
        story.append(HRFlowable(width="100%", thickness=0.5, color=black))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Čo vyhodnocuje systém BAS a ako reaguje pri núdzovom brzdení?",
        s_body,
    ))
    for _ in range(3):
        story.append(Spacer(1, 14))
        story.append(HRFlowable(width="100%", thickness=0.5, color=black))

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
