#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true


#https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    suma = 0
    sumb = 0

    suma = 0
    sumb = 0

    for i in range(len(arr)):
        suma += arr[i][i]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i + j == len(arr)-1:
                sumb += arr[i][j]

    return abs(suma-sumb)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
