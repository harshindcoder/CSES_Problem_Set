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
# Utility Functions
# =======================

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# =======================
# Main Logic
# =======================

def solve():
    # Example input
    INF = 10**9+7
    n = int(input())
    arr = [[INF]*n for i in range(n)]
    moves = [[-1,-2],[-1,2],[1,-2],[1,2],[2,1],[2,-1],[-2,1],[-2,-1]]
    q = deque()
    q.append([0,0])
    arr[0][0] = 0
    while q:
        x,y = q.popleft()
        move = arr[x][y]
        for dx,dy in moves:
            if x+dx < n and y+dy < n and x+dx >= 0 and y+dy >= 0 and arr[x+dx][y+dy] == INF:
                arr[x+dx][y+dy] = move+1
                q.append([x+dx,y+dy])
    output = [[str(arr[i][j]) for j in range(n)] for i in range(n)]
    for layer in output:
        sys.stdout.write(" ".join(layer)+"\n")
        

    
            


    
    



# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
