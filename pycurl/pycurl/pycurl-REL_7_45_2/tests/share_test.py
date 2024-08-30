#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

from . import localhost
import threading
import pycurl
import pytest
import unittest

from . import appmanager
from . import util

setup_module, teardown_module = appmanager.setup(('app', 8380))

class WorkerThread(threading.Thread):

    def __init__(self, share):
        threading.Thread.__init__(self)
        self.curl = util.DefaultCurl()
        self.curl.setopt(pycurl.URL, 'http://%s:8380/success' % localhost)
        self.curl.setopt(pycurl.SHARE, share)
        self.sio = util.BytesIO()
        self.curl.setopt(pycurl.WRITEFUNCTION, self.sio.write)

    def run(self):
        self.curl.perform()
        self.curl.close()

class ShareTest(unittest.TestCase):
    def test_share(self):
        s = pycurl.CurlShare()
        s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_COOKIE)
        s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_DNS)
        s.setopt(pycurl.SH_SHARE, pycurl.LOCK_DATA_SSL_SESSION)

        t1 = WorkerThread(s)
        t2 = WorkerThread(s)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        del s

        self.assertEqual('success', t1.sio.getvalue().decode())
        self.assertEqual('success', t2.sio.getvalue().decode())

    def test_share_close(self):
        s = pycurl.CurlShare()
        s.close()

    def test_share_close_twice(self):
        s = pycurl.CurlShare()
        s.close()
        s.close()

    # positional arguments are rejected
    def test_positional_arguments(self):
        with pytest.raises(TypeError):
            pycurl.CurlShare(1)

    # keyword arguments are rejected
    def test_keyword_arguments(self):
        with pytest.raises(TypeError):
            pycurl.CurlShare(a=1)
