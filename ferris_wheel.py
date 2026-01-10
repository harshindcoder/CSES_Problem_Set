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
    arr = list(map(int, input().split()))
    n,x = arr[0],arr[1]
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    i,j = 0,n-1
    while i <= j:
        if i < j and A[i] + A[j] <= x:
            ans += 1
            i+=1
            j-=1
        else:
            ans += 1
            j-=1
    
    sys.stdout.write(str(ans)+"\n")



# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
