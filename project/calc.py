def fact(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a, b):
    result = 0

    if a < 0:
        a *= -1

    if a == 0:
        return abs(b)

    if b == 0:
        return abs(a)
    
    if a == b == 0:
        return 0

    for i in range(1, a+1):
        n=a%i
        m=b%i
        if n == 0 and m == 0:
            result = i


    
    return result