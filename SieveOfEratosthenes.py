import sys
import math

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(math.sqrt(max_num)) + 1):
        if is_prime[start]:
            for multiple in range(start*start, max_num + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def segmented_sieve(m, n, primes):
    is_prime = [True] * (n - m + 1)
    if m == 1:
        is_prime[0] = False
    for prime in primes:
        start = max(prime*prime, m + (prime - m % prime) % prime)
        for j in range(start, n + 1, prime):
            is_prime[j - m] = False
    return [num for num, prime in enumerate(is_prime, start=m) if prime]

def main():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    max_n = 0
    test_cases = []
    
    for _ in range(t):
        m = int(data[index])
        n = int(data[index + 1])
        test_cases.append((m, n))
        max_n = max(max_n, n)
        index += 2
    
    primes = sieve_of_eratosthenes(int(math.sqrt(max_n)) + 1)
    
    for m, n in test_cases:
        primes_in_range = segmented_sieve(m, n, primes)
        results.append(primes_in_range)
    
    for result in results:
        for prime in result:
            print(prime)
        print()

if __name__ == "__main__":
    main()