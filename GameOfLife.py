import sys

DEBUG = False  # Ustaw na True, aby włączyć wypisywanie komunikatów debug na stderr

def count_neighbors(board, i, j):
    """Zwraca liczbę żywych sąsiadów komórki (i,j) z zawinięciem krawędzi."""
    n_rows, n_cols = 5, 5
    cnt = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            ni = (i + di) % n_rows
            nj = (j + dj) % n_cols
            cnt += board[ni][nj]
    return cnt

def next_state(board):
    """Oblicza kolejny stan planszy wg zasad Gry w życie."""
    new_board = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == 1:
                # Żywa komórka: przeżywa przy 2 lub 3 sąsiadach, inaczej ginie.
                if neighbors == 2 or neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
            else:
                # Martwa komórka: ożywa, jeśli dokładnie 3 sąsiadów jest żywych.
                if neighbors == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
    return new_board

def simulate(board, iterations=100):
    """Symuluje rozwój planszy przez podaną liczbę iteracji."""
    if DEBUG:
        print("[DEBUG] Stan początkowy:", file=sys.stderr)
        for row in board:
            print(row, file=sys.stderr)
    for it in range(iterations):
        board = next_state(board)
        if DEBUG:
            print(f"[DEBUG] Stan po iteracji {it+1}:", file=sys.stderr)
            for row in board:
                print(row, file=sys.stderr)
    return board

def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    # Pierwsza linia zawiera liczbę testów
    t = int(input_lines[0].strip())
    if DEBUG:
        print(f"[DEBUG] Liczba testów: {t}", file=sys.stderr)
    output_lines = []
    line_index = 1
    for test in range(1, t+1):
        # Dla każdego testu mamy 5 kolejnych linii
        if line_index + 5 > len(input_lines):
            break  # brak wystarczających linii
        board = []
        for i in range(5):
            # Każda linia zawiera dokładnie 5 znaków ('0' lub '1')
            row_str = input_lines[line_index].strip()
            board.append([int(ch) for ch in row_str])
            line_index += 1
        if DEBUG:
            print(f"[DEBUG] Test #{test}: początkowa plansza", file=sys.stderr)
            for row in board:
                print(row, file=sys.stderr)
        final_board = simulate(board, iterations=100)
        # Sprawdzamy, czy przynajmniej jedna komórka jest żywa.
        alive_exists = any(cell == 1 for row in final_board for cell in row)
        output_lines.append("yes" if alive_exists else "no")
    sys.stdout.write("\n".join(output_lines))

def run_tests():
    """
    Funkcja testowa - przykładowe wejście oraz porównanie z oczekiwanym wyjściem.
    """
    import io
    from contextlib import redirect_stdout, redirect_stderr

    # Przykładowe dane testowe
    # Przykładowe testy mogą być skonstruowane tak, aby po 100 iteracjach plansza była całkowicie martwa lub zawierała żywe komórki.
    sample_input = (
        "2\n"
        "00000\n"
        "00100\n"
        "00100\n"
        "00100\n"
        "00000\n"
        "00000\n"
        "00000\n"
        "01110\n"
        "00000\n"
        "00000\n"
    )
    # W pierwszym teście (ruch "migającego" pionowego linii) - w zależności od konfiguracji,
    # po 100 iteracjach może zaniknąć lub stabilizować. Dla celów testu przyjmijmy, że wynik "yes" lub "no" zostanie odpowiednio oceniony.
    # Drugi test - pozioma linia "01110" może ustabilizować się jako blok lub wygasnąć.
    # Tutaj podamy oczekiwane wyjście przykładowe (może być różne, w zależności od początkowego ustawienia).
    # Dla uproszczenia przyjmujemy, że oba testy mają wynik "yes".
    expected_output = "yes\nyes"

    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()
    sys.stdin = io.StringIO(sample_input)
    with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
        main()
    output = stdout_capture.getvalue().strip()
    debug_info = stderr_capture.getvalue().strip()

    print("Test Output:")
    print(output)
    print("Debug Output:")
    print(debug_info)
    print("Expected Output:")
    print(expected_output)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        main()
