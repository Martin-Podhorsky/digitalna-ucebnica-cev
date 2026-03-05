"""
Generátor pracovného listu: Tlmenie – teleskopické tlmiče a tlmiče s reguláciou

Použitie:  python generate_worksheet_tlmenie.py
Výstup:    pracovny-list-tlmenie.pdf

Požiadavky: pip install reportlab
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
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
TWINTUBE_IMG = os.path.join(
    BASE_DIR, "content", "ucivo", "2-rocnik", "02-pruzenie-tlmenie",
    "tlmenie", "teleskopicke-tlmice", "twintube.png"
)
OUTPUT = os.path.join(BASE_DIR, "Pracovny-list_tlmenie.pdf")

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
LIGHT_GRAY = HexColor("#F8F8F8")

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
s_match_desc = ParagraphStyle("MatchDesc", fontName="F", fontSize=10, leading=13)
s_match_lbl = ParagraphStyle(
    "MatchLbl", fontName="FB", fontSize=10, leading=13, alignment=TA_CENTER,
)

BL = "_______________"
BL_SHORT = "_________"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
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
    return [Spacer(1, 20), HRFlowable(width="100%", thickness=0.5, color=black)]


def lines_block(n, width):
    """Return a Paragraph containing n stacked answer lines fitting given width."""
    items = []
    for _ in range(n):
        items += answer_line()
    return items


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
        "Pracovný list CEV: Tlmenie – teleskopické tlmiče a tlmiče s reguláciou",
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
    #  Q1 – Describe the twin-tube shock absorber from image
    #  Image on LEFT, answer lines on RIGHT
    # ================================================================
    story.append(Paragraph(
        "1) Vyznač a pomenuj jednotlivé časti dvojplášťového teleskopického tlmiča:",
        s_q,
    ))

    IMG_W = 5.5 * cm
    IMG_H = 16.5 * cm   # force tall render – shock content fills the height
    img_obj = Image(TWINTUBE_IMG, width=IMG_W, height=IMG_H)
    img_obj.hAlign = "CENTER"

    GAP = 0.9 * cm  # gap between image and lines (3× original 0.3 cm)
    lines_col_w = UW - IMG_W - GAP
    # ~23 lines to fill the full image height (16.5 cm / ~0.71 cm per line)
    line_rows = []
    for _ in range(23):
        line_rows.append([Spacer(1, 20)])
        line_rows.append([HRFlowable(width="100%", thickness=0.5, color=black)])
    lines_tbl = Table(line_rows, colWidths=[lines_col_w])
    lines_tbl.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))

    side_tbl = Table(
        [[img_obj, lines_tbl]],
        colWidths=[IMG_W + GAP, lines_col_w],
    )
    side_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(side_tbl)
    story.append(Spacer(1, 4))

    # ================================================================
    #  Q2 – True / False (general damping info)
    # ================================================================
    story.append(Paragraph("2) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt in [
        "Tlmiče slúžia na zvýšenie únosnosti pružín pri veľkom zaťažení.",
        "Tlmiče premieňajú kinetickú energiu kmitania pružín na teplo.",
        "Jednoplášťový tlmič sa môže montovať v ľubovoľnej polohe.",
        "Dvojplášťový tlmič má lepšie chladenie ako jednoplášťový.",
        "Fading tlmiča je jav, pri ktorom v dôsledku prehriatia dochádza "
        "k zníženiu viskozity oleja a k jeho prevzdušneniu či kavitácii "
        "(vzniku bublín), čo vedie k výraznej strate tlmiaceho účinku.",
    ]:
        story.append(pn_row(stmt))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q3 – Comparison table (twin-tube vs mono-tube)
    # ================================================================
    story.append(Paragraph(
        "3) Doplň porovnávaciu tabuľku (dvojplášťový vs. jednoplášťový tlmič):",
        s_q,
    ))
    props = [
        "Chladenie (lepšie/horšie)",
        "Odozva na nerovnosti (pomalšia/rýchlejšia)",
        "Montážna poloha",
        "Výrobné náklady (menšie/väčšie)",
        "Použitie",
    ]
    cmp_data = [[
        Paragraph("<b>Vlastnosť</b>", s_table_b),
        Paragraph("<b>Dvojplášťový</b>", s_table_b),
        Paragraph("<b>Jednoplášťový</b>", s_table_b),
    ]]
    for p in props:
        cmp_data.append([
            Paragraph(p, s_table),
            Paragraph("", s_table_c),
            Paragraph("", s_table_c),
        ])
    ct = Table(cmp_data, colWidths=[UW * 0.36, UW * 0.32, UW * 0.32])
    ct.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, black),
        ("BACKGROUND", (0, 0), (-1, 0), GRAY_BG),
        ("BACKGROUND", (0, 1), (0, -1), LIGHT_GRAY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(ct)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q4 – Fill in the blanks (twin-tube principle)
    # ================================================================
    story.append(Paragraph("4) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Dvojplášťový tlmič sa skladá z dvoch valcov (plášťov) – {BL}. "
        f"Medzi týmito valcami sa nachádza priestor slúžiaci ako {BL}. "
        f"Pri stláčaní sa piest pohybuje {BL} a vytláča hydraulickú "
        f"kvapalinu z pod piesta nad piest. Pri rozťahovaní sa piest pohybuje "
        f"{BL} a kvapalina prúdi z priestoru nad piestom do priestoru pod "
        f"piestom. Ventil, cez ktorý kvapalina preteká pri rozťahovaní, má "
        f"spravidla {BL} prierez alebo {BL} tlak potrebný na otvorenie, aby "
        f"tlmič kládol {BL} odpor pri rozťahovaní ako pri stláčaní.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q5 – Match descriptions to regulation types
    # ================================================================
    story.append(Paragraph(
        "5) Priraď opis k správnemu typu regulácie tlmenia (A, B alebo C):",
        s_q,
    ))
    story.append(Paragraph(
        "<b>A</b> – Manuálna regulácia &nbsp;&nbsp;&nbsp;&nbsp;"
        "<b>B</b> – Poloautomatická regulácia &nbsp;&nbsp;&nbsp;&nbsp;"
        "<b>C</b> – Aktívna (adaptívna) regulácia",
        s_body,
    ))
    story.append(Spacer(1, 2))

    descs = [
        "Vodič prepína medzi režimami Comfort / Normal / Sport "
        "pomocou tlačidla počas jazdy.",
        "Mechanik nastavuje tvrdosť otáčaním regulátora "
        "pri stojacom vozidle.",
        "Riadiaca jednotka automaticky a nepretržite "
        "upravuje tlmenie každého kolesa nezávisle.",
    ]
    match_data = []
    for i, d in enumerate(descs, 1):
        match_data.append([
            Paragraph(f"{i}. {d}", s_match_desc),
            Paragraph("____", s_match_lbl),
        ])
    mt = Table(match_data, colWidths=[UW * 0.88, UW * 0.12])
    mt.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, HexColor("#CCCCCC")),
    ]))
    story.append(mt)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – Fill in the blanks (MagneRide)
    # ================================================================
    story.append(Paragraph("6) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Magnetoreologická kvapalina obsahuje {BL}. "
        f"V normálnom stave sa častice voľne pohybujú a kvapalina má "
        f"{BL} viskozitu. "
        f"Keď elektromagnetická cievka v pieste vytvorí magnetické pole, "
        f"kovové častice sa zoradia do reťazcov v smere magnetických siločiar. "
        f"Tieto reťazce vytvárajú odpor voči prúdeniu kvapaliny, čím sa "
        f"{BL} jej zdanlivá viskozita a tým aj tlmiaca sila.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q7 – Short answers
    # ================================================================
    story.append(Paragraph("7) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Uveď aspoň 3 úlohy tlmičov pruženia.",
        s_body,
    ))
    for _ in range(3):
        story += answer_line()
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Uveď 2 výhody magnetoreologických tlmičov oproti solenoidovým.",
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
