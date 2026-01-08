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
    arr = [list(input().strip()) for _ in range(8)]
    col = [True] * 8
    diag1 = [True] * 15      # i + j
    diag2 = [True] * 15      # i - j + 7

    ans = 0

    def backtrack(r):
        nonlocal ans
        if r == 8:
            ans += 1
            return

        for c in range(8):
            if arr[r][c] == "*":
                continue
            if col[c] and diag1[r + c] and diag2[r - c + 7]:
                col[c] = diag1[r + c] = diag2[r - c + 7] = False
                backtrack(r + 1)
                col[c] = diag1[r + c] = diag2[r - c + 7] = True

    backtrack(0)
    sys.stdout.write(str(ans))
        
            

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
