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

from collections import Counter

from collections import Counter

def solve():
    s = input().strip()
    n = len(s)
    freq = Counter(s)

    # Global impossibility check
    max_freq = max(freq.values())
    if max_freq > (n + 1) // 2:
        print("-1")
        return

    result = []
    prev = None

    # characters in sorted order once
    chars = sorted(freq.keys())

    for _ in range(n):
        placed = False
        for ch in chars:
            if freq[ch] == 0 or ch == prev:
                continue

            # try ch
            freq[ch] -= 1
            remaining = n - len(result) - 1

            # update max_freq if needed
            old_max = max_freq
            if freq[ch] + 1 == max_freq:
                max_freq = max(freq.values())

            if max_freq <= (remaining + 1) // 2:
                result.append(ch)
                prev = ch
                placed = True
                break
            else:
                # undo
                freq[ch] += 1
                max_freq = old_max

        if not placed:
            print("-1")
            return

    print("".join(result))


    
# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
