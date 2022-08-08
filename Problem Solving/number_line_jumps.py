#https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true


### 8 out of 30 tests will be failed .. i will work on this later ...
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    boolMe = False
    
    a = True
    b = True

    while(a and b):
        x1 += v1
        x2 += v2

        a = x1 > -1 and x1 < 10001 and x2 > -1 and x2 < 10001
        b = v1 > 0 and v1 < 10001 and v2 > 0 and v2 < 100001

        if x1 == x2:
            boolMe = True


    if boolMe:
        return "YES"
    elif boolMe == False:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
