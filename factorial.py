# The factorial of the integer , written , is defined as:

# Calculate and print the factorial of a given integer.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    result=1
    for i in range(n):
        result=result*(n-i)
    print(result)
    return

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
