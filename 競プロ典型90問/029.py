from atcoder.lazysegtree import LazySegTree

# 区間演算op
def op(data1, data2):
    return max(data1, data2)

# opの単位元 op(data1, e) = data1
e = 0

# lazyをdataに作用させる
def mapping(lazy_upper, data_lower):
    if lazy_upper == -1:
        return data_lower
    else:
        return lazy_upper

# lazyをlazyに作用させる
def composition(lazy_upper, lazy_lower):
    if lazy_upper == -1:
        return lazy_lower
    else:
        return lazy_upper

# mapping(_id, data_lower) = data_lower
_id = 0

w, n = map(int, input().split())
lst = [-1]*w
z = LazySegTree(op, e, mapping, composition, _id, lst)

for i in range(n):
    l, r = map(int, input().split())
    l -= 1
    height = z.prod(l, r)
    z.apply(l, r, height+1)
    print(height+1)