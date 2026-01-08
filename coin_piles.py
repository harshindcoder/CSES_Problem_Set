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
    n = int(input())
    for _ in range(n):
        arr = list(map(int, input().split()))
        x,y = arr[0],arr[1]
        if (2*y-x)%3 == 0 and (2*x-y)%3 == 0 and 2*y >= x and 2*x >= y:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")

    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
