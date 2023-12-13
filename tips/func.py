"""
・最大公約数, gcd
"""
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

"""
・最小公倍数, lcm
"""
def lcm(a, b):
    return (a*b) // gcd(a, b)