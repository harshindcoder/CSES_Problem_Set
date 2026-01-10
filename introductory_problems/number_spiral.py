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
    out = []
    for _ in range(n):
        arr = list(map(int, input().split()))
        x,y = arr[0],arr[1]
        edge = max(x,y)
        ans = (edge-1)**2 + edge
        if x < edge:
            if y%2 == 0:
                ans -= (y-x)
            else:
                ans += (y-x)
        elif y < edge:
            if x%2 == 0:
                ans += (x-y)
            else:
                ans -= (x-y)
        out.append(str(ans))
    sys.stdout.write("\n".join(out))

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
