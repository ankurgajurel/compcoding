#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    x = ""

    if s[-2:] == "PM":
        if int(s[:2]) != 12:
            x = str(12 + int(s[:2])) + s[2:-2]
        else:
            x = s[:-2]
    elif s[-2:] == "AM":
        if int(s[:2]) == 12:
            x = str("00" + s[2:-2])
        else:
            x = s[:-2]

    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
