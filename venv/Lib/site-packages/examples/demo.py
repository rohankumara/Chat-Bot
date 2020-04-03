#encoding=utf-8

import sys

import os
from chatter_learning import Chatter

chatter = Chatter(database_url='mongodb://127.0.0.1:27017')
while True:
    testVar = raw_input().decode(sys.stdin.encoding)
    print chatter.response_to(testVar)