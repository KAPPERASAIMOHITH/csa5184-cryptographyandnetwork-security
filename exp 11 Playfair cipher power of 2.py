import math

# Using Stirling's approximation for factorial
def stirling_approximation(n):
    return math.sqrt(2 * math.pi * n) * (n / math.e)**n

# Compute approximate power of 2 for 25!
n_factorial = stirling_approximation(25)
x = math.log2(n_factorial)

print(f"Approximate power of 2 for the number of keys: 2^{round(x)}")

