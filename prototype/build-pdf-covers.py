#!/usr/bin/env python3
"""Prepend institutional covers to the two project PDFs."""
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor

OUT = Path(__file__).parent / "pdf"
INK = HexColor("#132019")
MUTED = HexColor("#5B6B62")
GREEN = HexColor("#4E9A3F")
CORK = HexColor("#C2603A")


def cover(path, title, subtitle, accent):
    c = canvas.Canvas(str(path), pagesize=A4)
    w, h = A4
    c.setFillColor(HexColor("#F4FBFA"))
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(accent)
    c.rect(0, 0, 18, h, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont("Times-Roman", 11)
    c.drawString(48, h - 64, "Centro Studi R.I.S.S.T.E. APS  ·  Soggetto attuatore")
    c.setFont("Times-Bold", 22)
    y = h - 130
    for line in title:
        c.drawString(48, y, line)
        y -= 28
    c.setFillColor(MUTED)
    c.setFont("Times-Italic", 13)
    y -= 10
    for line in subtitle:
        c.drawString(48, y, line)
        y -= 18
    c.setFillColor(INK)
    c.setFont("Times-Roman", 12)
    c.drawString(48, 160, "Progetto di ricerca e sviluppo, valorizzazione del sughero sardo")
    c.drawString(48, 142, "e innovazione tecnologica")
    c.setFont("Times-Bold", 12)
    c.drawString(48, 116, "CUP E77G24000450002")
    c.setFont("Times-Roman", 10)
    c.setFillColor(MUTED)
    c.drawString(48, 88, "Progetto finanziato dalla Regione Autonoma della Sardegna")
    c.drawString(48, 74, "Assessorato dell'Agricoltura e riforma agro-pastorale")
    c.drawString(48, 50, "I dati pubblicati sul sito derivano dal database validato del progetto.")
    c.showPage()

    c.setFillColor(HexColor("#F4FBFA"))
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont("Times-Bold", 16)
    c.drawString(48, h - 72, "Premessa")
    c.setFont("Times-Roman", 11)
    text = c.beginText(48, h - 108)
    text.setLeading(16)
    for para in [
        "Questo volume e' parte del Progetto di ricerca e sviluppo, valorizzazione del sughero sardo e innovazione tecnologica (CUP E77G24000450002), realizzato dal Centro Studi R.I.S.S.T.E. APS in qualita' di soggetto attuatore.",
        "",
        "Il progetto riguarda la valorizzazione del comparto sughericolo sardo, la mappatura della risorsa, la ricerca di mercato, la raccolta e l'elaborazione dei dati, la gestione sostenibile dei sistemi agroforestali, le certificazioni, l'innovazione tecnologica e la costruzione di un database geografico aperto.",
        "",
        "La Gallura e' trattata come principale territorio della filiera, area di concentrazione di imprese e competenze, e caso di studio utile alla lettura del comparto regionale. Non costituisce l'ambito esclusivo del progetto.",
        "",
        "I titoli e la cornice istituzionale di questa edizione sono allineati al progetto regionale. Il contenuto scientifico resta quello validato dagli autori.",
    ]:
        text.textLine(para)
    c.drawText(text)
    c.showPage()
    c.save()


def prepend(src, cover_pdf):
    writer = PdfWriter()
    for page in PdfReader(cover_pdf).pages:
        writer.add_page(page)
    for page in PdfReader(src).pages:
        writer.add_page(page)
    tmp = src.with_suffix(".tmp.pdf")
    writer.write(tmp)
    tmp.replace(src)


def main():
    OUT.mkdir(exist_ok=True)
    c1 = OUT / "_cover1.pdf"
    c2 = OUT / "_cover2.pdf"
    cover(c1, [
        "Studio 1",
        "Quadro territoriale, socioeconomico",
        "e produttivo della filiera",
        "sughericola in Gallura",
    ], ["Approfondimento territoriale del progetto regionale", "Focus Gallura  ·  polo Calangianus-Tempio"], GREEN)
    cover(c2, [
        "Studio 2",
        "Patrimonio sughericolo,",
        "innovazione tecnologica",
        "e gestione sostenibile in Sardegna",
    ], ["Atlante dei trenta comuni, technology scouting", "e strumenti di certificazione"], CORK)
    p1 = OUT / "RISSTE_CUP_E77G24000450002_Parte1_signed.pdf"
    p2 = OUT / "RISSTE_CUP_E77G24000450002_Parte2_signed.pdf"
    prepend(p1, c1)
    prepend(p2, c2)
    c1.unlink()
    c2.unlink()
    print("Copertine anteposte ai due PDF")


if __name__ == "__main__":
    main()
