#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

if 'SITEURL' not in os.environ:
    raise Exception('SITEURL variable must be set')

ABSOLUTE_SITEURL = os.environ['SITEURL']
I18N_SUBSITES['fi']['ABSOLUTE_SITEURL'] = ABSOLUTE_SITEURL + '/fi'

if 'GOOGLE_ANALYTICS' in os.environ:
    GOOGLE_ANALYTICS = os.environ['GOOGLE_ANALYTICS']


DELETE_OUTPUT_DIRECTORY = True

#GOOGLE_ANALYTICS = ""
