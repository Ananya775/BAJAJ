from math import gcd
from functools import reduce

def fibonacci(n: int):
    if n < 0:
        raise ValueError("Invalid input")

    if n == 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(arr):
    return [x for x in arr if isinstance(x, int) and is_prime(x)]

def lcm(arr):
    def _lcm(a, b):
        return abs(a * b) // gcd(a, b)
    return reduce(_lcm, arr)

def hcf(arr):
    return reduce(gcd, arr)
