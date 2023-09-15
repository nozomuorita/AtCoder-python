from itertools import permutations

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

l = list(range(1, n+1))
s = list(permutations(l, n))

for i in range(len(s)):
    if s[i] == tuple(p):
        p_idx = i+1
    if s[i] == tuple(q):
        q_idx = i+1
        
print(abs(p_idx - q_idx))