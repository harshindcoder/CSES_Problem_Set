# =======================
# Python CP Template
# (bits/stdc++.h equivalent)
# =======================

import sys
import math
import threading

# Fast I/O
input = sys.stdin.readline
def print(x):
    sys.stdout.write(x)
    sys.stdout.flush()

# Common imports
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations, product, accumulate
from functools import lru_cache, reduce
import heapq
import bisect

# Constants
INF = float('inf')
MOD = 10**9 + 7

# =======================
# Utility Functions
# =======================

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# =======================
# Main Logic
# =======================

def solve():
    # Example input
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    def sums(i,cursum):
        if i == n:
            return abs(total-2*cursum)
        value1 = sums(i+1,cursum+arr[i])
        value2 = sums(i+1,cursum)
        return min(value1,value2)
    ans = sums(0,0)
    sys.stdout.write(str(ans))

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
