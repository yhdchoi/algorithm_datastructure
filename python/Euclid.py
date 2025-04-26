# Euclidean Algorithm 유클리드 호제법
# gcd = greatest common denominator
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print(gcd(192, 162))
