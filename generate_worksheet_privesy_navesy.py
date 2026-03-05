"""
Generátor pracovného listu: Prívesy a návesy

Použitie:  python generate_worksheet_privesy_navesy.py
Výstup:    pracovny-list-privesy-navesy.pdf

Požiadavky: pip install reportlab Pillow
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
IMG_DIR  = os.path.join(BASE_DIR, "content", "ucivo", "2-rocnik", "04-privesy-navesy")

IMG_AUTOBUS  = os.path.join(IMG_DIR, "autobusovy-prives.jpg")
IMG_PLACHTA  = os.path.join(IMG_DIR, "plachtovy-naves.jpg")
IMG_SKRINA   = os.path.join(IMG_DIR, "skrinovy-naves.jpg")
IMG_VALNIK   = os.path.join(IMG_DIR, "valnik.jpg")

OUTPUT = os.path.join(BASE_DIR, "Pracovny-list_privesy-navesy.pdf")

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
pdfmetrics.registerFont(TTFont("F",   os.path.join(FONT_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("FB",  os.path.join(FONT_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("FI",  os.path.join(FONT_DIR, "ariali.ttf")))
pdfmetrics.registerFont(TTFont("FBI", os.path.join(FONT_DIR, "arialbi.ttf")))
pdfmetrics.registerFontFamily("F", normal="F", bold="FB", italic="FI", boldItalic="FBI")

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------
RED        = HexColor("#CC0000")
GRAY_BG    = HexColor("#F0F0F0")
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
s_body    = ParagraphStyle("Body",  fontName="F",  fontSize=10, leading=14, spaceAfter=1)
s_pn      = ParagraphStyle("PN",    fontName="F",  fontSize=10, leading=17)
s_pnr     = ParagraphStyle(
    "PNR", fontName="FB", fontSize=9, leading=17, alignment=TA_CENTER,
)
s_table   = ParagraphStyle("Tbl",   fontName="F",  fontSize=10, leading=13)
s_table_b = ParagraphStyle("TblB",  fontName="FB", fontSize=10, leading=13)
s_table_c = ParagraphStyle(
    "TblC", fontName="F", fontSize=10, leading=13, alignment=TA_CENTER,
)
s_img_label = ParagraphStyle(
    "ImgLbl", fontName="FB", fontSize=9, leading=12, alignment=TA_CENTER,
)
s_match_lbl = ParagraphStyle(
    "MatchLbl", fontName="FB", fontSize=10, leading=13, alignment=TA_CENTER,
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
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN",         (1, 0), (1,  0),  "CENTER"),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
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
        topMargin=MARGIN_TB,  bottomMargin=MARGIN_TB,
    )
    story = []

    # ================================================================
    #  HEADER
    # ================================================================
    story.append(Paragraph(
        "Pracovný list CEV: Prívesy a návesy",
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
    #  Q1 – Vysvetli pojmy
    # ================================================================
    story.append(Paragraph("1) Vysvetli pojmy:", s_q))

    story.append(Paragraph(
        "a) Aký je hlavný rozdiel medzi prívesom a návesom?",
        s_body,
    ))
    for _ in range(3):
        story += answer_line()
    story.append(Spacer(1, 5))

    story.append(Paragraph(
        "b) Vysvetli, čo je to prítlak oja a prečo je dôležité, aby nebol príliš veľký ani príliš malý.",
        s_body,
    ))
    for _ in range(3):
        story += answer_line()
    story.append(Spacer(1, 5))

    # ================================================================
    #  Q2 – Match images to terms
    # ================================================================
    story.append(Paragraph(
        "2) Priraď každý obrázok (A – D) k správnemu názvu. "
        "Napíš písmeno obrázka na príslušný riadok.",
        s_q,
    ))

    imgs = [
        (IMG_SKRINA,  "A"),
        (IMG_VALNIK,  "B"),
        (IMG_AUTOBUS, "C"),
        (IMG_PLACHTA, "D"),
    ]

    COLS   = 4
    cell_w = UW / COLS
    img_h  = 3.6 * cm

    img_row = [scaled_img(p, cell_w * 0.90, max_h=img_h) for p, _ in imgs]
    lbl_row = [Paragraph(f"<b>{n}</b>", s_img_label)     for _, n  in imgs]

    grid = Table([img_row, lbl_row], colWidths=[cell_w] * COLS)
    grid.setStyle(TableStyle([
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(grid)
    story.append(Spacer(1, 4))

    # matching list – shuffled order
    terms = [
        "Valníkový náves",
        "Autobusový príves",
        "Plachtový náves",
        "Skriňový náves",
    ]
    half  = len(terms) // 2
    col_w = UW / 2
    match_rows = []
    for i in range(half):
        match_rows.append([
            Paragraph(terms[i],        s_table),
            Paragraph("_____",         s_match_lbl),
            Paragraph(terms[i + half], s_table),
            Paragraph("_____",         s_match_lbl),
        ])
    mt = Table(match_rows, colWidths=[col_w * 0.72, col_w * 0.28, col_w * 0.72, col_w * 0.28])
    mt.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LINEBEFORE",    (2, 0), (2,  -1), 0.5, HexColor("#AAAAAA")),
    ]))
    story.append(mt)
    story.append(Spacer(1, 5))

    # ================================================================
    #  Q3 – Comparison table: príves vs. náves
    # ================================================================
    story.append(Paragraph(
        "3) Doplň porovnávaciu tabuľku (príves vs. náves):",
        s_q,
    ))
    props = [
        "Predná náprava",
        "Spôsob pripojenia k ťažnému vozidlu",
        "Prenos hmotnosti na ťažné vozidlo",
        "Možnosť manipulácie bez ťažného vozidla",
        "Maximálna dĺžka celej súpravy",
    ]
    cmp_data = [[
        Paragraph("<b>Vlastnosť</b>", s_table_b),
        Paragraph("<b>Príves</b>",    s_table_b),
        Paragraph("<b>Náves</b>",     s_table_b),
    ]]
    for p in props:
        cmp_data.append([
            Paragraph(p, s_table),
            Paragraph("", s_table_c),
            Paragraph("", s_table_c),
        ])
    ct = Table(cmp_data, colWidths=[UW * 0.38, UW * 0.31, UW * 0.31])
    ct.setStyle(TableStyle([
        ("GRID",          (0, 0), (-1, -1), 0.5, black),
        ("BACKGROUND",    (0, 0), (-1,  0), GRAY_BG),
        ("BACKGROUND",    (0, 1), (0,  -1), LIGHT_GRAY),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    story.append(ct)

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q4 – True / False
    # ================================================================
    story.append(Paragraph("4) Rozhodni – Pravda / Nepravda:", s_q))
    statements = [
        "Príves aj náves sú prípojné vozidlá bez vlastného pohonu.",
        "Na ťažné vozidlo sa pri prívese prenáša 30 až 40 % jeho celkovej hmotnosti.",
        "Kráľovský čap je súčasťou ťahača a točnica je súčasťou návesu.",
        "Guľová spojka sa používa na ľahkých prívesoch a prívesných vozíkoch do 3,5 t.",
        "Pri samočinnom závese je pripojenie prívesu automatické a odpojenie ručné.",
        "Návesová súprava má lepšiu manévrovateľnosť ako prívesová súprava.",
        "Off-tracking je jav, kedy zadné kolesá prívesu sledujú presnú stopu predných kolies ťažného vozidla.",
        "Ak sa preťaží zadná časť návesu, jazdná súprava sa stáva veľmi nestabilnou.",
    ]
    for stmt in statements:
        story.append(pn_row(stmt))
    story.append(Spacer(1, 5))

    # ================================================================
    #  Q5 – Order the steps: postup pripájania návesu
    # ================================================================
    story.append(Paragraph(
        "5) Zoraď kroky správneho postupu pripájania návesu k ťahači. "
        "Napíš číslo 1 – 7 pred každý krok (1 = prvý krok):",
        s_q,
    ))
    steps = [
        "Zdvihni podporné nohy návesu.",
        "Pripoj vzduchové a elektrické vedenia.",
        "Ťahač cúva pod prednú časť návesu (náves je podopretý podpornými nohami).",
        "Skontroluj zaistenie točnice (vizuálne alebo podľa signalizácie).",
        "Vykonaj skúšku bŕzd a skontroluj funkčnosť osvetlenia.",
        "Kráľovský čap sa zasúva do V-drážky na točnici a čeľuste ho automaticky zachytia.",
        "Skontroluj, či je prípojné vozidlo zabrzdené a zabezpečené klinmi.",
    ]
    step_rows = []
    for step in steps:
        step_rows.append([
            Paragraph("_____", s_match_lbl),
            Paragraph(step, s_table),
        ])
    st = Table(step_rows, colWidths=[UW * 0.10, UW * 0.90])
    st.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LINEBELOW",     (0, 0), (-1, -2), 0.3, HexColor("#CCCCCC")),
    ]))
    story.append(st)
    story.append(Spacer(1, 5))

    # ================================================================
    #  Q6 – Short answers
    # ================================================================
    story.append(Paragraph("6) Krátke odpovede:", s_q))

    story.append(Paragraph(
        "a) Vysvetli jav off-tracking. Kedy k nemu dochádza a čo ho ovplyvňuje?",
        s_body,
    ))
    for _ in range(3):
        story += answer_line()
    story.append(Spacer(1, 5))

    story.append(Paragraph(
        "b) Uveď aspoň 4 činitele, ktoré ovplyvňujú manévrovateľnosť jazdnej súpravy:",
        s_body,
    ))
    for i in range(1, 5):
        story.append(Paragraph(f"{i}.", s_body))
        story += answer_line()
        story.append(Spacer(1, 2))

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
