"""
Generátor pracovného listu S ODPOVEĎAMI:
Hydraulický brzdový systém a Brzdové posilňovače

Použitie:  python generate_worksheet_hbs_bp_answers.py
Výstup:    pracovny-list-hbs-bp-odpovede.pdf

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
OUTPUT = os.path.join(BASE_DIR, "pracovny-list-hbs-bp-odpovede.pdf")

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
BLUE = HexColor("#0044AA")

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
s_match = ParagraphStyle("Match", fontName="F", fontSize=9.5, leading=13)
s_pn = ParagraphStyle("PN", fontName="F", fontSize=10, leading=17)
s_pnr = ParagraphStyle(
    "PNR", fontName="FB", fontSize=9, leading=17, alignment=TA_CENTER,
)
s_answer_line = ParagraphStyle(
    "AnswerLine", fontName="FI", fontSize=10, leading=16, textColor=BLUE,
)


def A(text):
    """Wrap text as an italic blue answer inline."""
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
    """True/False row with the correct answer highlighted in italic blue."""
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


def answer_grid(items, cols=2):
    """Create a 2-column grid of numbered answers filled in."""
    rows = []
    for i in range(0, len(items), cols):
        row = []
        for j in range(cols):
            idx = i + j
            if idx < len(items):
                label, ans = items[idx]
                row.append(Paragraph(
                    f"<b>{label}</b> – {A(ans)}", s_ans,
                ))
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
        "Pracovný list CEV: Hydraulický brzdový systém a Brzdové posilňovače "
        f'– {A("ODPOVEDE")}',
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

    q1_answers = [
        ("1", "Brzdový pedál"),
        ("2", "Podtlakový posilňovač"),
        ("3", "Hlavný (dvojokruhový) brzdový valec"),
        ("4", "Nádržka na brzdovú kvapalinu"),
        ("5", "Okruh predných bŕzd"),
        ("6", "Okruh zadných bŕzd"),
        ("7", "Obmedzovač brzdového účinku"),
        ("8", "Predné brzdy (kotúčové)"),
        ("9", "Zadné brzdy (bubnové)"),
    ]
    story.append(answer_grid(q1_answers))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Fill in the blanks (principle of operation)
    # ================================================================
    story.append(Paragraph("2) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Keď vodič stlačí brzdový {A('pedál')}, piest v hlavnom brzdovom "
        f"{A('valci')} vytvorí tlak v brzdovej {A('kvapaline')}. Tento tlak "
        f"sa prenáša {A('potrubím')} do brzdových {A('valčekov')} pri kolesách, "
        f"kde posúva piesty. Piesty pritláčajú brzdové {A('doštičky')} na kotúče "
        f"alebo brzdové {A('čeľuste')} na bubny, čím vzniká trenie "
        f"a {A('brzdná')} sila.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q3 – Brake circuit arrangements
    # ================================================================
    story.append(Paragraph("3) Brzdové okruhy:", s_q))
    story.append(Paragraph(
        f"a) Koľko nezávislých brzdových okruhov musí mať prevádzková brzda? "
        f"{A('2 (dva)')}",
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
                Paragraph(f"1. {A('TT')}", s_ans),
                Paragraph(f"2. {A('Diagonálne')}", s_ans),
                Paragraph(f"3. {A('HT')}", s_ans),
            ],
            [
                Paragraph(f"4. {A('LL')}", s_ans),
                Paragraph(f"5. {A('HH')}", s_ans),
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
    q4 = [
        ("Prevádzková brzda musí mať vždy dva samostatné brzdové okruhy.",
         "Pravda"),
        ("Obmedzovač brzdového účinku reguluje tlak v okruhu predných bŕzd.",
         "Nepravda"),
        ("Nádržka na brzdovú kvapalinu by mala byť na ľahko dostupnom "
         "a viditeľnom mieste v motorovom priestore.",
         "Pravda"),
        ("Hydraulický brzdový systém prenáša brzdnú silu pomocou stlačeného vzduchu.",
         "Nepravda"),
    ]
    for stmt, ans in q4:
        story.append(pn_row(stmt, ans))

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

    # Correct: 1→D, 2→E, 3→B, 4→F, 5→A, 6→C
    parts_col = [
        ("1.", "Podtlaková komora", "D"),
        ("2.", "Membrána", "E"),
        ("3.", "Tanierový ventil", "B"),
        ("4.", "Prepúšťací kanál", "F"),
        ("5.", "Tlačná tyč", "A"),
        ("6.", "Reakčný kotúč", "C"),
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
        num, name, correct_letter = parts_col[i]
        d_letter, d_text = descs_col[i]
        match_data.append([
            Paragraph(num, s_match),
            Paragraph(name, s_match),
            Paragraph(f'<i><font color="#0044AA"><b>{correct_letter}</b></font></i>', s_match),
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
        f"Keď vodič nestláča brzdový pedál, v podtlakovej aj v {A('pracovnej')} "
        f"komore je rovnaký tlak ({A('podtlak')}). Pri stlačení pedála sa do "
        f"pracovnej komory vpustí {A('atmosférický')} tlak a zablokuje sa "
        f"{A('prepúšťací')} kanál. Rozdiel tlakov vytvára silu, ktorá tlačí na "
        f"{A('piest')} a prenáša sa do hlavného brzdového valca pomocou "
        f"{A('tlačnej')} tyče.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q7 – True / False
    # ================================================================
    story.append(Paragraph("7) Rozhodni – Pravda / Nepravda:", s_q))
    q7 = [
        ("Brzdový posilňovač zosilňuje silu vyvinutú vodičom na brzdový pedál.",
         "Pravda"),
        ("Podtlakový posilňovač využíva podtlak z výfukového potrubia motora.",
         "Nepravda"),
        ("Membrána oddeľuje podtlakovú komoru od pracovnej komory.",
         "Pravda"),
        ("Zosílenie brzdového posilňovača býva zvyčajne od 300% do 500%.",
         "Pravda"),
        ("Tanierový ventil pri stlačení brzdového pedálu otvára prepúšťací kanál.",
         "Nepravda"),
    ]
    for stmt, ans in q7:
        story.append(pn_row(stmt, ans))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q8 – Short answers
    # ================================================================
    story.append(Paragraph("8) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Aká je hlavná funkcia brzdového posilňovača?", s_body,
    ))
    story.append(Paragraph(
        A("Brzdový posilňovač je zariadenie zosilňujúce silu, ktorú vodič vyvinie "
          "stlačením brzdového pedálu pri brzdení. Tým pádom taktiež znižuje silu, "
          "ktorú musí vodič pri brzdení na pedál vyvinúť. Zosílenie býva zvyčajne "
          "od 300% do 500%."),
        s_answer_line,
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Čo vyhodnocuje systém BAS a ako reaguje pri núdzovom brzdení?",
        s_body,
    ))
    story.append(Paragraph(
        A("Systém BAS vyhodnocuje rýchlosť stláčania brzdového pedála. Pri zistení "
          "náhlého, rýchleho stlačenia (typické pre núdzovú situáciu) systém "
          "automaticky zvyšuje brzdný tlak na maximum."),
        s_answer_line,
    ))

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
