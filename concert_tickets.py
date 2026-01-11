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

def solve():
    n, m = map(int, input().split())
    tickets = list(map(int, input().split()))
    customers = list(map(int, input().split()))

    tickets.sort()  # sort ticket prices
    ans = []
    for t in customers:
        # index of first element > t
        idx = bisect.bisect_right(tickets, t) - 1

        if idx >= 0:
            ans.append(str(tickets[idx]))
            tickets.pop(idx)   # remove used ticket
        else:
            ans.append("-1")
    sys.stdout.write("\n".join(ans))


# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
