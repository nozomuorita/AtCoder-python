s = input()
s1, s2 = s[:2], s[2:]

ym, my = False, False
if ("00"<=s1<="99") and ("01"<=s2<="12"): ym=True
if ("01"<=s1<="12") and ("00"<=s2<="99"): my=True

if ym and my: print("AMBIGUOUS")
elif ym: print("YYMM")
elif my: print("MMYY")
else: print("NA")