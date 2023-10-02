# h==1 or w==1のときはすべて点灯可能らしい
h, w = map(int, input().split())

if h==1 or w==1:
    ans = max(h, w)
else:
    ans = ((h+1)//2) * ((w+1)//2)
        
print(ans)