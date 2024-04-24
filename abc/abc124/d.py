"""
・0と1の塊ごとにまとめる([(0が3個), (1が2個)...]みたいに)
・左から順に、塊を取り出し、1なら追加
・0の場合はkに満たないなら追加し、kを+1、kがいっぱいなら、すでに追加した塊(done)から取り出していく作業に移る
・0の塊が取り出せるまで取り出し、scoreを減らしていく
・以上をdequeで行う
"""
from collections import deque
n, k = map(int, input().split())
s = input()

s2 = deque()
zero_one=0 if s[0]=="0" else 1
num = 1

for i in range(1, n):
    if s[i]==s[i-1]:
        num += 1
    else:
        s2.append((num, zero_one))
        num = 1
        zero_one=0 if s[i]=="0" else 1

s2.append((num, zero_one))

score = 0
K = 0
ans = 0
done = deque()
while s2:
    num, zero_one = s2.popleft()
    if zero_one==0:
        if K<k:
            score += num
            K += 1
            done.append((num, zero_one))
        else:
            while 1:
                num2, zero_one2 = done.popleft()
                score -= num2
                if zero_one2==0:
                    break
            score += num
            done.append((num, zero_one))
    else:
        score += num
        done.append((num, zero_one))
    
    ans = max(ans, score)

print(ans)