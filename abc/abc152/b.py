a, b = map(int,  input().split())
ans1 = str(a)*b
ans2 = str(b)*a
print(min(ans1, ans2))