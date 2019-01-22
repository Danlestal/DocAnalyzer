import textract
import textacy
from textacy import keyterms

class Analyzer(object):

    def analyze(self, file_path):
        pdf_text = textract.process(file_path, encoding='UTF-8')
        real_text = pdf_text.decode("utf-8")

        doc = textacy.Doc(real_text)
        resultado = keyterms.sgrank(doc, ngrams=(2, 3, 4), normalize='lower', n_keyterms=0.1)
        return resultado[:20]


