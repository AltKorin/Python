import random

t = 5  # Liczba testów
n = 100000  # Liczba osób
filename = "large_test_input.txt"
        
def generate_large_test_case(filename, t, n):
    with open(filename, 'w') as f:
        f.write(f"{t}\n")
        for _ in range(t):
            f.write(f"{n}\n")
            for _ in range(n):
                accusation = random.randint(1, n)
                f.write(f"{accusation}\n")

generate_large_test_case(filename, t, n)
