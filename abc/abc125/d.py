#!/usr/bin/python
# -*- coding: utf-8 -*-
n = int(input())
a = list(map(int, input().split()))

neg = 0
zero = 0
mn = 10**18
ans = 0
for i in range(n):
    if a[i]==0: zero+=1
    elif a[i]<0: neg+=1
    ans += abs(a[i])
    mn = min(mn, abs(a[i]))

if neg%2==0: print(ans)
else:
    if zero>0: print(ans)
    else: print(ans-mn*2)
        
