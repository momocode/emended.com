#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

if 'SITEURL' not in os.environ:
    raise Exception('SITEURL variable must be set')

from pelicanconf import *

if 'GOOGLE_ANALYTICS' in os.environ:
    GOOGLE_ANALYTICS = os.environ['GOOGLE_ANALYTICS']

DELETE_OUTPUT_DIRECTORY = True
