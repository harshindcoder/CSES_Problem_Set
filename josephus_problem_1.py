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
    dq = deque(range(1, n + 1))
    ans = []

    while dq:
        dq.rotate(-1)      # move first element to back
        ans.append(dq.popleft())

    print(*ans)

if __name__ == "__main__":
    solve()