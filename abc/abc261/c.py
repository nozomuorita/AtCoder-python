N = int(input())
memo = {}

for i in range(N):
    s = input()
    if s in memo:
        print(f"{s}({memo[s]})")
        memo[s] += 1
    else:
        memo[s] = 1
        print(s)
