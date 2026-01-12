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
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    pos = [0] * (n + 1)
    for i in range(n):
        pos[arr[i]] = i

    ans = 1
    for i in range(2, n + 1):
        if pos[i] < pos[i - 1]:
            ans += 1

    res = []

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        x = arr[a]
        y = arr[b]

        affected = set()
        for v in (x, y):
            if v > 1:
                affected.add((v - 1, v))
            if v < n:
                affected.add((v, v + 1))

        # remove old contributions
        for u, v in affected:
            if pos[u] > pos[v]:
                ans -= 1

        # swap in arr
        arr[a], arr[b] = arr[b], arr[a]
        pos[x], pos[y] = pos[y], pos[x]

        # add new contributions
        for u, v in affected:
            if pos[u] > pos[v]:
                ans += 1

        res.append(str(ans))

    print("\n".join(res))
   

    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()