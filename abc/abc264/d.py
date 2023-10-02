# """
# ・BFSで遷移していき、探索
# """
# from collections import deque
# s = input()
# atcoder  = 'atcoder'
# q = deque()
# q.append((s, 0))
# visited = set()

# while q:
#     word, n = q.popleft()
#     #print(word)
#     if word == atcoder:
#         ans = n
#         break
#     if word in visited:
#         continue
#     visited.add(word)
#     for i in range(len(atcoder)-1):
#         t = list(word)
#         t[i], t[i+1] = t[i+1], t[i]
#         new_word = ''.join(t)
#         if new_word not in visited:
#             q.append((new_word, n+1))
            
# print(ans)

"""
・別解(転倒数)
・https://output-zakki.com/inversion_number/
"""
s = input()
atcoder = list('atcoder') 

sl = [atcoder.index(i) for i in s]

ans = 0
for i in range(len(sl)):
    for j in range(i+1, len(sl)):
        if sl[i] > sl[j]:
            ans += 1
            
print(ans)