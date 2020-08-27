from src.parser.text_extractor.docx import extract_text_from_doc
from src.parser.text_extractor.pdf import extract_text_from_pdf



def extract_text_from_document(document_path):

    text = ""
    if document_path.endswith(".pdf"):
        for page in extract_text_from_pdf(document_path):
            text += ' ' + page
    elif document_path.endswith(".docx"):
        text = extract_text_from_doc(document_path)

    return text


