n = int(input())
w = input()[:-1].split(" ")

ans = w.count("TAKAHASHIKUN") + w.count("Takahashikun") + w.count("takahashikun")
print(ans)