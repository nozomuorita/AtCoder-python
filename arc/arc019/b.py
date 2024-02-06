s = input()
l = len(s)

kaibun = 0
for i in range(l//2):
    if s[i]!=s[l-i-1]: kaibun+=1
kaibun = min(kaibun, 2)

ans = 0
match kaibun:
    case 0:
        for i in range(l//2):
            ans += 25*2
    case 1:
        for i in range(l//2):
            if s[i]==s[l-i-1]: ans+=25*2
            else: ans+=24*2
        if l%2==1: ans+=25
    case 2:
        for i in range(l//2):
            if s[i]==s[l-1-i]: ans+=25*2
            else: ans+=25*2
        if l%2==1: ans+=25

print(ans)