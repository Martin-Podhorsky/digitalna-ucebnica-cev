"""
Generátor odpoveďového hárku: Tlmenie – teleskopické tlmiče a tlmiče s reguláciou

Použitie:  python generate_worksheet_tlmenie_answers.py
Výstup:    pracovny-list-tlmenie-odpovede.pdf

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
from reportlab.lib import pdfencrypt

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TWINTUBE_IMG = os.path.join(
    BASE_DIR, "content", "ucivo", "2-rocnik", "02-pruzenie-tlmenie",
    "tlmenie", "teleskopicke-tlmice", "twintube.png"
)
TWINTUBE_NUMBERED_IMG = os.path.join(
    BASE_DIR, "content", "ucivo", "2-rocnik", "02-pruzenie-tlmenie",
    "tlmenie", "teleskopicke-tlmice", "twin-tube-numbers.png"
)
OUTPUT = os.path.join(BASE_DIR, "Pracovny-list_tlmenie_odpovede.pdf")

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
s_answer_line = ParagraphStyle(
    "AnsLine", fontName="FI", fontSize=10, leading=14, textColor=BLUE,
)

BL = "_______________"


def A(text):
    return f'<i><font color="#0033AA">{text}</font></i>'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
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
    return [Spacer(1, 20), HRFlowable(width="100%", thickness=0.5, color=black)]


# ---------------------------------------------------------------------------
# Build the PDF
# ---------------------------------------------------------------------------
def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=A4,
        leftMargin=MARGIN_LR, rightMargin=MARGIN_LR,
        topMargin=MARGIN_TB, bottomMargin=MARGIN_TB,
        encrypt=pdfencrypt.StandardEncryption("skus-hadat-123", canPrint=1),
    )
    story = []

    # ================================================================
    #  HEADER
    # ================================================================
    story.append(Paragraph(
        "Pracovný list CEV: Tlmenie – teleskopické tlmiče a tlmiče "
        "s reguláciou – ODPOVEDE",
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
    IMG_H = 16.5 * cm
    img_obj = Image(TWINTUBE_NUMBERED_IMG, width=IMG_W, height=IMG_H)
    img_obj.hAlign = "CENTER"

    parts = [
        "1 – Vnútorný plášť",
        "2 – Vonkajší plášť",
        "3 – Piestnica",
        "4 – Piest s prietokovými jednocestnými ventilmi A a B",
        "5 – Pracovný priestor",
        "6 – Priestor zásobníka (vzduch alebo dusík)",
        "7 – Dno s prietokovými jednocestnými ventilmi C a D",
        "8 – Vedenie piestice",
        "9 – Tesnenie",
        "10 – Oká na uchytenie",
    ]
    s_part = ParagraphStyle(
        "Part", fontName="FI", fontSize=10, leading=15, textColor=BLUE,
    )
    parts_content = [Spacer(1, 4)]
    for p in parts:
        parts_content.append(Paragraph(f'<i><font color="#0033AA">{p}</font></i>', s_part))

    GAP = 0.9 * cm
    lines_col_w = UW - IMG_W - GAP

    from reportlab.platypus import KeepInFrame
    parts_frame = KeepInFrame(lines_col_w, IMG_H, parts_content, mode="shrink")

    side_tbl = Table(
        [[img_obj, parts_frame]],
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
    #  Q2 – True / False
    # ================================================================
    story.append(Paragraph("2) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt, ans in [
        ("Tlmiče slúžia na zvýšenie únosnosti pružín pri veľkom "
         "zaťažení.", False),
        ("Tlmiče premieňajú kinetickú energiu kmitania pružín na "
         "teplo.", True),
        ("Jednoplášťový tlmič sa môže montovať v ľubovoľnej polohe.",
         True),
        ("Dvojplášťový tlmič má lepšie chladenie ako jednoplášťový.",
         False),
        ("Fading tlmiča je jav, pri ktorom v dôsledku prehriatia "
         "dochádza k zníženiu viskozity oleja a k jeho prevzdušneniu "
         "či kavitácii (vzniku bublín), čo vedie k výraznej strate "
         "tlmiaceho účinku.", True),
    ]:
        story.append(pn_row(stmt, ans))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q3 – Comparison table
    # ================================================================
    story.append(Paragraph(
        "3) Doplň porovnávaciu tabuľku (dvojplášťový vs. jednoplášťový "
        "tlmič):",
        s_q,
    ))
    props_answers = [
        ("Chladenie (lepšie/horšie)", "Horšie", "Lepšie"),
        ("Odozva na nerovnosti (pomalšia/rýchlejšia)", "Pomalšia", "Rýchlejšia"),
        ("Montážna poloha", "Max. 45° od zvislice", "Ľubovoľná"),
        ("Výrobné náklady (menšie/väčšie)", "Menšie", "Väčšie"),
        ("Použitie", "Bežné osobné autá", "Športové, terénne, pretekárske"),
    ]
    cmp_data = [[
        Paragraph("<b>Vlastnosť</b>", s_table_b),
        Paragraph("<b>Dvojplášťový</b>", s_table_b),
        Paragraph("<b>Jednoplášťový</b>", s_table_b),
    ]]
    for p, d, j in props_answers:
        cmp_data.append([
            Paragraph(p, s_table),
            Paragraph(A(d), s_table_c),
            Paragraph(A(j), s_table_c),
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
        f"Dvojplášťový tlmič sa skladá z dvoch valcov (plášťov) – "
        f"{A('vnútorného pracovného valca (plášťa) a vonkajšieho zásobníkového valca (plášťa)')}. "
        f"Medzi týmito valcami sa nachádza priestor slúžiaci ako "
        f"{A('zásobník oleja')}. "
        f"Pri stláčaní sa piest pohybuje {A('nadol')} a vytláča hydraulickú "
        f"kvapalinu z pod piesta nad piest. Pri rozťahovaní sa piest pohybuje "
        f"{A('nahor')} a kvapalina prúdi z priestoru nad piestom do priestoru pod "
        f"piestom. Ventil, cez ktorý kvapalina preteká pri rozťahovaní, má "
        f"spravidla {A('menší')} prierez alebo {A('väčší')} tlak potrebný na "
        f"otvorenie, aby tlmič kládol {A('väčší')} odpor pri rozťahovaní ako "
        f"pri stláčaní.",
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

    descs_answers = [
        ("Vodič prepína medzi režimami Comfort / Normal / Sport "
         "pomocou tlačidla počas jazdy.", "B"),
        ("Mechanik nastavuje tvrdosť otáčaním regulátora "
         "pri stojacom vozidle.", "A"),
        ("Riadiaca jednotka automaticky a nepretržite "
         "upravuje tlmenie každého kolesa nezávisle.", "C"),
    ]
    match_data = []
    for i, (d, a) in enumerate(descs_answers, 1):
        match_data.append([
            Paragraph(f"{i}. {d}", s_match_desc),
            Paragraph(f"<b>{A(a)}</b>", s_match_lbl),
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
        f"Magnetoreologická kvapalina obsahuje "
        f"{A('mikroskopické kovové častice (železný prášok)')}. "
        f"V normálnom stave sa častice voľne pohybujú a kvapalina má "
        f"{A('nízku')} viskozitu. "
        f"Keď elektromagnetická cievka v pieste vytvorí magnetické pole, "
        f"kovové častice sa zoradia do reťazcov v smere magnetických siločiar. "
        f"Tieto reťazce vytvárajú odpor voči prúdeniu kvapaliny, čím sa "
        f"{A('zvyšuje')} jej zdanlivá viskozita a tým aj tlmiaca sila.",
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
    story.append(Paragraph(
        A("1) Rýchlo utlmiť kmitanie pružín po prejazde nerovnosťou; "
          "2) Zabrániť dlhodobému hojdaniu karosérie; "
          "3) Udržať kolesá v stálom kontakte s vozovkou; "
          "4) Zlepšiť stabilitu a ovládateľnosť vozidla; "
          "5) Zvýšiť komfort jazdy."),
        s_answer_line,
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Uveď 2 výhody magnetoreologických tlmičov oproti solenoidovým.",
        s_body,
    ))
    story.append(Paragraph(
        A("Rýchlejšia odozva, vyššia spoľahlivosť, plynulá regulácia, "
          "široký rozsah regulácie, tichá prevádzka."),
        s_answer_line,
    ))

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
