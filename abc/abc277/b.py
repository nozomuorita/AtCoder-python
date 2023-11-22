N = int(input())
S = []
flag = True

for i in range(N):
    s = input()
    S.append(s)
    
first_ch = ['H', 'D', 'C', 'S']
second_ch = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
for s in S:
    # 一つ目
    if s[0] not in first_ch:
        flag = False
        break
    
    # 二つ目
    if s[1] not in second_ch:
        flag = False
        break
        
# 三つ目
S_set = list(set(S))
if len(S_set) != len(S):
    flag = False
    
# 出力
if flag:
    print('Yes')
else:
    print('No')