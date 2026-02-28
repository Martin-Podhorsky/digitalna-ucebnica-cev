"""
Generátor pracovného listu S ODPOVEĎAMI: Vzduchotlakové (strojové) brzdy

Použitie:  python generate_worksheet_vzduchove_answers.py
Výstup:    pracovny-list-vzduchove-brzdy-odpovede.pdf

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
SCHEME_IMG = os.path.join(CONTENT_DIR, "vzduchove-brzdy", "air-brake-scheme.png")
OUTPUT = os.path.join(BASE_DIR, "pracovny-list-vzduchove-brzdy-odpovede.pdf")

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
BLUE = HexColor("#0044AA")
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
s_table_ans = ParagraphStyle(
    "TblAns", fontName="FI", fontSize=10, leading=13, textColor=BLUE,
)
s_answer_line = ParagraphStyle(
    "AnswerLine", fontName="FI", fontSize=10, leading=16, textColor=BLUE,
)


def A(text):
    return f'<i><font color="#0044AA">{text}</font></i>'


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
    label = f'<i><font color="#0044AA"><b>{answer}</b></font></i>'
    t = Table(
        [[Paragraph(statement, s_pn), Paragraph(label, s_pnr)]],
        colWidths=[UW * 0.73, UW * 0.27],
    )
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, 0), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
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
        f"Pracovný list CEV: Vzduchotlakové (strojové) brzdy – {A('ODPOVEDE')}",
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
    #  Q1 – Fill in the blanks (general + service brake principle)
    # ================================================================
    story.append(Paragraph("1) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Vzduchotlakové brzdy používajú na prenos sily od brzdového pedálu "
        f"{A('stlačený vzduch')} namiesto brzdovej kvapaliny. Používajú sa "
        f"pri ťažkých {A('nákladných vozidlách')}, {A('autobusoch')} "
        f"a súpravách s prívesmi. "
        f"Typický prevádzkový tlak je približne {A('6,9 až 8,3')} bar. "
        f"Keď vodič stlačí brzdový pedál, vzduch je vedený zo {A('zásobníka')} "
        f"do brzdových {A('komôr')} pri kolesách. Tlak vzduchu posunie "
        f"{A('membrány')}, ktoré pritlačia brzdové platničky na kotúče.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Label selected parts of the air brake scheme
    # ================================================================
    story.append(Paragraph(
        "2) Popíš vybrané časti schémy systému vzduchových bŕzd:", s_q,
    ))
    story.append(scaled_img(SCHEME_IMG, UW * 0.80, max_h=6 * cm))
    story.append(Spacer(1, 3))

    selected = [
        ("1", "Kompresor vzduchu"),
        ("3", "Sušič vzduchu"),
        ("5", "Štvorkanálový ochranný ventil"),
        ("6", "Prevádzkové zásobníky"),
        ("9", "Brzdový pedál (brzdový ventil)"),
        ("12", "Pružinové komory"),
    ]
    rows = []
    for i in range(0, len(selected), 2):
        num1, ans1 = selected[i]
        left = Paragraph(f"<b>{num1}</b> – {A(ans1)}", s_ans)
        if i + 1 < len(selected):
            num2, ans2 = selected[i + 1]
            right = Paragraph(f"<b>{num2}</b> – {A(ans2)}", s_ans)
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
    #  Q3 – Fill in the blanks (parking brake principle)
    # ================================================================
    story.append(Paragraph("3) Princíp parkovacej brzdy – doplň do textu:", s_q))
    story.append(Paragraph(
        f"Parkovacie brzdy fungujú {A('opačne')} ako prevádzkové – sú "
        f"držané v polohe brzdenia silnou {A('pružinou')}. Po naštartovaní "
        f"motora {A('kompresor')} vytvorí v systéme požadovaný tlak, ktorý "
        f"pružinu {A('stlačí')} a tým uvoľní brzdu. Pri náhlej strate tlaku "
        f"vzduchu sa pružina {A('uvoľní')} a okamžite aktivuje "
        f"{A('parkovaciu brzdu')}.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q4 – True / False
    # ================================================================
    story.append(Paragraph("4) Rozhodni – Pravda / Nepravda:", s_q))
    q4 = [
        ("Vzduchotlakové brzdy sa používajú predovšetkým pri osobných "
         "automobiloch.", "Nepravda"),
        ("Vzduch je nestlačiteľný, preto je reakcia vzduchových bŕzd okamžitá.",
         "Nepravda"),
        ("Sušič vzduchu odstraňuje vlhkosť, ktorá by v zime mohla zamrznúť "
         "a zablokovať ventily.", "Pravda"),
        ("Štvorkanálový ochranný ventil rozdeľuje vzduch do štyroch "
         "samostatných okruhov.", "Pravda"),
        ("Stlačený vzduch z nádrží sa dá využiť aj na iné účely, napr. na "
         "pohon klaksónu alebo dohusťovanie pneumatík.", "Pravda"),
    ]
    for stmt, ans in q4:
        story.append(pn_row(stmt, ans))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q5 – Advantages and disadvantages table
    # ================================================================
    story.append(Paragraph(
        "5) Napíš 3 výhody a 3 nevýhody vzduchotlakových bŕzd:", s_q,
    ))
    adv_data = [
        [Paragraph("<b>Výhody</b>", s_table_b),
         Paragraph("<b>Nevýhody</b>", s_table_b)],
        [Paragraph(f"1. {A('Veľká brzdná sila')}", s_table_ans),
         Paragraph(f"1. {A('Pomalšia reakcia (brake lag)')}", s_table_ans)],
        [Paragraph(f"2. {A('Odolnosť voči malým únikom')}", s_table_ans),
         Paragraph(f"2. {A('Vysoká cena a zložitosť')}", s_table_ans)],
        [Paragraph(f"3. {A('Jednoduché prepojenie s prívesmi')}", s_table_ans),
         Paragraph(f"3. {A('Hlučnosť')}", s_table_ans)],
    ]
    at = Table(adv_data, colWidths=[UW * 0.5] * 2, rowHeights=[20, 35, 35, 35])
    at.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, black),
        ("BACKGROUND", (0, 0), (-1, 0), GRAY_BG),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(at)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – Short answers
    # ================================================================
    story.append(Paragraph("6) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Prečo sú moderné vzduchotlakové brzdové systémy vždy dvojokruhové?",
        s_body,
    ))
    story.append(Paragraph(
        A("Pre bezpečnosť – pri poruche jedného okruhu zostáva druhý plne "
          "funkčný. Štvorkanálový ochranný ventil automaticky izoluje poškodený "
          "okruh, čím sa zabráni strate tlaku v celom systéme."),
        s_answer_line,
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Prečo majú vzduchotlakové brzdy pomalšiu reakciu (brake lag) "
        "ako hydraulické brzdy?",
        s_body,
    ))
    story.append(Paragraph(
        A("Pretože vzduch je stlačiteľný, takže trvá dlhšie (približne 0,5 "
          "sekundy), kým sa tlak prenesie k brzdám. Hydraulická kvapalina je "
          "nestlačiteľná, takže prenos sily je okamžitý."),
        s_answer_line,
    ))

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
