
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch

document = []

def addTitle(doc):
    doc.append(Spacer(1, 20))
    doc.append(Paragraph('Ein_Satz_Spiel', ParagraphStyle(name='Yeat',
                                                          fontFamily='Helvetica',
                                                          fontSize=36,
                                                          alignment=TA_CENTER)))
    doc.append(Spacer(1, 50))
    return doc

def addParagraphs(doc):
    doc.append(Spacer(1, 20))
    doc.append(Paragraph('hier_strings_von_nils_einfügen', ParagraphStyle(name='Yoot',
                                                          fontFamily='Helvetica',
                                                          fontSize=20,
                                                          alignment=TA_JUSTIFY)))
    doc.append(Spacer(1, 20))
    return doc

    document = addTitle(document)

SimpleDocTemplate('One_Sentence_Game.pdf', pagesize=letter,
                  rightMargin=12, leftMargin=12,
                  topMargin=12, bottomMargin=6).build(addParagraphs(document))