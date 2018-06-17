#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if sys.version_info[0] < 3:
    import xmlrpclib
else:
    import xmlrpc.client as xmlrpclib

proxy = xmlrpclib.ServerProxy('http://localhost:9000', verbose=True)
proxy.multiply(3, 24)
proxy.hello()