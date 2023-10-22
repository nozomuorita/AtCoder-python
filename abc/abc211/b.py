s1 = input()
s2 = input() 
s3 = input()
s4 = input()

s = [s1, s2, s3, s4]
if len(set(s))==4:
    print("Yes")
else:
    print("No")