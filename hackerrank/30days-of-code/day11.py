#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

highest = -100
for i in range(4):
    s = 0
    for j in range(4):
        s = 0
        #print(arr[i][j])
        s += arr[i][j] + arr[i][j+1] + arr[i][j+2]
        #print(s)
        s += arr[i+1][j+1]
        #print(s)
        s += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        #print(s)
        if (s > highest):
            highest = s
    #print(s)
    
print(highest)

