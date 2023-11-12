"""
・各インデックスからk個分に火をつけるとして、最短距離を計算し、更新
・idxとk個先のインデックス(idx+k-1)の座標から、正と負なら0から近いほうを2倍した距離が最短
・両方同じ符号なら、遠いほうまで行く距離が最短
"""

n, k = map(int, input().split())
x = list(map(int, input().split()))
ans = float('inf')

idx = 0
while idx+k-1<=(n-1):
    if x[idx]<0 and x[idx+k-1]>=0:
        d = 2*min(abs(x[idx]), x[idx+k-1]) + max(abs(x[idx]), x[idx+k-1])
    elif (x[idx]<0 and x[idx+k-1]<0) or (x[idx]>=0 and x[idx+k-1]>=0):
        d = max(abs(x[idx]), abs(x[idx+k-1]))
        
    ans = min(ans, d)
    idx += 1
    
print(ans)