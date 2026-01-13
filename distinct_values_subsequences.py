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
    arr = Counter(arr)
    result = 1
    for value,count in arr.items():
        result*= (count+1)
        result %= MOD 
    print(result%MOD-1)





    
    
if __name__ == "__main__":
    solve()