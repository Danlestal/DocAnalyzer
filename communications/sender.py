import requests

class DocumentSender(object):

    DOCUMENTS_ENDPOINT = "http://localhost:8080/documents"

    def send(self, data ):
        document_data = {'documentUrl': data['file'], 'sourceUrl': data['file']}
        resp = requests.post(self.DOCUMENTS_ENDPOINT, headers={"content-type":"application/json"}, json=document_data)
        respuesta = resp.json()

        for key in data['keys']:
            internalkeys_url = "%s/%s/internalkeys" % (self.DOCUMENTS_ENDPOINT,respuesta['id'])
            respuesta_key = requests.post(internalkeys_url,
                                headers={"content-type":"application/json"}, 
                                json=key[0])
