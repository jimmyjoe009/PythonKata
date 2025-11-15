# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# Function description

# Complete the  function with the following parameter:

# : a 2-D array of integers

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
    # Write your code here
    sum_i=0
    sum_j=0
    result=0
    rows=len(arr)
    for i in range(rows):
        sum_i=sum_i+arr[i][i]
        sum_j=sum_j+arr[i][rows-i-1]
    result=abs(sum_i-sum_j)
    return(result)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
