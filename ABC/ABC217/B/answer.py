s1 = input()
s2 = input()
s3 = input()
s = [s1, s2, s3]

contests = ['ABC', 'ARC', 'AGC', 'AHC']

for i in contests:
    if i not in s:
        print(i)