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
    m = int(input())
    for _ in range(m):
        arr = list(map(int, input().split()))
        n,a,b = arr[0],arr[1],arr[2]
        if a == 0 and b != 0:
            sys.stdout.write("NO\n")
        elif a != 0 and b == 0:
            sys.stdout.write("NO\n")
        elif a+b > n:
            sys.stdout.write("NO\n")
        else:
            B = [i for i in range(0,n)]
            A = [str(i+1) for i in range(0,n)]
            Bn = [i for i in range(0,n)]
            p = a+b 
            for i in range(p):
                Bn[i] = (B[i] + a)%p
            B = [str(i+1) for i in Bn]
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(A)+"\n")
            sys.stdout.write(" ".join(B)+"\n")

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
