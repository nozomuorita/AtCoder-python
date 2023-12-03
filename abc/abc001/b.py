m = int(input())
m /= 1000

if m < 0.1:
    ans = '00'
elif m <= 5:
    ans = str(int(m * 10))
    if len(ans)==1:
        ans = '0' + ans
elif m <= 30:
    ans = str(int(m + 50))
elif m <= 70:
    ans = str(int((m - 30) / 5 + 80))
else:
    ans = '89'

print(ans)