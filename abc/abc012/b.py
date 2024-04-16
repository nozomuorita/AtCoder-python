n = int(input())
h = str(n//3600).zfill(2)
n -= (n//3600)*3600
m = str(n//60).zfill(2)
n -= (n//60)*60
s = str(n).zfill(2)
print(h+':'+m+':'+s)