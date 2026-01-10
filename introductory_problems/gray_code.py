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
    output = [""]
    for _ in range(n):
        output2 = []
        for i in output:
            output2.append("0"+i)
        for i in output[::-1]:
            output2.append("1"+i)
        output = output2

    sys.stdout.write("\n".join(output))


    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
