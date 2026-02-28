"""
Generátor pracovného listu: ABS, ASR a FDR (ESP)

Použitie:  python generate_worksheet_abs_asr_fdr.py
Výstup:    pracovny-list-abs-asr-fdr.pdf

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
ABS_IMG = os.path.join(CONTENT_DIR, "ABS", "ABS.png")
OUTPUT = os.path.join(BASE_DIR, "pracovny-list-abs-asr-fdr.pdf")

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

BL = "_______________"
BL_LONG = "_" * 55


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
        "Pracovný list CEV: ABS, ASR a FDR (ESP)", s_title,
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
    #  Q1 – Explain abbreviations and functions
    # ================================================================
    story.append(Paragraph(
        "1) Napíš celý názov skratky a jednou vetou vysvetli funkciu systému:",
        s_q,
    ))
    for abbr in ["ABS", "ASR", "FDR/ESP"]:
        story.append(Paragraph(
            f"<b>{abbr}</b> = {BL}  –  {BL_LONG}", s_ans,
        ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Label the ABS diagram
    # ================================================================
    story.append(Paragraph(
        "2) Popíš schému systému ABS:", s_q,
    ))
    story.append(scaled_img(ABS_IMG, UW * 0.62, max_h=8 * cm))
    story.append(Spacer(1, 3))

    rows = []
    for i in range(1, 4):
        rows.append([Paragraph(f"<b>{i}</b> – {'_' * 55}", s_ans)])
    t = Table(rows, colWidths=[UW])
    t.setStyle(TableStyle([
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(t)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q3 – Fill in the blanks (ABS principle)
    # ================================================================
    story.append(Paragraph("3) Doplň do textu:", s_q))
    story.append(Paragraph(
        f"Systém ABS neustále monitoruje rýchlosť otáčania každého kolesa "
        f"pomocou {BL}. Tieto údaje porovnáva {BL} s rýchlosťou vozidla. "
        f"Keď ECU zistí, že niektoré koleso spomaľuje rýchlejšie, než spomaľuje "
        f"vozidlo, okamžite {BL} brzdný tlak na tomto kolese pomocou "
        f"{BL}. Tým umožní kolesu opätovne sa {BL} a obnoviť priľnavosť "
        f"k vozovke. Tento proces sa opakuje {BL} za sekundu.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q4 – True / False (ABS)
    # ================================================================
    story.append(Paragraph("4) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt in [
        "ABS zabraňuje zablokovaniu kolies počas brzdenia.",
        "Na štrku a hlbokom snehu ABS skracuje brzdnú dráhu.",
        "ABS je v EÚ povinnou výbavou nových osobných automobilov od roku 2004.",
        "Vodič pri aktivácii ABS vníma pulzovanie brzdového pedála.",
        "ABS reguluje brzdný tlak na všetkých kolesách rovnako.",
    ]:
        story.append(pn_row(stmt))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q5 – ASR regulation methods
    # ================================================================
    story.append(Paragraph(
        "5) ASR – metódy regulácie:", s_q,
    ))
    story.append(Paragraph(
        "ASR zabraňuje preklzu hnacích kolies dvoma hlavnými spôsobmi:", s_body,
    ))
    story.append(Paragraph(f"a) {'_' * 80}", s_ans))
    story.append(Paragraph(f"b) {'_' * 80}", s_ans))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "Uveď 3 spôsoby, akými ASR znižuje výkon <b>benzínového</b> motora:",
        s_body,
    ))
    for i in range(1, 4):
        story.append(Paragraph(f"{i}. {'_' * 78}", s_ans))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q6 – FDR interventions table
    # ================================================================
    story.append(Paragraph(
        "6) Doplň, ako zasahuje systém FDR v nasledujúcich situáciách:", s_q,
    ))
    fdr_data = [
        [Paragraph("<b>Situácia</b>", s_table_b),
         Paragraph("<b>Zásah systému FDR</b>", s_table_b)],
        [Paragraph("Pretáčavosť (oversteer)", s_table),
         Paragraph("", s_table)],
        [Paragraph("Nedotáčavosť (understeer)", s_table),
         Paragraph("", s_table)],
        [Paragraph("Preklz pri rozjazde", s_table),
         Paragraph("", s_table)],
        [Paragraph("Blokovanie pri brzdení", s_table),
         Paragraph("", s_table)],
    ]
    ft = Table(fdr_data, colWidths=[UW * 0.35, UW * 0.65])
    ft.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, black),
        ("BACKGROUND", (0, 0), (-1, 0), GRAY_BG),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(ft)
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q7 – True / False (ASR + FDR)
    # ================================================================
    story.append(Paragraph("7) Rozhodni – Pravda / Nepravda:", s_q))
    for stmt in [
        "ASR využíva rovnaké snímače otáčok kolies ako ABS.",
        "ASR zabraňuje preklzu kolies iba znížením výkonu motora.",
        "FDR porovnáva zámer vodiča (uhol natočenia volantu) so skutočným "
        "správaním vozidla.",
        "ESP je v EÚ povinné pre všetky nové registrácie osobných "
        "automobilov od roku 2004.",
        "ESP dokáže zabrániť až 80% nehodám spôsobeným šmykom.",
    ]:
        story.append(pn_row(stmt))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q8 – Short answers
    # ================================================================
    story.append(Paragraph("8) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Aký je vzťah medzi systémami ABS, ASR a FDR/ESP?", s_body,
    ))
    for _ in range(3):
        story += answer_line()
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Čo je MSR a kedy sa aktivuje?", s_body,
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
