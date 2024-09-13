'''https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    DATA = bin(n)

    MAXIMUM = 0
    CURRENT = 0

    for num in DATA:
        if num == '1':
            CURRENT = CURRENT + 1
        else:
            MAXIMUM = max(MAXIMUM, CURRENT)
            CURRENT = 0

    print(max(MAXIMUM, CURRENT))
