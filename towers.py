# =======================
# Python CP Template
# (bits/stdc++.h equivalent)
# =======================

import sys

# Fast I/O
input = sys.stdin.readline

# Common imports
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations, product, accumulate
from functools import lru_cache, reduce
import heapq
import bisect

# Constants
MAX = float('inf')
MIN = float('-inf')
MOD = 10**9 + 7

# =======================
# Main Logic
# =======================


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    values = []
    for x in arr:
        if not values or values[-1] <= x:
            values.append(x)
        else:
            i,j = 0,len(values)-1
            point = -1
            while i <= j:
                mid = (i+j)//2
                if values[mid] > x:
                    point = mid
                    j = mid-1
                else:
                    i = mid+1
            values[point] = x
    sys.stdout.write(str(len(values)))

   

    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()