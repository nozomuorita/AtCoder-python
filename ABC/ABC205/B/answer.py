n = int(input())
a = list(map(int, input().split()))

a_set = set(a)
if len(a_set)==n:
    print('Yes')
else:
    print('No')