def gcd(a,b):
    if b is 0: return a
    return gcd(b,a%b)
print(gcd(357,234))