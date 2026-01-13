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

import sys
input = sys.stdin.readline

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        """ smallest index i such that sum(i) >= k """
        idx = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bit_mask >>= 1
        return idx + 1


def solve():
    n, k = map(int, input().split())

    fw = Fenwick(n)
    for i in range(1, n + 1):
        fw.add(i, 1)

    pos = 0
    alive = n
    ans = []

    for _ in range(n):
        pos = (pos + k) % alive
        idx = fw.kth(pos + 1)
        ans.append(idx)
        fw.add(idx, -1)
        alive -= 1

    print(*ans)


if __name__ == "__main__":
    solve()

