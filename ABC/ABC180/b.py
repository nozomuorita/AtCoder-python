n = int(input())
x = list(map(int, input().split()))

ans1, ans2, ans3 = 0, 0, -1
for i in x:
    ans1 += abs(i)
    ans2 += abs(i) ** 2
    ans3 = max(ans3, abs(i))
    
ans2 = ans2 ** 0.5
print(ans1)
print(ans2)
print(ans3)