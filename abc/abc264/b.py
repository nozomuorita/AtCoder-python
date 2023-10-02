# 真ん中からのチェビシェフ距離が偶数なら白
# 奇数なら黒
R, C = map(int, input().split())

c_dist = max(abs(8-R), abs(8-C)) #チェビシェフ距離
if c_dist % 2 == 0:
  print('white')
else:
  print('black')