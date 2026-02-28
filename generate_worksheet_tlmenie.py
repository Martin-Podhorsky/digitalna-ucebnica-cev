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
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE_DIR, "pracovny-list-tlmenie.pdf")

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
    #  Q1 – True / False (general damping info)
    # ================================================================
    story.append(Paragraph("1) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt in [
        "Tlmiče slúžia na zvýšenie únosnosti pružín pri veľkom zaťažení.",
        "Tlmiče premieňajú kinetickú energiu kmitania pružín na teplo.",
        "Jednoplášťový tlmič sa môže montovať v ľubovoľnej polohe.",
        "Dvojplášťový tlmič má lepšie chladenie ako jednoplášťový.",
        "Fading je jav, pri ktorom sa olej v tlmiči mieša so vzduchom "
        "a výrazne sa zníži tlmiaca schopnosť.",
    ]:
        story.append(pn_row(stmt))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Comparison table (twin-tube vs mono-tube)
    # ================================================================
    story.append(Paragraph(
        "2) Doplň porovnávaciu tabuľku (dvojplášťový vs. jednoplášťový tlmič):",
        s_q,
    ))
    props = [
        "Chladenie",
        "Odozva na nerovnosti",
        "Montážna poloha",
        "Komfort jazdy",
        "Výrobné náklady",
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
    ct = Table(cmp_data, colWidths=[UW * 0.30, UW * 0.35, UW * 0.35])
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
    #  Q3 – Fill in the blanks (twin-tube principle)
    # ================================================================
    story.append(Paragraph(
        "3) Doplň do textu (princíp činnosti dvojplášťového tlmiča):", s_q,
    ))
    story.append(Paragraph(
        f"Dvojplášťový tlmič sa skladá z dvoch valcov – {BL} a {BL}. "
        f"Pri stláčaní sa piest pohybuje nadol a vytláča hydraulickú "
        f"kvapalinu cez ventil z pod piesta nad piest. Pri {BL} sa piest "
        f"pohybuje nahor. Ventil B má spravidla {BL} prierez, aby tlmič "
        f"kládol väčší odpor pri rozťahovaní.",
        s_body,
    ))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q4 – Match descriptions to regulation types
    # ================================================================
    story.append(Paragraph(
        "4) Priraď opis k správnemu typu regulácie tlmenia (A, B alebo C):",
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
    #  Q5 – Fill in the blanks (MagneRide)
    # ================================================================
    story.append(Paragraph(
        "5) Doplň do textu (magnetoreologické tlmiče – MagneRide):", s_q,
    ))
    story.append(Paragraph(
        f"Magnetoreologická kvapalina obsahuje mikroskopické {BL} "
        f"častice rozptýlené v syntetickom oleji. Bez magnetického poľa "
        f"má kvapalina {BL} viskozitu ({BL} tlmenie). Keď "
        f"elektromagnetická cievka vytvorí magnetické pole, častice "
        f"sa zoradia do {BL} a vytvoria odpor proti prúdeniu. Tým sa "
        f"zvýši viskozita a tlmenie sa stane {BL}.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – Match system to manufacturer
    # ================================================================
    story.append(Paragraph(
        "6) Priraď systém adaptívneho tlmenia k jeho výrobcovi:", s_q,
    ))
    sys_data = [[
        Paragraph("<b>Systém</b>", s_table_b),
        Paragraph("<b>Výrobca</b>", s_table_b),
    ]]
    for sys_name in ["CDC (Continuous Damping Control)",
                     "DCC (Dynamic Chassis Control)",
                     "MagneRide",
                     "PASM (Porsche Active Suspension Management)"]:
        sys_data.append([
            Paragraph(sys_name, s_table),
            Paragraph("", s_table),
        ])
    st = Table(sys_data, colWidths=[UW * 0.55, UW * 0.45])
    st.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, black),
        ("BACKGROUND", (0, 0), (-1, 0), GRAY_BG),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(st)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q7 – Short answers
    # ================================================================
    story.append(Paragraph("7) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Uveď 3 úlohy tlmičov pruženia.",
        s_body,
    ))
    for _ in range(3):
        story += answer_line()
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Uveď 2 výhody magnetoreologických tlmičov oproti "
        "solenoidovým.",
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
