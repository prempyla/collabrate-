def mod_exponentiation(a, b, m):
    result = 1
    a = a % m  
    while b > 0:
        if b % 2:  
            result = (result * a) % m
        a = (a * a) % m  
        b //= 2  
    return result

