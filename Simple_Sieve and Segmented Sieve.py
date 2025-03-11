import sys
import math

DEBUG = True  # Ustaw na True, aby włączyć komunikaty debug

def simple_sieve(limit):
    """Zwraca listę liczb pierwszych do 'limit' przy użyciu klasycznego sita."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            for j in range(num * num, limit + 1, num):
                sieve[j] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def segmented_sieve(m, n, primes):
    """Zwraca listę liczb pierwszych w przedziale [m, n] używając wcześniej obliczonych liczb pierwszych."""
    size = n - m + 1
    segment = [True] * size
    
    for p in primes:
        if p * p > n:
            break
        # Znajdź najmniejszą wielokrotność p w przedziale [m, n]
        start = max(p * p, ((m + p - 1) // p) * p)
        for j in range(start, n + 1, p):
            segment[j - m] = False

    # Specjalny przypadek: jeśli m == 1, to 1 nie jest liczbą pierwszą
    if m == 1:
        segment[0] = False
    
    return [i + m for i, is_prime in enumerate(segment) if is_prime]

def main():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    t = int(input_data[0])
    cases = []
    index = 1
    max_n = 0
    for _ in range(t):
        m = int(input_data[index])
        n = int(input_data[index+1])
        cases.append((m, n))
        max_n = max(max_n, n)
        index += 2
    
    if DEBUG:
        print(f"[DEBUG] Liczba przypadków testowych: {t}", file=sys.stderr)
        print(f"[DEBUG] Maksymalna wartość n: {max_n}", file=sys.stderr)
    
    # Oblicz liczby pierwsze do sqrt(max_n)
    limit = int(math.sqrt(max_n)) + 1
    primes = simple_sieve(limit)
    
    if DEBUG:
        print(f"[DEBUG] Liczby pierwsze do {limit}: {primes}", file=sys.stderr)
    
    output_lines = []
    case_number = 1
    for m, n in cases:
        if DEBUG:
            print(f"[DEBUG] Przetwarzam przypadek testowy #{case_number}: zakres [{m}, {n}]", file=sys.stderr)
        primes_in_range = segmented_sieve(m, n, primes)
        if DEBUG:
            print(f"[DEBUG] Znaleziono {len(primes_in_range)} liczb pierwszych w zakresie [{m}, {n}]", file=sys.stderr)
        for prime in primes_in_range:
            output_lines.append(str(prime))
        output_lines.append("")  # pusta linia oddzielająca przypadki
        case_number += 1
    
    # Usuń ostatnią pustą linię, jeśli istnieje.
    if output_lines and output_lines[-1] == "":
        output_lines.pop()
    
    sys.stdout.write("\n".join(output_lines))

if __name__ == '__main__':
    main()
