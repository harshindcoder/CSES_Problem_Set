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
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    colors = ['A', 'B', 'C', 'D']
    ans = [[''] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            forbidden = set()
        
        # Original character must be changed
            forbidden.add(grid[i][j])
        
        # Check top neighbor
            if i > 0:
                forbidden.add(ans[i-1][j])
        
        # Check left neighbor
            if j > 0:
                forbidden.add(ans[i][j-1])
        
        # Choose any valid color
            for c in colors:
                if c not in forbidden:
                    ans[i][j] = c
                    break

# Print result
    for row in ans:
        print("".join(row))


# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
