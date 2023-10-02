from collections import defaultdict
k = int(input())
s = input()
t = input()

cards = defaultdict(int)
for i in range(1, 10):
    cards[str(i)] = k
for i in range(len(s)-1):
    cards[s[i]] -= 1
    cards[t[i]] -= 1

w = (9*k) - 8  #  残りのカード枚数
wp = (w*(w-1))  # 残りのカードから2枚選択する場合の数
tp = 0  # 高橋くんが勝つ場合の数

def judge(card):
    score = 0
    for i in range(1, 10):
        score += i * (10**(card.count(str(i))))
    return score

for i in range(1, 10):
    for j in range(1, 10):
        if (i==j) and (cards[str(i)]<2): continue
        if (i!=j) and ((cards[str(i)]<1) or (cards[str(j)]<1)): continue

        score_t = judge(s[:-1]+str(i))
        score_a = judge(t[:-1]+str(j))

        if score_t > score_a:
            if i==j:
                p = (cards[str(i)]*(cards[str(i)]-1))
            else:
                p = (cards[str(i)])*(cards[str(j)])
            tp += p

ans = tp / wp
print(ans)