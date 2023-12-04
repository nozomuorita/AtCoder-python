a, b = map(int, input().split())
if a==b: exit(print("1.000"))
c = (10**4)*b//a

if c%10>=5: c//=10; c+=1
else: c//=10

ans = list(str(c))
ans = "0." + "".join(ans)
if len(ans)<5: ans+="0"*(5-len(ans))
print(ans)