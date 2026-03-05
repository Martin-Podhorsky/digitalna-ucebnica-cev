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
from reportlab.lib import pdfencrypt

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, "content", "ucivo", "2-rocnik", "01-brzdy")
SCHEME_IMG = os.path.join(CONTENT_DIR, "vzduchove-brzdy", "air-brake-scheme.png")
OUTPUT = os.path.join(BASE_DIR, "Pracovny-list_vzduchove-brzdy_odpovede.pdf")

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
    "TblAns", fontName="FI", fontSize=9.5, leading=12, textColor=BLUE,
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
        encrypt=pdfencrypt.StandardEncryption("skus-hadat-123", canPrint=1),
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
    #  Q1 – Fill in the blanks (service brake + parking brake)
    # ================================================================
    story.append(Paragraph("1) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Keď vodič stlačí brzdový pedál, vzduch je pod tlakom vedený zo "
        f"{A('zásobníka')} do {A('brzdových komôr')} pri kolesách. Tlak vzduchu "
        f"posunie membrány alebo piesty, ktoré pritlačia brzdové doštičky alebo "
        f"čeľuste na {A('kotúče alebo bubny')}. Po uvoľnení pedála sa stlačený "
        f"vzduch {A('vypustí do atmosféry')} "
        f"a vratné pružiny vrátia brzdové doštičky/čeľuste do pôvodnej pozície.",
        s_body,
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        f"Parkovacie brzdy fungujú {A('opačným')} spôsobom. Brzdy sú držané "
        f"v polohe brzdenia silnou pružinou a po naštartovaní motora, keď "
        f"kompresor vytvorí v systéme požadovaný tlak vzduchu, tento tlak "
        f"pružinu {A('stlačí')} a tým {A('uvoľní')} brzdu. Pri náhlej strate "
        f"tlaku vzduchu sa pružina {A('uvoľní')} a okamžite aktivuje parkovaciu "
        f"brzdu (kvôli bezpečnosti).",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Label selected parts of the air brake scheme
    # ================================================================
    story.append(Paragraph(
        "2) Popíš vybrané časti schémy systému vzduchových bŕzd:", s_q,
    ))
    story.append(scaled_img(SCHEME_IMG, UW * 0.98, max_h=11 * cm))
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

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q3 – True / False
    # ================================================================
    story.append(Paragraph("3) Rozhodni – Pravda / Nepravda:", s_q))
    q3 = [
        ("Vzduchotlakové brzdy sa používajú predovšetkým pri osobných "
         "automobiloch.", "Nepravda"),
        ("Vzduch je stlačiteľný, preto je reakcia vzduchových bŕzd okamžitá.",
         "Nepravda"),
        ("Sušič vzduchu slúži na zachytávanie vlhkosti.", "Pravda"),
        ("Menší únik vzduchu pri strojových brzdách nie je kritický.", "Pravda"),
        ("Stlačený vzduch z nádrží sa dá využiť aj na iné účely, napr. na "
         "pohon klaksónu alebo dohusťovanie pneumatík.", "Pravda"),
    ]
    for stmt, ans in q3:
        story.append(pn_row(stmt, ans))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q4 – Advantages and disadvantages table (full answer key)
    # ================================================================
    story.append(Paragraph(
        "4) Napíš 3 výhody a 3 nevýhody vzduchotlakových bŕzd:", s_q,
    ))
    advantages = [
        "Veľká brzdná sila",
        "Odolnosť voči malým únikom",
        "Jednoduché prepojenie s prívesmi",
        "Neobmedzené médium",
        "Viacúčelovosť (napr. dohusťovanie pneumatík)",
        "Vyššia odolnosť voči prehriatiu",
    ]
    disadvantages = [
        "Pomalšia reakcia (Brake Lag) – vzduch je stlačiteľný",
        "Vysoká cena a zložitosť",
        "Po dlhšom státí musí vodič počkať, kým sa systém natlakuje",
        "Náchylnosť na mráz – zlyhanie sušiča môže vyradiť brzdy",
        "Hlučnosť – hlasné odfúknutie pri uvoľnení brzdy",
        "Veľké rozmery a hmotnosť",
        "Pri poruche okruhu sa aktivujú parkovacie brzdy",
    ]
    adv_data = [[
        Paragraph("<b>Výhody</b>", s_table_b),
        Paragraph("<b>Nevýhody</b>", s_table_b),
    ]]
    max_rows = max(len(advantages), len(disadvantages))
    for i in range(max_rows):
        adv_text = f"{i+1}. {A(advantages[i])}" if i < len(advantages) else ""
        dis_text = f"{i+1}. {A(disadvantages[i])}" if i < len(disadvantages) else ""
        adv_data.append([
            Paragraph(adv_text, s_table_ans),
            Paragraph(dis_text, s_table_ans),
        ])
    at = Table(adv_data, colWidths=[UW * 0.5] * 2)
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
    #  Q5 – Short answers
    # ================================================================
    story.append(Paragraph("5) Krátke odpovede:", s_q))
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
