"""
Generátor pracovného listu S ODPOVEĎAMI: ABS, ASR a FDR (ESP)

Použitie:  python generate_worksheet_abs_asr_fdr_answers.py
Výstup:    pracovny-list-abs-asr-fdr-odpovede.pdf

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
OUTPUT = os.path.join(BASE_DIR, "pracovny-list-abs-asr-fdr-odpovede.pdf")

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
        f"Pracovný list CEV: ABS, ASR a FDR (ESP) – {A('ODPOVEDE')}",
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
    #  Q1 – Explain abbreviations and functions
    # ================================================================
    story.append(Paragraph(
        "1) Napíš celý názov skratky a jednou vetou vysvetli funkciu systému:",
        s_q,
    ))
    q1 = [
        ("ABS", "Anti-lock Braking System",
         "zabraňuje zablokovaniu kolies počas brzdenia"),
        ("ASR", "Anti-Slip Regulation",
         "zabraňuje preklzu hnacích kolies pri rozjazde a akcelerácii"),
        ("FDR/ESP", "Fahrdynamikregelung / Electronic Stability Program",
         "pomáha vodičovi udržať vozidlo pod kontrolou v zákrutách "
         "a pri prudkých zmenách smeru"),
    ]
    for abbr, full, func in q1:
        story.append(Paragraph(
            f"<b>{abbr}</b> = {A(full)}  –  {A(func)}",
            s_ans,
        ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q2 – Label the ABS diagram
    # ================================================================
    story.append(Paragraph("2) Popíš schému systému ABS:", s_q))
    story.append(scaled_img(ABS_IMG, UW * 0.62, max_h=8 * cm))
    story.append(Spacer(1, 3))

    q2_answers = [
        "Snímače otáčok",
        "Elektronická riadiaca jednotka (ECU)",
        "Hydraulická riadiaca jednotka (HCU)",
    ]
    rows = []
    for i, ans in enumerate(q2_answers, 1):
        rows.append([Paragraph(f"<b>{i}</b> – {A(ans)}", s_ans)])
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
        f"pomocou {A('snímačov')}. Tieto údaje porovnáva "
        f"{A('elektronická riadiaca jednotka (ECU)')} s rýchlosťou vozidla. "
        f"Keď ECU zistí, že niektoré koleso spomaľuje rýchlejšie, než spomaľuje "
        f"vozidlo, okamžite {A('zníži')} brzdný tlak na tomto kolese pomocou "
        f"{A('hydraulických ventilov')}. Tým umožní kolesu opätovne sa "
        f"{A('roztočiť')} a obnoviť priľnavosť "
        f"k vozovke. Tento proces sa opakuje {A('niekoľkokrát')} za sekundu.",
        s_body,
    ))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q4 – True / False (ABS)
    # ================================================================
    story.append(Paragraph("4) Rozhodni – Pravda / Nepravda:", s_q))
    q4 = [
        ("ABS zabraňuje zablokovaniu kolies počas brzdenia.", "Pravda"),
        ("Na štrku a hlbokom snehu ABS skracuje brzdnú dráhu.", "Nepravda"),
        ("ABS je v EÚ povinnou výbavou nových osobných automobilov od roku 2004.",
         "Pravda"),
        ("Vodič pri aktivácii ABS vníma pulzovanie brzdového pedála.", "Pravda"),
        ("ABS reguluje brzdný tlak na všetkých kolesách rovnako.", "Nepravda"),
    ]
    for stmt, ans in q4:
        story.append(pn_row(stmt, ans))

    # ================================================================
    #  PAGE 2
    # ================================================================
    story.append(PageBreak())

    # ================================================================
    #  Q5 – ASR regulation methods
    # ================================================================
    story.append(Paragraph("5) ASR – metódy regulácie:", s_q))
    story.append(Paragraph(
        "ASR zabraňuje preklzu hnacích kolies dvoma hlavnými spôsobmi:",
        s_body,
    ))
    story.append(Paragraph(f"a) {A('Zníženie výkonu motora')}", s_ans))
    story.append(Paragraph(f"b) {A('Pribrzdenie preklzujúceho kolesa')}", s_ans))
    story.append(Spacer(1, 2))
    story.append(Paragraph(
        "Uveď 3 spôsoby, akými ASR znižuje výkon <b>benzínového</b> motora:",
        s_body,
    ))
    q5_methods = [
        "Znížením dávky paliva alebo dočasným vypnutím vstrekovania",
        "Oneskorením iskry alebo jej vynechávaním v niektorých valcoch",
        "Dočasným znížením prívodu vzduchu (prikrytím škrtiacej klapky)",
    ]
    for i, m in enumerate(q5_methods, 1):
        story.append(Paragraph(f"{i}. {A(m)}", s_ans))
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
         Paragraph(A("Pribrzdi predné vonkajšie koleso"), s_table_ans)],
        [Paragraph("Nedotáčavosť (understeer)", s_table),
         Paragraph(A("Pribrzdi zadné vnútorné koleso"), s_table_ans)],
        [Paragraph("Preklz pri rozjazde", s_table),
         Paragraph(A("Aktivuje sa funkcia ASR"), s_table_ans)],
        [Paragraph("Blokovanie pri brzdení", s_table),
         Paragraph(A("Aktivuje sa funkcia ABS"), s_table_ans)],
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
    q7 = [
        ("ASR využíva rovnaké snímače otáčok kolies ako ABS.", "Pravda"),
        ("ASR zabraňuje preklzu kolies iba znížením výkonu motora.", "Nepravda"),
        ("FDR porovnáva zámer vodiča (uhol natočenia volantu) so skutočným "
         "správaním vozidla.", "Pravda"),
        ("ESP je v EÚ povinné pre všetky nové registrácie osobných "
         "automobilov od roku 2004.", "Nepravda"),
        ("ESP dokáže zabrániť až 80% nehodám spôsobeným šmykom.", "Pravda"),
    ]
    for stmt, ans in q7:
        story.append(pn_row(stmt, ans))
    story.append(Spacer(1, 3))

    # ================================================================
    #  Q8 – Short answers
    # ================================================================
    story.append(Paragraph("8) Krátke odpovede:", s_q))
    story.append(Paragraph(
        "a) Aký je vzťah medzi systémami ABS, ASR a FDR/ESP?", s_body,
    ))
    story.append(Paragraph(
        A("FDR/ESP je nadstavba nad ABS a ASR – obsahuje všetky ich komponenty "
          "a pridáva ďalšie snímače (uhol volantu, priečne zrýchlenie, gyroskop). "
          "ABS zabraňuje blokovaniu kolies pri brzdení, ASR zabraňuje preklzu "
          "pri akcelerácii a FDR riadi stabilitu celého vozidla."),
        s_answer_line,
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "b) Čo je MSR a kedy sa aktivuje?", s_body,
    ))
    story.append(Paragraph(
        A("MSR (Motor Schleppmoment Regelung) je regulácia brzdného momentu "
          "motora – doplnková funkcia ASR. Aktivuje sa pri prudkom znížení "
          "otáčok motora (napr. pri radení na nižší prevod na klzkom povrchu), "
          "keď hrozí zablokovanie hnacích kolies brzdným účinkom motora."),
        s_answer_line,
    ))

    # ================================================================
    #  BUILD
    # ================================================================
    doc.build(story)
    print(f"PDF vytvorený: {OUTPUT}")


if __name__ == "__main__":
    build()
