from doc_processor.analyzer import Analyzer
from doc_processor.processor import Processor
from communications.sender import DocumentSender


analyzer = Analyzer()
processor = Processor(analyzer)
document_data = processor.process_local_file('docs/30e70721-f034-4700-a2c1-a6d0e862d40e.pdf')

sender = DocumentSender()
sender.send(document_data)

