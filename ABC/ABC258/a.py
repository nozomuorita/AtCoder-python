K = int(input())

if K < 60:
  hh = str(21)
  mm = str(K).zfill(2)
else:
  hh = str(22)
  mm = str(K-60).zfill(2)
  
print(hh + ':' + mm)