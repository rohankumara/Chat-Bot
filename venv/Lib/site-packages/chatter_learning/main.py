#encoding=utf-8
import sys

from chatter_learning import Chatter
# chatter = Chatter()

while True:
    testVar = raw_input().decode(sys.stdin.encoding)
    print testVar, type(testVar)
    # print chatter.response_to(testVar)