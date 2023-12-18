one = ["AB", "BC", "CD", "DE", "EA"]
two = ["AC", "AD", "BD", "BE", "CE"]

s = input()
t = input()

if s in one or s[1]+s[0] in one: s_type=1
else: s_type=2
if t in one or t[1]+t[0] in one: t_type=1
else: t_type=2

print("Yes") if s_type==t_type else print('No')
