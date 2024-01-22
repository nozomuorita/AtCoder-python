"""公式解説と同じようなやり方"""
h, w = map(int, input().split())
ans = 10**18
#  横
n = 0
for i in range(h):
    n += w
    cnt = h*w - n
    score1 = [n, (w//2)*(h-(i+1)), (w-(w//2))*(h-(i+1))]
    score2 = [n, (h-(i+1))//2 * w, ((h-(i+1))-((h-(i+1))//2)) * w]
    ans = min(ans, max(score1)-min(score1), max(score2)-min(score2))

#  縦
n = 0
for i in range(w):
    n += h
    cnt = h*w - n
    score1 = [n, (h//2)*(w-(i+1)), (h-(h//2))*(w-(i+1))]
    score2 = [n, (w-(i+1))//2 * h, ((w-(i+1))-((w-(i+1))//2)) * h]
    ans = min(ans, max(score1)-min(score1), max(score2)-min(score2))

print(ans)