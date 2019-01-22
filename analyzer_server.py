#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from doc_processor.downloader import Downloader
from doc_processor.analyzer import Analyzer
from doc_processor.processor import Processor
import time
import json

hostName = ""
hostPort = 80

class MyServer(BaseHTTPRequestHandler):

    downloader = Downloader('./docs')
    analyzer = Analyzer()

    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))

    def do_POST(self):

        print( "incomming http: ", self.path )
        if self.path == '/analyze':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length) # <--- Gets the data itself
            post_data = post_data.decode("utf-8")
            processor = Processor(self.downloader, self.analyzer)
            result=processor.process(post_data)
            json_string = json.dumps(result)
            self.wfile.write(json_string.encode())
            self.send_response(200)

        
        self.send_response(200)


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))