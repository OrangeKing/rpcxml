#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if sys.version_info[0] < 3:
    from SimpleXMLRPCServer import SimpleXMLRPCServer
else:
    from xmlrpc.server import SimpleXMLRPCServer


address = ('localhost', 9000)
server = SimpleXMLRPCServer(address)


def multiply(a, b):
    """Return the product of two numbers"""
    print(a * b)
    return a * b

def hello():
    """Hello message"""
    print("Hello world")
    return True


server.register_function(multiply)
server.register_function(hello)


if __name__ == '__main__':
    try:
        print("Server running on %s:%s" % address)
        print("Use Ctrl-C to Exit")
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Exiting")
