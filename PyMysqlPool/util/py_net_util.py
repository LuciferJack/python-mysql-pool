#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding=utf-8
import socket


def get_ip_address():
    print  socket.gethostbyname(socket.gethostname())
    return socket.gethostbyname(socket.gethostname())
