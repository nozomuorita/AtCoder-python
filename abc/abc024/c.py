"""
・各民族に対して、各日に移動できる範囲を求める
・どの町からどの町まで移動できるのかを求め、各日の最後に目的地に行けるのならその日が最短
"""
n, d, k = map(int, input().split())
l, r = [], []
for i in range(d):
    _l, _r = map(int, input().split())
    l.append(_l)
    r.append(_r)

for i in range(k):
    s, t = map(int, input().split())
    left, right = -1, -1
    for j in range(d):
        if left==-1 and right==-1:
            if l[j]<=s<=r[j]:
                left, right = l[j], r[j]
        else:
            if l[j]>right or r[j]<left: continue  # この日に移動できる範囲(l[j]~r[j])に前日までにたどり着けないならcontinue
            left = min(left, l[j])
            right = max(right, r[j])
    
        if left<=t<=right:
            print(j+1)
            break