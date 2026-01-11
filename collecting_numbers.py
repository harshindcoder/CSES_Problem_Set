# =======================
# Python CP Template
# (bits/stdc++.h equivalent)
# =======================

import sys

# Fast I/O
input = sys.stdin.readline

# Common imports
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations, product, accumulate
from functools import lru_cache, reduce
import heapq
import bisect

# Constants
MAX = float('inf')
MIN = float('-inf')
MOD = 10**9 + 7

# =======================
# Main Logic
# =======================


def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    arr2 = [0] * n
    ans = 1
    for x,y in enumerate(arr):
        arr2[y-1] = x
    for i in range(1,n):
        if arr2[i] < arr2[i-1]:
            ans+=1
    sys.stdout.write(str(ans))

    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()