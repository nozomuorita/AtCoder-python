n = int(input())
a = list(map(int, input().split()))

a_front = [0]
for i in a:
    a_front.append(max(a_front[-1], i))
a_back = [0]
for i in reversed(a):
    a_back.append(max(a_back[-1], i))

d = int(input())
for i in range(d):
    l, r = map(int, input().split())
    ans = max(a_front[l-1], a_back[n-r])
    print(ans)