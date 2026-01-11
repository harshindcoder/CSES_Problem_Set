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
    arr.sort()
    ans = 0
    for x in arr:
        if x > ans+1:
            break
        ans += x
    sys.stdout.write(str(ans+1))

    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()