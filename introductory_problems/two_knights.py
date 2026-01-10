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
    n = int(input())
    res = []
    for k in range(1, n + 1):
        total = k * k * (k * k - 1) // 2
        attack = 4 * (k - 1) * (k - 2)
        res.append(str(total - attack))
    sys.stdout.write("\n".join(res))
    
    
 
 
# =======================
# Entry Point
# =======================
 
if __name__ == "__main__":
    solve()