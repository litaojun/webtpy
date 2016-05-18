#!/usr/bin/python
# -*- coding: utf-8 -*-

import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'test')) 
import sae
import web
from myweb import testweb

application = testweb()