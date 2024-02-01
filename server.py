from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os.path

hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # content = f.read()
        # content = content[:-1]
        with(open("devices.txt", "r")) as f:
            content = f.read()
            content = content[:-2]
            self.wfile.write(bytes("[" + content + "]", "utf-8"))

myServer = HTTPServer((hostName, serverPort), MyServer)
print(time.asctime(), "Server - http://%s:%s" % (hostName, serverPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass



