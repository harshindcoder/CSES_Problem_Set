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

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    i,j = 0,0
    value = 1
    group = Counter()
    for j in range(len(arr)):
        while arr[j] in group:
            group.pop(arr[i])
            i += 1
        group[arr[j]] += 1
        result += j-i+1
    print(result)





    
    
if __name__ == "__main__":
    solve()