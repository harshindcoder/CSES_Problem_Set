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
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 1 
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            ans += 1
    sys.stdout.write(str(ans)+"\n")

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
