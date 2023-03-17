Given an array of integers, find the sum of its elements.

For example, if the array ar = [1,2,3],1 + 2 + 3 = 6 , so return 6.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CODE:

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum=0
    for i in range(0,ar_count):
        sum = sum + ar[i]
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
