
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
# given n number of socks and array of colors of the socks. How many pairs are there?
# count number of a single color, there will be count // 2 number of pairs
# add number of pairs to result and loop to next number
# added cache to prevent counting a number again


def sockMerchant(n, ar):
    result = 0
    cache = []
    for i in range(n-1):
        if ar[i] not in cache:
            cache.append(ar[i])
            count = ar.count(ar[i])
            pairs = count // 2
            result += pairs

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
