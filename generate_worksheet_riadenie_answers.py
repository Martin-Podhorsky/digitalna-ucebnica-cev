"""
Generátor odpoveďového hárku: Riadenie – mechanizmus riadenia a posilňovače

Použitie:  python generate_worksheet_riadenie_answers.py
Výstup:    pracovny-list-riadenie-odpovede.pdf

Požiadavky: pip install reportlab Pillow
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
IMG_DIR = os.path.join(BASE_DIR, "content", "ucivo", "2-rocnik", "03-riadenie")
IMG_A = os.path.join(IMG_DIR, "so-spojovacou-tycou.png")
IMG_B = os.path.join(IMG_DIR, "s-riadiacimi-tycami.png")
IMG_C = os.path.join(IMG_DIR, "s-dvoma-tahadlami.png")
OUTPUT = os.path.join(BASE_DIR, "Pracovny-list_riadenie_odpovede.pdf")

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
s_img_label = ParagraphStyle(
    "ImgLbl", fontName="FB", fontSize=11, leading=14, alignment=TA_CENTER,
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
        "Pracovný list CEV: Riadenie – mechanizmus riadenia "
        "a posilňovače – ODPOVEDE",
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
    #  Q1 – Requirements for steering
    # ================================================================
    story.append(Paragraph(
        "1) Vymenuj a popíš aspoň 4 požiadavky kladené na riadenie:", s_q,
    ))
    req_lines = [
        "<b>Bezpečnosť</b> – riadiaci mechanizmus musí zabezpečiť spoľahlivé ovládanie smeru jazdy za všetkých podmienok. Pri poruche nesmie dôjsť k náhlej strate kontroly nad ovládaním.",
        "<b>Presnosť a stabilita</b> – natočeniu volantu musí zodpovedať presná zmena smeru jazdy. Vozidlo musí udržať nastavený smer bez neustálych korekcií vodiča.",
        "<b>Primeraný prevodový pomer</b> – musí zabezpečiť vhodný kompromis medzi potrebnou silou na ovládanie volantu a citlivosťou riadenia.",
        "<b>Vratnosť</b> – po uvoľnení volantu sa kolesá musia samočinne vrátiť do polohy pre priamu jazdu.",
        "<b>Tlmenie rázov</b> – riadiaci mechanizmus by nemal prenášať otrasy a vibrácie z nerovností vozovky na volant v nadmernej miere.",
        "<b>Minimálna vôľa</b> – vôľa v riadiacom mechanizme musí byť čo najmenšia pre čo najmenšiu odozvu.",
        "<b>Nízka námaha</b> – vodič musí byť schopný pohodlne ovládať riadenie aj pri nízkych rýchlostiach (parkovanie) a pri plnom zaťažení vozidla.",
        "<b>Bezpečnostná konštrukcia</b> – volantová tyč musí byť skonštruovaná tak, aby vodiča pri čelnom náraze nezranila.",
    ]
    s_req = ParagraphStyle("Req", fontName="FI", fontSize=9.5, leading=13, textColor=BLUE)
    for line in req_lines:
        story.append(Paragraph(f'<i><font color="#0033AA">{line}</font></i>', s_req))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Match terms to images (terms left, images right in column)
    # ================================================================
    story.append(Paragraph(
        "2) Priraď názov konštrukcie k správnemu obrázku:",
        s_q,
    ))

    img_col_w = UW * 0.55
    term_col_w = UW * 0.45
    img_h = 2.8 * cm

    # Terms shuffled to match worksheet order; answers show correct image number
    names_answers = [
        ("S dvoma ťahadlami", IMG_A, "1", "3"),
        ("So spájacou (priečnou) tyčou", IMG_B, "2", "1"),
        ("S delenou spojovacou tyčou", IMG_C, "3", "2"),
    ]

    s_term = ParagraphStyle("Term", fontName="F", fontSize=10, leading=14)
    s_lbl = ParagraphStyle("Lbl", fontName="FB", fontSize=10, leading=14, alignment=TA_CENTER)

    rows = []
    for name, img_path, lbl, correct in names_answers:
        term_cell = Paragraph(f"{name} <b>→ {A(correct)}</b>", s_term)
        img_obj = scaled_img(img_path, img_col_w * 0.95, max_h=img_h)
        lbl_cell = Paragraph(f"<b>{lbl}</b>", s_lbl)
        img_inner = Table([[img_obj], [lbl_cell]], colWidths=[img_col_w])
        img_inner.setStyle(TableStyle([
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ]))
        rows.append([term_cell, img_inner])

    match_tbl = Table(rows, colWidths=[term_col_w, img_col_w])
    match_tbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (0, -1), 2),
        ("BOTTOMPADDING", (0, 0), (0, -1), 2),
        ("TOPPADDING", (1, 0), (1, -1), 4),
        ("BOTTOMPADDING", (1, 0), (1, -1), 4),
        ("LINEBELOW", (0, 0), (-1, -2), 0.3, HexColor("#CCCCCC")),
    ]))
    story.append(match_tbl)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q3 – Fill in the blanks (prevodovka riadenia)
    # ================================================================
    story.append(Paragraph("3) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Prevodovka riadenia premieňa {A('otáčavý pohyb volantu')} na "
        f"{A('posuvný pohyb')}. Prevodový pomer "
        f"15:1 znamená, že pri otočení volantu o {A('15°')} sa kolesá "
        f"natočia o {A('1°')}. Dnes najbežnejším typom prevodovky "
        f"riadenia v osobných autách je {A('hrebeňová prevodovka')}.",
        s_body,
    ))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q4 – Comparison table: HPS vs EPS
    # ================================================================
    story.append(Paragraph(
        "4) Doplň porovnávaciu tabuľku (hydraulický vs. elektronický "
        "posilňovač riadenia):",
        s_q,
    ))
    props_answers = [
        ("Zdroj pomocnej sily",
         "Hydraulické čerpadlo poháňané motorom",
         "Elektromotor"),
        ("Veľkosť pomocnej sily (väčšia/menšia)",
         "Väčšia",
         "Menšia"),
        ("Spätná väzba z cesty",
         "Lepšia (prirodzenejšia)",
         "Menšia (menej prirodzená)"),
        ("Údržba",
         "Vyžaduje pravidelnú údržbu",
         "Bezúdržbový"),
        ("Závislosť od chodu motora",
         "Áno",
         "Nie"),
        ("Asistenčné systémy (LKA, parkovací asistent)",
         "Neumožňuje",
         "Umožňuje"),
    ]
    cmp_data = [[
        Paragraph("<b>Vlastnosť</b>", s_table_b),
        Paragraph("<b>HPS</b>", s_table_b),
        Paragraph("<b>EPS</b>", s_table_b),
    ]]
    for p, hps, eps in props_answers:
        cmp_data.append([
            Paragraph(p, s_table),
            Paragraph(A(hps), s_table_c),
            Paragraph(A(eps), s_table_c),
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
    #  Q5 – True / False
    # ================================================================
    story.append(Paragraph("5) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt, ans in [
        ("Hrebeňové riadenie sa používa hlavne v nákladných "
         "automobiloch.", False),
        ("Posilňovač riadenia dokáže znížiť potrebnú ovládaciu silu "
         "až o 80%.", True),
        ("Pri riadení všetkých kolies (4WS) sa zadné kolesá pri "
         "nízkych rýchlostiach natáčajú rovnakým smerom ako predné.",
         False),
        ("Elektronický posilňovač riadenia využíva na "
         "posilňovanie hydraulickú kvapalinu.", False),
        ("Bezpečnostný stĺpik riadenia je navrhnutý tak, aby sa pri "
         "čelnom náraze zalomil alebo teleskopicky zasunul.", True),
    ]:
        story.append(pn_row(stmt, ans))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – Short answers
    # ================================================================
    story.append(Paragraph("6) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Vysvetli, čo je variabilný prevodový pomer riadenia.",
        s_body,
    ))
    story.append(Paragraph(
        A("Variabilný prevodový pomer znamená, že sa mení podľa "
          "polohy volantu. V stredovej polohe je väčší (malé pohyby "
          "volantom nespôsobia prudkú zmenu smeru, čo je bezpečnejšie "
          "na diaľnici). V krajnej polohe je menší (na natočenie kolies "
          "stačí menej otáčať volantom, čo uľahčuje parkovanie)."),
        s_answer_line,
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Uveď 2 funkcie moderných elektronických posilňovačov riadenia.",
        s_body,
    ))
    story.append(Paragraph(
        A("Napr.: Premenlivé posilňovanie podľa rýchlosti (pri "
          "parkovaní ľahšie, pri vyšších rýchlostiach tuhšie), "
          "aktívny návrat volantu do stredovej polohy, "
          "kompenzácia bočného vetra, asistent pre udržanie "
          "v jazdnom pruhu (LKA), parkovací asistent."),
        s_answer_line,
    ))

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
