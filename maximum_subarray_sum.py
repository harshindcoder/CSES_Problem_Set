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
INF = float('inf')
MOD = 10**9 + 7

# =======================
# Main Logic
# =======================


def solve():
    n = int(input())
    arr = list(map(int,input().split()))
    ans = float('-inf')
    value = 0
    for x in arr:
        value = max(value+x,x)
        ans = max(ans,value)
    sys.stdout.write(str(ans))

    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()