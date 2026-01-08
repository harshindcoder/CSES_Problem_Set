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

def backtrack(
    state: list[str], choices: list[str], selected: list[bool], res: set[str]
):
    """Backtracking algorithm: Permutations I"""
    # When the state length equals the number of elements, record the solution
    if len(state) == len(choices):
        res.add("".join(state))
        return
    # Traverse all choices
    for i, choice in enumerate(choices):
        # Pruning: do not allow repeated selection of elements
        if not selected[i]:
            # Attempt: make choice, update state
            selected[i] = True
            state.append(choice)
            # Proceed to the next round of selection
            backtrack(state, choices, selected, res)
            # Backtrack: undo choice, restore to previous state
            selected[i] = False
            state.pop()

def permutations_i(nums: list[str]) -> set[str]:
    """Permutations I"""
    res = set()
    backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
    return res


# =======================
# Main Logic
# =======================

def solve():
    word = list(input().strip())
    output = list(permutations_i(word))
    output.sort()
    sys.stdout.write(str(len(output))+"\n")
    for x in output:
       sys.stdout.write(x+"\n")

    
    
# =======================
# Entry Point
# =======================

if __name__ == "__main__":
    solve()
