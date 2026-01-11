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

import bisect
import sys
sys.setrecursionlimit(10**7)

class SegTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0] * (4 * n)

    def build(self, idx, l, r, arr):
        if l == r:
            self.seg[idx] = arr[l]
            return
        mid = (l + r) // 2
        self.build(idx*2, l, mid, arr)
        self.build(idx*2+1, mid+1, r, arr)
        self.seg[idx] = self.seg[idx*2] + self.seg[idx*2+1]

    def query(self, idx, l, r, ql, qr):
        if ql > r or qr < l or self.seg[idx] == 0:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        # go right first (largest ≤ t)
        res = self.query(idx*2+1, mid+1, r, ql, qr)
        if res != -1:
            return res
        return self.query(idx*2, l, mid, ql, qr)

    def update(self, idx, l, r, pos):
        if l == r:
            self.seg[idx] -= 1
            return
        mid = (l + r) // 2
        if pos <= mid:
            self.update(idx*2, l, mid, pos)
        else:
            self.update(idx*2+1, mid+1, r, pos)
        self.seg[idx] = self.seg[idx*2] + self.seg[idx*2+1]


def solve():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    t = list(map(int, input().split()))

    prices = sorted(set(h))
    comp = {v: i for i, v in enumerate(prices)}

    freq = [0] * len(prices)
    for x in h:
        freq[comp[x]] += 1

    st = SegTree(len(prices))
    st.build(1, 0, len(prices)-1, freq)
    ans = []
    for x in t:
        idx = bisect.bisect_right(prices, x) - 1
        if idx < 0:
            ans.append("-1")
            continue
        pos = st.query(1, 0, len(prices)-1, 0, idx)
        if pos == -1:
            ans.append("-1")
        else:
            ans.append(str(prices[pos]))
            st.update(1, 0, len(prices)-1, pos)
    sys.stdout.write("\n".join(ans))



# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
