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
    q = int(input())
    for _ in range(q):
        k = int(input())
        d = 1
        while True:
            cnt = 9 * (10 ** (d - 1))
            block = cnt * d
            if k > block:
                k -= block
                d += 1
            else:
                break

        num_index = (k - 1) // d
        digit_index = (k - 1) % d

        number = 10 ** (d - 1) + num_index
        sys.stdout.write(str(number)[digit_index]+"\n")
    
# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
