n = int(input())
t = list(map(int, input().split()))
s = sum(t)

for i in range(int(input())):
    p, x = map(int, input().split())
    print(s-t[p-1]+x)