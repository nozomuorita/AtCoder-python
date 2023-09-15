from itertools import combinations, permutations, product, accumulate, groupby, chain

n = list(input())
s = list(permutations(n, len(n)))
ans = -1

for i in s:
    for j in range(1, len(n)):
        if (i[0]=='0') or (i[j]=='0'):
            continue
        num1 = int(''.join(i[:j]))
        num2 = int(''.join(i[j:]))

        if (num1*num2) > ans:
            ans = num1*num2
print(ans)