#!/usr/bin/python

import sys
import SocketServer
from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888

httpd = SocketServer.TCPServer(('0.0.0.0', port), Handler)
sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()