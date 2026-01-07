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
# Main Logic
# =======================

def solve():
    # Example input
    n = int(input())
    arr = list(map(int, input().split()))

    # Example computation
    ans = 0

    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            ans += arr[i-1]-arr[i]
            arr[i] = arr[i-1]
    print(str(ans))

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
