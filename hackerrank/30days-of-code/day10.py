#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    binary = ''
    ones = 0
    g_len = 0
    l_len = 0
    while (n > 0):

        if (n % 2 == 1 and l_len == 0):
            l_len += 1
        elif (n % 2 == 1 and l_len > 0):
            l_len += 1
        elif (n % 2 == 0 and l_len > 0):
            #print(l_len, g_len)
            if (l_len > g_len):
                g_len = l_len
            l_len = 0
                
        #print(n, n%2, l_len, g_len)
                
        n = int(n/2)

    if (l_len > g_len):
        g_len = l_len
    print(g_len)
