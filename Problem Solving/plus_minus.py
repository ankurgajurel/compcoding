#https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos += 1
        elif i == 0:
            zero += 1
        else:
            neg += 1

    rat1 = float(format(pos / len(arr), ".7f"))
    rat2 = float(format(neg / len(arr), ".7f"))
    rat3 = float(format(zero / len(arr), ".7f"))
    
    print(rat1)
    print(rat2)
    print(rat3)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
