s = list(map(int, input().split()))
if s!=sorted(s): exit(print('No'))
if min(s)<100 or max(s)>675: exit(print('No'))
for i in s:
    if i%25!=0: exit(print('No'))
print('Yes')