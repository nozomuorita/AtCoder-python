s = input()

if len(s)!=8: exit(print('No'))
if ord(s[0])<ord("A") or ord("Z")<ord(s[0]): exit(print('No'))
if ord(s[-1])<ord("A") or ord("Z")<ord(s[-1]): exit(print('No'))

for i in s[1:-1]:
    if ord(i)<ord("0") or ord("9")<ord(i): exit(print('No'))

if int(s[1:-1])<100000 or 999999<int(s[1:-1]): exit(print('No'))

print('Yes')