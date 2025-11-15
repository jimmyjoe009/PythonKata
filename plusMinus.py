# Given an array of integers, calculate the ratios of its elements that are , , and . Print the decimal value of each fraction on a new line with 6 places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

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
    positive=0
    negative=0
    zero=0
    
    for i in arr:
        if i>0: positive=positive+(1/len(arr))
        elif i<0: negative+=(1/len(arr))
        else: zero+=1/len(arr)
    
    print("%.6f" % positive)
    print("%.6f" % negative)
    print("%.6f" % zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
