#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n ,arr):
    for i in range(1, n):
        small = arr[i]
        j = i-1
        while(j >= 0 and small < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
            print(*arr)
        arr[j+1] = small
    print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
