# from collections import defaultdict
# import bisect
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# b.sort(reverse=True)
# a.sort()

# db = defaultdict(int)
# da = defaultdict(int)

# na = 0
# for i in range(n):
#     da[a[i]] = na + 1
#     na += 1

# nb = 0
# for i in range(m):
#     db[b[i]] = nb + 1
#     nb += 1

# db_keys = list(db.keys())
# db_keys.sort()
# da_keys = list(da.keys())
# da_keys.sort()
# # print(db_keys)
# # print(da)
# # print(db)

# for key in list(da.keys()):
#     #print(key)
#     # for key in [keys, keys+1]:
#     num = bisect.bisect_left(db_keys, key)
#     if num >= len(db_keys):
#         continue
#     # print('num', num)
#     # print(db_keys[num])
#     if da[key] >= db[db_keys[num]]:
#         print(key)
#         exit()

# print(max(db_keys)+1)

# from collections import defaultdict
# import bisect
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# b.sort(reverse=True)
# a.sort()

# db = defaultdict(int)
# da = defaultdict(int)

# na = 0
# for i in range(n):
#     da[a[i]] = na + 1
#     da[a[i]+1] = na + 1
#     na += 1

# nb = 0
# for i in range(m):
#     db[b[i]] = nb + 1
#     db[b[i]+1] = nb
#     nb += 1

# db_keys = list(db.keys())
# db_keys.sort()
# da_keys = list(da.keys())
# da_keys.sort()
# # print(db_keys)
# # print(da)
# # print(db)
# c = a.copy()
# c_sub = [i+1 for i in b]
# c.extend(c_sub)
# c.sort()

# # for keys in list(da.keys()):
# for keys in c:
#     #print(key)
#     for key in [keys, keys+1]:
#         num = bisect.bisect_left(db_keys, key)
#         if num >= len(db_keys):
#             continue
#         # print('num', num)
#         # print(db_keys[num])
#         if da[key] >= db[db_keys[num]]:
#             print(key)
#             exit()

# print(max(b)+1)

from collections import defaultdict
import bisect
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort(reverse=True)
a.sort()

db = defaultdict(int)
da = defaultdict(int)

na = 0
for i in range(n):
    da[a[i]] = na + 1
    da[a[i]+1] = na + 1
    na += 1

nb = 0
for i in range(m):
    db[b[i]] = nb + 1
    db[b[i]+1] = nb
    nb += 1

db_keys = list(db.keys())
db_keys.sort()
da_keys = list(da.keys())
da_keys.sort()
# print(db_keys)
# print(da)
# print(db)
c = a.copy()
c_sub = [i+1 for i in b]
c.extend(c_sub)
c.sort()

# for keys in list(da.keys()):
for keys in c:
    #print(key)
    if da[keys] >= db[keys]:
        print(keys)
        exit()
        

    
    
    # for key in [keys, keys+1]:
    #     num = bisect.bisect_left(db_keys, key)
    #     if num >= len(db_keys):
    #         continue
    #     # print('num', num)
    #     # print(db_keys[num])
    #     if da[key] >= db[db_keys[num]]:
    #         print(key)
    #         exit()

print(max(b)+1)