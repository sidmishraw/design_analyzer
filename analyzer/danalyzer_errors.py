# danalyzer_errors.py
# -*- coding: utf-8 -*-
# @Author: Sidharth Mishra
# @Date:   2017-03-30 20:34:08
# @Last Modified by:   Sidharth Mishra
# @Last Modified time: 2017-03-30 20:36:54




# Python Standard Library imports
from pprint import pprint



class BadStarUMLProjectError(Exception):
  '''
  Raised when the StarUML project has a malformed JSON.
  '''

  pass
