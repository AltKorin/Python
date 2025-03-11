import sys
from collections import deque

DEBUG = False  # Ustaw na True, aby włączyć wypisywanie komunikatów debug na stderr

def can_exit(labyrinth_str):
    """
    Sprawdza, czy z danego labiryntu (opisany ciągiem 100 znaków) można dojść z pola (0,0) do (9,9).
    'O' oznacza pole puste, 'X' – pole zablokowane.
    """
    # Budujemy planszę 10x10
    grid = []
    for i in range(10):
        row = []
        for j in range(10):
            # Pole (i,j) odpowiada znakowi o indeksie 10*i + j
            char = labyrinth_str[i*10 + j]
            row.append(char == 'O')
        grid.append(row)
    
    if DEBUG:
        print("[DEBUG] Wczytany labirynt:", file=sys.stderr)
        for r in grid:
            print("".join(['O' if cell else 'X' for cell in r]), file=sys.stderr)
    
    # Jeżeli wejście lub wyjście są zablokowane, nie ma szans na przejście
    if not grid[0][0] or not grid[9][9]:
        if DEBUG:
            print("[DEBUG] Wejście lub wyjście zablokowane.", file=sys.stderr)
        return False

    # BFS – przeszukiwanie wszerz, zaczynając od (0,0)
    visited = [[False] * 10 for _ in range(10)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        if DEBUG:
            print(f"[DEBUG] Odwiedzam: ({x},{y})", file=sys.stderr)
        # Sprawdzamy, czy dotarliśmy do wyjścia
        if (x, y) == (9, 9):
            return True
        # Ruchy: góra, dół, lewo, prawo
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if grid[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return False

def main():
    input_lines = sys.stdin.read().splitlines()
    results = []
    for line in input_lines:
        line = line.strip()
        if len(line) != 100:
            # Pomijamy linie, które nie opisują pełnego labiryntu.
            continue
        if can_exit(line):
            results.append("1")
        else:
            results.append("0")
    sys.stdout.write("\n".join(results))

if __name__ == '__main__':
    main()
