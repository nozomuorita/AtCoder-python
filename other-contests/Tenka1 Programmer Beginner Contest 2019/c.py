n = int(input())
s = input()

left = [0, 0]
right = [s.count("#"), s.count(".")]   # (black, white)
ans = min(s.count("#"), s.count("."))

for i in range(n):
    if s[i]=="#": left[0]+=1; right[0]-=1
    else: left[1]+=1; right[1]-=1
    
    score = left[0] + right[1]
    ans = min(ans, score)

print(ans)