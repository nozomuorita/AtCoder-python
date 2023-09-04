n = input()
pon = ['0', '1', '6', '8']

if n[-1]=='3':
    print('bon')
elif n[-1] in pon:
    print('pon')
else:
    print('hon')