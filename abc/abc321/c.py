"""
・dfsで列挙
"""

import sys
sys.setrecursionlimit(100000000)
k = int(input())

n = []

def dfs(i):
    global n
    n.append(int(i))
    
    #  最大で10桁なので、10であればreturn
    if len(i)==10:
        return
    
    #  最下位桁より小さい数をくっつけて再帰
    for j in range(int(i[-1])-1, -1, -1):
        number = str(i)+str(j)
        dfs(number)
        
for m in range(1, 10):
    dfs(str(m))
    
n.sort()
print(n[k-1])

# """
# ・bit全探索で列挙(未実装)
# """
# k = int(input())

# number = [str(i) for i in range(9, -1, -1)]

# for i in range(2**10):
#     s = ''
#     for j in range(10):
#         if (2>>j) & 1:
#             s += number[j]