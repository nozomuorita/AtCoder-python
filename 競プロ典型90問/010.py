n = int(input())
one = [0] # 累積和
two = [0]

for i in range(n):
    c, p = map(int, input().split())
    if c==1:
        one.append(one[-1]+p)
        two.append(two[-1])
    else:
        one.append(one[-1])
        two.append(two[-1]+p)

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    ans_one = one[r] - one[l-1]
    ans_two = two[r] - two[l-1]
    print(ans_one, ans_two)