from collections import defaultdict, deque, Counter
import copy
from itertools import combinations, permutations, product, accumulate, groupby, chain
from heapq import heapify, heappop, heappush
import math
import bisect
from pprint import pprint
from random import randint
import sys
# sys.setrecursionlimit(700000)
input = lambda: sys.stdin.readline().rstrip('\n')
inf = float('inf')
mod1 = 10**9+7
mod2 = 998244353
def ceil_div(x, y): return -(-x//y)