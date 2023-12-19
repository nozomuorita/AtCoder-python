from collections import Counter
n = int(input())
a = list(map(int, input().split()))

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else: f += 2
    if n != 1: a.append(n)
    return a

two, three = [], []
other = set()
for i in range(n):
    c = Counter(prime_factorize(a[i]))
    st = set()
    two.append(c[2])
    three.append(c[3])
    for key in list(c.keys()):
        if key!=2 and key!=3: st.add(key)
    
    if i==0: other|= st
    else:
        if other != (other|st): exit(print(-1))

ans = 0
two.sort(reverse=True)
three.sort(reverse=True)
mn_two, mn_three = two[-1], three[-1]
for i in range(len(two)):
    if two[i]!=mn_two: ans+=two[i]-mn_two
for i in range(len(three)):
    if three[i]!=mn_three: ans+=three[i]-mn_three
print(ans)