# =======================
# Python CP Template
# (bits/stdc++.h equivalent)
# =======================

import sys
import math
import threading

# Fast I/O
input = sys.stdin.readline



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
    if n == 2 or  n == 3:
        sys.stdout.write("NO SOLUTION")
        return
    out = []
    for i in range(2,n+1,2):
        out.append(str(i))
    for i in range(1,n+1,2):
        out.append(str(i))
    sys.stdout.write(" ".join(out))
    
    
# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
