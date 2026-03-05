"""
Generátor odpoveďového hárku: Geometria riadenia kolies

Použitie:  python generate_worksheet_geometria_riadenia_answers.py
Výstup:    pracovny-list-geometria-riadenia-odpovede.pdf

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
from reportlab.lib import pdfencrypt

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "content", "ucivo", "2-rocnik", "03-riadenie", "geometria-riadenia")

IMG_ZBIEHAVOST   = os.path.join(IMG_DIR, "zbiehavost_use-for-pdf.jpg")
IMG_ROZBIEHAVOST = os.path.join(IMG_DIR, "rozbiehavost_use-for-pdf.jpg")
IMG_ODKLON       = os.path.join(IMG_DIR, "odklon-priklon.jpg")
IMG_PRIKLON      = os.path.join(IMG_DIR, "priklon-osi-riadenia_use-for-pdf.jpg")
IMG_ZAKLON       = os.path.join(IMG_DIR, "zaklon-osi-riadenia_use-for-pdf.png")
IMG_ZAVLEK       = os.path.join(IMG_DIR, "zavlek_use-for-pdf.png")
IMG_POLOMER      = os.path.join(IMG_DIR, "polomer-riadenia_use-for-pdf.jpg")
IMG_DIFERENCNY   = os.path.join(IMG_DIR, "diferencny-uhol.jpg")
IMG_ROZCHOD      = os.path.join(IMG_DIR, "rozchod.jpg")
IMG_RAZVOR       = os.path.join(IMG_DIR, "razvor.jpg")

OUTPUT = os.path.join(BASE_DIR, "Pracovny-list_geometria-riadenia_odpovede.pdf")

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
RED      = HexColor("#CC0000")
BLUE     = HexColor("#0033AA")
GRAY_BG  = HexColor("#F0F0F0")
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
s_body  = ParagraphStyle("Body",  fontName="F",  fontSize=10, leading=14, spaceAfter=1)
s_pn    = ParagraphStyle("PN",    fontName="F",  fontSize=10, leading=17)
s_pnr   = ParagraphStyle(
    "PNR", fontName="FB", fontSize=9, leading=17, alignment=TA_CENTER,
)
s_table   = ParagraphStyle("Tbl",  fontName="F",  fontSize=10, leading=13)
s_table_b = ParagraphStyle("TblB", fontName="FB", fontSize=10, leading=13)
s_table_c = ParagraphStyle(
    "TblC", fontName="F", fontSize=10, leading=13, alignment=TA_CENTER,
)
s_img_label = ParagraphStyle(
    "ImgLbl", fontName="FB", fontSize=9, leading=12, alignment=TA_CENTER,
)
s_match_lbl = ParagraphStyle(
    "MatchLbl", fontName="FB", fontSize=10, leading=13, alignment=TA_CENTER,
)
s_answer_line = ParagraphStyle(
    "AnsLine", fontName="FI", fontSize=10, leading=14, textColor=BLUE,
)
s_small = ParagraphStyle("Small", fontName="F", fontSize=9, leading=12)

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
        encrypt=pdfencrypt.StandardEncryption("skus-hadat-123", canPrint=1),
    )
    story = []

    # ================================================================
    #  HEADER
    # ================================================================
    story.append(Paragraph(
        "Pracovný list CEV: Geometria riadenia kolies – ODPOVEDE",
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
    #  Q1 – Short answer: definition and purpose
    # ================================================================
    story.append(Paragraph("1) Vysvetli pojmy:", s_q))
    story.append(Paragraph(
        "a) Čo je geometria riadenia kolies a prečo je dôležitá?",
        s_body,
    ))
    story.append(Paragraph(
        A("Geometria riadenia je súbor uhlov a rozmerov, ktoré určujú polohu kolies "
          "voči vozovke a karosérii vozidla. Tieto parametre majú zásadný vplyv na "
          "jazdné vlastnosti, opotrebovanie pneumatík a bezpečnosť jazdy."),
        s_answer_line,
    ))
    story.append(Spacer(1, 5))

    story.append(Paragraph(
        "b) Uveď 3 javy, ktoré správne nastavená geometria kolies zabezpečuje:",
        s_body,
    ))
    answers_1b = [
        "Rovnomerné odvaľovanie pneumatík po vozovke bez bočného šmyku, čím sa predlžuje ich životnosť a znižuje spotreba paliva.",
        "Stabilitu vozidla v priamom smere.",
        "Samovoľné vracanie kolies do priameho smeru po prejazde zákrutou.",
    ]
    for i, ans in enumerate(answers_1b, 1):
        story.append(Paragraph(f"{i}.", s_body))
        story.append(Paragraph(A(ans), s_answer_line))
        story.append(Spacer(1, 2))

    # ================================================================
    #  Q2 – Match images to terms
    # ================================================================
    story.append(Paragraph(
        "2) Priraď každý obrázok (1 – 10) k správnemu názvu parametra geometrie riadenia. "
        "Napíš číslo obrázka na príslušný riadok.",
        s_q,
    ))

    imgs = [
        (IMG_ZBIEHAVOST,   "1"),
        (IMG_ROZBIEHAVOST, "2"),
        (IMG_ODKLON,       "3"),
        (IMG_PRIKLON,      "4"),
        (IMG_ZAKLON,       "5"),
        (IMG_ZAVLEK,       "6"),
        (IMG_POLOMER,      "7"),
        (IMG_DIFERENCNY,   "8"),
        (IMG_ROZCHOD,      "9"),
        (IMG_RAZVOR,       "10"),
    ]

    COLS  = 4
    cell_w = UW / COLS
    img_h  = 3.8 * cm

    row1_imgs = [scaled_img(p, cell_w * 0.88, max_h=img_h) for p, _ in imgs[:4]]
    row1_lbls = [Paragraph(f"<b>{n}</b>", s_img_label)     for _, n  in imgs[:4]]
    row2_imgs = [scaled_img(p, cell_w * 0.88, max_h=img_h) for p, _ in imgs[4:8]]
    row2_lbls = [Paragraph(f"<b>{n}</b>", s_img_label)     for _, n  in imgs[4:8]]
    row3_imgs = [scaled_img(p, cell_w * 0.88, max_h=img_h) for p, _ in imgs[8:]]
    row3_imgs += [Paragraph("", s_img_label)] * (COLS - len(row3_imgs))
    row3_lbls = [Paragraph(f"<b>{n}</b>", s_img_label) for _, n in imgs[8:]]
    row3_lbls += [Paragraph("", s_img_label)] * (COLS - len(row3_lbls))

    grid = Table(
        [row1_imgs, row1_lbls, row2_imgs, row2_lbls, row3_imgs, row3_lbls],
        colWidths=[cell_w] * COLS,
    )
    grid.setStyle(TableStyle([
        ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(grid)
    story.append(Spacer(1, 4))

    # correct answers: term → image number (2-column layout)
    terms_answers = [
        ("Polomer riadenia",           "7"),
        ("Rázvor náprav",             "10"),
        ("Záklon osi riadenia",        "5"),
        ("Rozbiehavosť kolies",        "2"),
        ("Diferenčný uhol",            "8"),
        ("Odklon kolesa",              "3"),
        ("Rozchod kolies",             "9"),
        ("Závlek kolesa",              "6"),
        ("Príklon osi riadenia",       "4"),
        ("Zbiehavosť kolies",          "1"),
    ]
    half = len(terms_answers) // 2
    col_w = UW / 2
    match_rows = []
    for i in range(half):
        lt, la = terms_answers[i]
        rt, ra = terms_answers[i + half]
        match_rows.append([
            Paragraph(lt, s_table),
            Paragraph(f"<b>{A(la)}</b>", s_match_lbl),
            Paragraph(rt, s_table),
            Paragraph(f"<b>{A(ra)}</b>", s_match_lbl),
        ])
    mt = Table(match_rows, colWidths=[col_w * 0.72, col_w * 0.28, col_w * 0.72, col_w * 0.28])
    mt.setStyle(TableStyle([
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LINEBELOW",     (0, 0), (-1, -2), 0.3, HexColor("#CCCCCC")),
        ("LINEBEFORE",    (2, 0), (2,  -1), 0.5, HexColor("#AAAAAA")),
    ]))
    story.append(mt)

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q3 – True / False
    # ================================================================
    story.append(Paragraph("3) Rozhodni – Pravda / Nepravda:", s_q))
    pn_data = [
        ("Zbiehavosť kolies zlepšuje stabilitu vozidla v priamom smere jazdy.", True),
        ("Negatívny odklon kolesa zlepšuje priľnavosť pneumatík v zákrutách.", True),
        ("Príklon osi riadenia sa meria pri pohľade zboku na vozidlo.", False),
        ("Pozitívny záklon osi riadenia je hlavným faktorom zabezpečujúcim samovoľné vracanie kolies do priameho smeru.", True),
        ("Závlek kolesa je priamym dôsledkom príklonu osi riadenia.", False),
        ("Negatívny polomer riadenia je štandardom pre moderné vozidlá s predným náhonom a systémom ABS.", True),
    ]
    for stmt, ans in pn_data:
        story.append(pn_row(stmt, ans))
    story.append(Spacer(1, 4))

    # ================================================================
    #  Q4 – Short analytical questions (renumbered from Q5)
    # ================================================================
    story.append(Paragraph("4) Krátke odpovede:", s_q))

    story.append(Paragraph(
        "a) Vysvetli rozdiel medzi závlekom kolesa a polomerom riadenia. "
        "V čom sa líšia – ako sa merajú a čo každý z nich ovplyvňuje?",
        s_body,
    ))
    story.append(Paragraph(
        A("Závlek kolesa je vzdialenosť medzi bodom, kde predĺžená os riadenia "
          "pretína vozovku, a stredom dotykovej plochy pneumatiky, meraná v pozdĺžnom "
          "smere vozidla – teda pri pohľade zboku. Je dôsledkom záklonu osi riadenia "
          "a ovplyvňuje samovoľné vracanie kolies do priameho smeru a stabilitu "
          "pri vyšších rýchlostiach. "
          "Polomer riadenia je tá istá vzdialenosť, ale meraná v priečnom smere "
          "vozidla – teda pri pohľade spredu. Je dôsledkom príklonu osi riadenia "
          "a ovplyvňuje spätnú väzbu od vozovky, ťahanie vozidla pri brzdení a sily "
          "v riadení pri akcelerácii vozidiel s predným náhonom."),
        s_answer_line,
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "b) Prečo musí pri prejazde zákrutou vnútorné koleso zvierať väčší uhol "
        "natočenia ako vonkajšie? Ako sa tento požiadavok technicky rieši?",
        s_body,
    ))
    story.append(Paragraph(
        A("Vnútorné koleso opisuje oblúk s menším polomerom ako vonkajšie, preto sa "
          "musí natočiť o väčší uhol, aby sa obe kolesá odvaľovali bez bočného šmyku. "
          "Rozdiel týchto uhlov sa nazýva diferenčný uhol (Ackermannova geometria). "
          "Technicky sa dosahuje vhodným sklonom riadiacich ramien – tzv. lichobežníkovým "
          "usporiadaním riadenia, kde sú riadiace ramená naklonené tak, že pri natáčaní "
          "vnútorné koleso automaticky zviera väčší uhol."),
        s_answer_line,
    ))
    story.append(Spacer(1, 4))

    # ================================================================
    #  Q5 – Consequences of incorrect geometry (renumbered from Q6)
    # ================================================================
    story.append(Paragraph(
        "5) Doplň tabuľku – aké dôsledky má nesprávne nastavenie daného parametra:",
        s_q,
    ))
    cons_answers = [
        (
            "Nadmerná zbiehavosť",
            "Zvýšené opotrebovanie vonkajších hrán pneumatík.",
        ),
        (
            "Nadmerná rozbiehavosť",
            "Nestabilita vozidla v priamom smere; zvýšené opotrebovanie vnútorných hrán pneumatík.",
        ),
        (
            "Nadmerný pozitívny odklon",
            "Opotrebovanie vonkajšej hrany pneumatiky; pri naloženom vozidle sa kolesá vychyľujú nadmerne von.",
        ),
        (
            "Nadmerný negatívny odklon",
            "Pneumatika sa v priamom smere dotýka vozovky len vnútornou hranou – zhoršuje brzdenie, akceleráciu a spôsobuje rýchle opotrebovanie vnútornej strany pneumatiky.",
        ),
        (
            "Nesymetrický záklon (rozdielny ľavý / pravý)",
            "Vozidlo ťahá do strany (k strane s menším zákonom).",
        ),
    ]
    cons_data = [[
        Paragraph("<b>Parameter</b>", s_table_b),
        Paragraph("<b>Dôsledok (čo sa stane?)</b>", s_table_b),
    ]]
    for p, ans in cons_answers:
        cons_data.append([
            Paragraph(p, s_table),
            Paragraph(A(ans), s_table),
        ])
    ct3 = Table(cons_data, colWidths=[UW * 0.38, UW * 0.62])
    ct3.setStyle(TableStyle([
        ("GRID",          (0, 0), (-1, -1), 0.5, black),
        ("BACKGROUND",    (0, 0), (-1,  0), GRAY_BG),
        ("BACKGROUND",    (0, 1), (0,  -1), LIGHT_GRAY),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 5),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 5),
    ]))
    story.append(ct3)

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
