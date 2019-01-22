import urllib
import urllib.request
import uuid
import html

class Downloader(object):

    def __init__(self, destination_folder):
        self.destination_folder = destination_folder

    def get_url_extension(self, url):
        index = url.rfind('.')
        index = index + 1
        extension = url[index:]
        queryparams_index = extension.find('?') 
        if queryparams_index > 0:
            extension = extension[0:queryparams_index]

        if extension.find('/') > 0:
            return 'jpg'

        return extension

    def get_url_name(self, url):
        index = url.rfind('/')
        index = index + 1
        name = url[index:]
        queryparams_index = name.find('?') 
        if queryparams_index > 0:
            name = name[0:queryparams_index]

        return name

    def generate_uuid(self):
        return str(uuid.uuid4())

    def download(self, url):
        url = html.unescape(url)
        if not url:
            return None
        try:
            return urllib.request.urlretrieve(url, self.destination_folder + '/' + self.generate_uuid() + '.' + self.get_url_extension(url))
        except Exception as e:
            print(e)
            return None

    def download_with_name(self, url):
        url = html.unescape(url)
        if not url:
            return None
        try:
            file_tuple = urllib.request.urlretrieve(url, self.destination_folder + '/' + self.get_url_name(url))
            return file_tuple
        except Exception as e:
            print(e)
            return None

