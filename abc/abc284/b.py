t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [1 if i%2!=0 else 0 for i in a]
    print(ans.count(1))