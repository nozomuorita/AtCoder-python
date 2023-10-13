"""
・ある町について、青木派がA人、高橋派がB人であるとする。
・このとき、この町で演説すると高橋派はA+B人増え、青木派はA人減る。
・よって、2*A+Bが一つの町で演説した時の変化。
・この変化が大きいものから演説していく。
・「自分の提出」のWAのやりかたでは、(高橋派の増分, 青木派の減)=(100, 1), (99, 98)であった場合、後者のほうがより答えに近づくのに、ソートした時に前者が先に来てしまう
・なので、WAのやり方はダメ
"""
n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]

s = [2*ab[i][0]+ab[i][1] for i in range(n)]
s.sort(reverse=True)

x = 0
for i in range(n): x-=ab[i][0]

for i in range(n):
    x += s[i]
    if x>0:
        ans = i+1
        break
    
print(ans)