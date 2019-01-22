class Processor(object):

    def __init__(self, downloader, doc_analyzer):
        self.downloader = downloader
        self.doc_analyzer = doc_analyzer

    def process(self, url):

        name = self.downloader.get_url_name(url)
        real_file = self.downloader.download(url)[0]
        key_terms = self.doc_analyzer.analyze(real_file)
        
        result = {
            'source_url': url,
            'name': name,
            'file': real_file,
            'keys': key_terms
        }

        return result
        
        