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
    word = input().strip()
    word_count = defaultdict(int)
    for ch in word:
        word_count[ch] += 1
    front = ""
    middle = ""
    ans = ""
    odds = 0
    for x,y in word_count.items():
        if y%2 == 1:
            odds += 1
            middle += (x*y)
            if odds > 1:
                sys.stdout.write("NO SOLUTION\n")
                return
        else:
            value = y//2
            front+=(x * value) 
    sys.stdout.write(front+middle+front[::-1]+"\n")

    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
