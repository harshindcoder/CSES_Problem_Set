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
    x, n = map(int, input().split())
    positions = list(map(int, input().split()))

    # Sorted list of traffic light positions
    lights = [0, x]

    # Multiset of segment lengths
    segments = Counter()
    segments[x] = 1

    max_len = x
    result = []

    for p in positions:
        # Find position to insert
        idx = bisect.bisect_left(lights, p)

        left = lights[idx - 1]
        right = lights[idx]

        # Remove old segment
        old_len = right - left
        segments[old_len] -= 1
        if segments[old_len] == 0:
            del segments[old_len]

        # Add new segments
        left_len = p - left
        right_len = right - p
        segments[left_len] += 1
        segments[right_len] += 1

        # Insert new light
        lights.insert(idx, p)

        # Update maximum segment length
        max_len = max(segments)
        result.append(max_len)

    print(*result)
    
if __name__ == "__main__":
    solve()