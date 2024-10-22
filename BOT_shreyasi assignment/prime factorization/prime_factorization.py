def prime_factorization(n):
    if n <= 1:
        return []

    prime_factors = []
    exponent = 0
    while n % 2 == 0:
        n //= 2
        exponent += 1
    if exponent > 0:
        prime_factors.append((2, exponent))

    for i in range(3, int(n**0.5) + 1, 2):
        exponent = 0
        while n % i == 0:
            n //= i
            exponent += 1
        if exponent > 0:
            prime_factors.append((i, exponent))

    if n > 2:
        prime_factors.append((n, 1))

    return prime_factors