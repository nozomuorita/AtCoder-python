n = int(input())
a = list(map(int, input().split()))

money, stock = 1000, 0
i = 0

while i<(n-1):
    now, nxt = a[i], a[i+1]
    if now<nxt:
        s = money//now
        money -= now*s
        stock += s
        while i<(n-1) and a[i]<=a[i+1]: i+=1
        s = a[i]*stock
        money += s
        stock = 0
        while i<(n-1) and a[i]>a[i+1]: i+=1
    else: i+=1
        
if stock>0:
    money += a[-1]*stock

print(money)