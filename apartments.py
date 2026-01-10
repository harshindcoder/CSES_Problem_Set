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
    n,m,k = arr[0],arr[1],arr[2]
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    ans = 0
    i,j = 0,0
    while i < n and j < m:
        if A[i] > B[j]+k:
            j+=1
        elif B[j]-k > A[i]:
            i+=1
        elif  B[j]-k <= A[i] and A[i] <= B[j]+k:
            ans+=1
            i+=1
            j+=1

    sys.stdout.write(str(ans)+"\n")



# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
