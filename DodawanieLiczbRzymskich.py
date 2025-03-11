import sys

DEBUG = False  # Ustaw na True, aby włączyć komunikaty debug (są wypisywane na stderr)

def roman_to_int(s):
    """
    Konwertuje napis w zapisie rzymskim (s) na odpowiadającą mu liczbę całkowitą.
    Zakładamy poprawny zapis rzymski.
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(s):
        # Jeśli następny symbol jest większy, stosujemy zasadę odejmowania.
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            total += roman_map[s[i+1]] - roman_map[s[i]]
            i += 2
        else:
            total += roman_map[s[i]]
            i += 1
    return total

def int_to_roman(num):
    """
    Konwertuje liczbę całkowitą (num) na zapis rzymski.
    """
    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    roman = []
    for val, numeral in values:
        while num >= val:
            roman.append(numeral)
            num -= val
    return "".join(roman)

def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return

    output_lines = []
    for line in input_lines:
        if line.strip():
            tokens = line.strip().split()
            if len(tokens) != 2:
                continue  # pomiń linie, które nie zawierają dokładnie dwóch liczb rzymskich
            roman1, roman2 = tokens
            if DEBUG:
                print(f"[DEBUG] Przetwarzam: {roman1} oraz {roman2}", file=sys.stderr)
            num1 = roman_to_int(roman1)
            num2 = roman_to_int(roman2)
            if DEBUG:
                print(f"[DEBUG] Konwersja: {roman1} -> {num1}, {roman2} -> {num2}", file=sys.stderr)
            total = num1 + num2
            roman_sum = int_to_roman(total)
            if DEBUG:
                print(f"[DEBUG] Suma: {num1} + {num2} = {total} -> {roman_sum}", file=sys.stderr)
            output_lines.append(roman_sum)
    sys.stdout.write("\n".join(output_lines))

def run_tests():
    """
    Funkcja testowa. Uruchamia przykładowe testy i wyświetla wyjście oraz komunikaty debug.
    """
    import io
    from contextlib import redirect_stdout, redirect_stderr

    # Przykładowe dane testowe:
    # I + V = 1 + 5 = 6 -> VI
    # X + IV = 10 + 4 = 14 -> XIV
    # MM + M = 2000 + 1000 = 3000 -> MMM
    sample_input = "I V\nX IV\nMM M\n"
    expected_output = "VI\nXIV\nMMM"

    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()
    # Ustawiamy przykładowe wejście
    sys.stdin = io.StringIO(sample_input)
    with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
        main()
    output = stdout_capture.getvalue()
    debug_info = stderr_capture.getvalue()

    print("Test Output:")
    print(output)
    print("Debug Output:")
    print(debug_info)
    print("Expected Output:")
    print(expected_output)

if __name__ == '__main__':
    # Jeśli uruchomimy skrypt z parametrem "--test", wykonane zostaną testy.
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        main()
