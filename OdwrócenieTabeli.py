import sys

DEBUG = True  # Ustaw na True, aby włączyć komunikaty debug

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    if DEBUG:
        print(f"[DEBUG] Liczba przypadków testowych: {t}", file=sys.stderr)
    index = 1
    output_lines = []
    for test_index in range(1, t+1):
        n = int(data[index])
        index += 1
        # Pobierz n liczb jako elementy tablicy
        arr = data[index:index+n]
        index += n
        if DEBUG:
            print(f"[DEBUG] Przypadek testowy #{test_index}: n = {n}", file=sys.stderr)
            print(f"[DEBUG] Oryginalna tablica: {arr}", file=sys.stderr)
        arr_reversed = arr[::-1]
        if DEBUG:
            print(f"[DEBUG] Odwrócona tablica: {arr_reversed}", file=sys.stderr)
        output_lines.append(" ".join(arr_reversed))
    sys.stdout.write("\n".join(output_lines))

def run_tests():
    """Funkcja uruchamia przykładowe testy, przechwytując wyjście i komunikaty debug."""
    import io
    from contextlib import redirect_stdout, redirect_stderr

    # Test case with n = 100
    max_n_test_case = "100 " + " ".join(map(str, range(1, 101))) + "\n"
    max_n_expected_output = " ".join(map(str, range(100, 0, -1)))

    # Test case with t = 100, each with n = 1
    max_t_test_case = "100\n" + "\n".join("1 " + str(i) for i in range(1, 101)) + "\n"
    max_t_expected_output = "\n".join(str(i) for i in range(1, 101))

    sample_input = f"3\n7 1 2 3 4 5 6 7\n3 3 2 11\n{max_n_test_case}{max_t_test_case}"
    expected_output = "7 6 5 4 3 2 1\n11 2 3\n" + max_n_expected_output + "\n" + max_t_expected_output

    # Przechwytywanie wyjścia
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
    # Jeśli podamy parametr "--test", uruchamiamy testy zamiast zwykłego działania
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        main()
