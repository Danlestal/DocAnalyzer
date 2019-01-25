
import hashlib

def create_hash(file):
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()


class Processor(object):
    def __init__(self, doc_analyzer):
        self.doc_analyzer = doc_analyzer

    def process_local_file(self, file_path):
        key_terms = self.doc_analyzer.analyze(file_path)
        md5 = create_hash(file_path)
        
        return {
            'md5': md5,
            'file': file_path,
            'keys': key_terms
        }

    def process_url(self, downloader, url):
        real_file = downloader.download(url)[0]
        local_data_result = self.process_local_file(real_file)
        local_data_result['source_url'] = url
        return local_data_result

