from algoritmo_de_euclides import *
import random
import math

n = 10000000
co_primes = 0
for i in range(n):
    a = random.randint(1, 100000)
    b = random.randint(1, 100000)
    if is_co_prime(a, b):
        co_primes += 1  
pie = math.sqrt(6 * (n / co_primes))
print(pie)

