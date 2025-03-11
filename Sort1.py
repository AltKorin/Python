import sys
import math

DEBUG = True  # Ustaw na True, aby włączyć komunikaty debug

def calculate_distance(x, y):
    """Oblicza odległość euklidesową od środka układu współrzędnych."""
    return math.sqrt(x**2 + y**2)

def main():
    input_data = sys.stdin.read().strip().split('\n')
    if not input_data:
        return
    
    index = 0
    t = int(input_data[index])
    index += 1
    if DEBUG:
        print(f"[DEBUG] Liczba przypadków testowych: {t}", file=sys.stderr)
    
    output_lines = []
    
    for test_index in range(t):
        if index < len(input_data) and input_data[index] == '':
            index += 1  # Pomiń pustą linię między testami
        n = int(input_data[index])
        index += 1
        points = []
        
        for _ in range(n):
            line = input_data[index].split()
            name = line[0]
            x = int(line[1])
            y = int(line[2])
            distance = calculate_distance(x, y)
            points.append((distance, name, x, y))
            index += 1
        
        # Sortuj punkty według odległości
        points.sort()
        
        if DEBUG:
            print(f"[DEBUG] Przypadek testowy #{test_index + 1}: n = {n}", file=sys.stderr)
            for point in points:
                print(f"[DEBUG] Punkt: {point[1]} ({point[2]}, {point[3]}) - Odległość: {point[0]}", file=sys.stderr)
        
        for point in points:
            output_lines.append(f"{point[1]} {point[2]} {point[3]}")
        output_lines.append("")  # Pusta linia oddzielająca przypadki testowe
    
    # Usuń ostatnią pustą linię, jeśli istnieje.
    if output_lines and output_lines[-1] == "":
        output_lines.pop()
    
    sys.stdout.write("\n".join(output_lines) + "\n")

if __name__ == '__main__':
    main()