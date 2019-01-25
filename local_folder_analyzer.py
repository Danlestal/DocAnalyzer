from doc_processor.analyzer import Analyzer
from doc_processor.processor import Processor
from communications.sender import DocumentSender
import os


analyzer = Analyzer()
processor = Processor(analyzer)
sender = DocumentSender()

files = os.listdir('docs/')
for name in files:
    try:
        document_data = processor.process_local_file('docs/' + name)
    except:
        continue
    sender.send(document_data)






