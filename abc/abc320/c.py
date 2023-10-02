from itertools import permutations
M=int(input())
S=[]
for _ in range(3):
  s=input()
  S.append(s+s)

def solve(p,d):
  if any(d not in S[i] for i in range(3)): return 10**9
  crr=0
  for i in range(3):
    crr+=S[p[i]][crr%M:].index(d)+1
  return crr-1

ans=10**9
for d in range(10):
  for p in permutations(range(3)):
    ans=min(ans,solve(p,str(d)))

print(ans if ans!=10**9 else -1)

"""
【別解】
・かかる時間は最大でも3*mである。
・mは最大で100なのでO(m**3)としてもとおるので、各リールを止める時間を0~3*mについてfor文で全探索
・止める時間が同じになる場合、(i==j)or(j==k)or(k==i)、これはできないので飛ばす
・各時刻i, j, kで止まる数字が同じなら答えを比較し、更新(i, j, kで一番値の大きいものがその止め方のかかる時間)
"""

# m = int(input())
# s1 = input()
# s2 = input()
# s3 = input()
# s = [s1, s2, s3]

# # ここの処理は下のfor文でも判定できるのでなくても通る
# s1_set = set(s1)
# s2_set = set(s2)
# s3_set = set(s3)
# f = False
# for i in s1_set:
#     if (i in s2_set) and (i in s3_set):
#         f = True
#         break
# if not f:
#     print(-1)
#     exit()

# ans = float('INF')
# for i in range(3*m):
#     for j in range(3*m):
#         for k in range(3*m):
#             if (i==j) or (j==k) or (k==i):
#                 continue
#             if s[0][i%m] == s[1][j%m] == s[2][k%m]:
#                 ans = min(ans, max(i, j, k))
                
# print(ans) 