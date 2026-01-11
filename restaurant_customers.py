# =======================
# Python CP Template
# (bits/stdc++.h equivalent)
# =======================

import sys
import math
import threading

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
    data = sys.stdin.buffer.read().split()
    n = int(data[0])

    visits = []
    idx = 1
    for _ in range(n):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        visits.append((u, 1))
        visits.append((v, -1))

    visits.sort()

    cur = 0
    ans = 0
    for _, d in visits:
        cur += d
        if cur > ans:
            ans = cur

    sys.stdout.write(str(ans))
    

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
