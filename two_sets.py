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
    l,m = n//2, (n-1)//2
    if n == 1 or (n%2 == 0 and l%2 != 0) or (n%2 == 1 and m%2 != 1):
        sys.stdout.write("NO")
        return
    
    list1 = []
    list2 = []

    if n%2 == 0 and l%2 == 0:
        for i in range(1,l//2+1):
            list1.append(str(i))
            list1.append(str(n+1-i))
        for i in range(l//2+1,l+1):
            list2.append(str(i))
            list2.append(str(n+1-i))
    
    if n%2 == 1 and m%2 == 1:
        list1.append(str(n))
        for i in range(1,m//2+1):
            list1.append(str(i))
            list1.append(str(n-i))
        for i in range(m//2+1,m+1):
            list2.append(str(i))
            list2.append(str(n-i))
    sys.stdout.write("YES\n")
    sys.stdout.write(str(len(list1))+"\n")
    sys.stdout.write(" ".join(list1)+"\n")
    sys.stdout.write(str(len(list2))+"\n")
    sys.stdout.write(" ".join(list2)+"\n")



# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
