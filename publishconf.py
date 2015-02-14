#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://m157q.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "m157q-logdown"
GOOGLE_ANALYTICS = "UA-45367183-2"
GOOGLE_ANALYTICS_DOMAIN = "auto"
GOOGLE_SEARCH = "005681925362179744994:3xdgt3w3iu0"
