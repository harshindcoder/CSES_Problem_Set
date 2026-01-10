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
    arr = [[0]*n for i in range(n)]
    for i in range(n):
        arr[i][0] = i
        arr[0][i] = i
    for i in range(1,n):
        for j in range(1,n):
            if i == j:
                arr[i][j] = 0
            else:
                values = set()
                for k in range(j):
                    values.add(arr[i][k])
                for k in range(i):
                    values.add(arr[k][j])
                put = 1 
                while put in values:
                    put += 1
                arr[i][j] = put
    output = [[""] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            output[i][j] = str(arr[i][j])
    for layer in output:
        sys.stdout.write(" ".join(layer)+"\n")
    



# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
