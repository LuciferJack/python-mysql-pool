#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8

import ssl
import requests

print('OpenSSL: {0}'.format(ssl.OPENSSL_VERSION))
print('requests: {0}'.format(requests.__version__))