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
    arr = list(map(int,input().split()))
    n,x = arr[0],arr[1]
    arr = list(map(int,input().split()))
    arr2 = [(y,x) for x,y in enumerate(arr)]
    arr = arr2
    arr2.sort()
    i,j = 0,n-1
    key = True
    while i < j:
        if arr[i][0]+arr[j][0] == x:
            sys.stdout.write(str(arr[i][1]+1)+" "+str(arr[j][1]+1))
            key = False
            break
        elif arr[i][0]+arr[j][0] < x:
            i +=1
        else:
            j -=1
    if key:    
        sys.stdout.write("IMPOSSIBLE")

# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()