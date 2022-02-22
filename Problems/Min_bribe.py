#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0

    for i, o in enumerate(q):
        cur = i + 1

        if o - cur > 2:
            print("Too chaotic")
            return
        
        for k in q[max(o - 2, 0):i]:
            if k > o:
                bribes += 1

    print(bribes)
        
    

if __name__ == '__main__':
    q = [1,2,3,5,4,6,7,8]
    minimumBribes(q)

    r=[4,1,2,3]
    minimumBribes(r)
