s = input()
yy = int(s[:2])
mm = int(s[2:])

if 1<=yy<=12 and 1<=mm<=12:
    print("AMBIGUOUS")
elif 1<=yy<=12:
    print("MMYY")
elif 1<=mm<=12:
    print("YYMM")
else:
    print("NA")