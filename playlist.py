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
    arr = list(map(int, input().split()))
    i = 0
    ans = 0
    values = set()
    for j in range(n):
        while arr[j] in values:
            values.remove(arr[i])
            i += 1
        values.add(arr[j])
        ans = max(ans,j-i+1)
    sys.stdout.write(str(ans))
   

    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()