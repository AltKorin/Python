import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
    # Rozmiar planszy – możesz zmienić tę wartość, by uzyskać większy lub mniejszy obszar symulacji.
    n = 50
    # Losowa inicjalizacja planszy: 20% szans na komórkę żywą (1) i 80% na martwą (0)
    grid = np.random.choice([0, 1], size=(n, n), p=[0.8, 0.2])
    
    fig, ax = plt.subplots()
    # Wyświetlamy planszę – cmap='gray' pokazuje żywe komórki jako ciemne, martwe jako jasne.
    img = ax.imshow(grid, interpolation='nearest', cmap='gray')
    ax.set_title("Game of Life - Zamknij okno, aby zakończyć")
    
    def update(frameNum):
        nonlocal grid
        # Liczymy sąsiadów przy użyciu zawijania krawędzi:
        neighbors = (
            np.roll(grid, 1, axis=0) + np.roll(grid, -1, axis=0) +
            np.roll(grid, 1, axis=1) + np.roll(grid, -1, axis=1) +
            np.roll(np.roll(grid, 1, axis=0), 1, axis=1) +
            np.roll(np.roll(grid, 1, axis=0), -1, axis=1) +
            np.roll(np.roll(grid, -1, axis=0), 1, axis=1) +
            np.roll(np.roll(grid, -1, axis=0), -1, axis=1)
        )
        # Zasady gry:
        # 1. Żywa komórka przeżywa, jeśli ma 2 lub 3 sąsiadów.
        # 2. Martwa komórka ożywa, jeśli ma dokładnie 3 sąsiadów.
        new_grid = np.where((grid == 1) & ((neighbors == 2) | (neighbors == 3)), 1, 0)
        new_grid = np.where((grid == 0) & (neighbors == 3), 1, new_grid)
        grid = new_grid
        img.set_data(grid)
        return img,
    
    # Ustawiamy animację – co 200 ms wywoływana jest funkcja update.
    ani = animation.FuncAnimation(fig, update, interval=200, blit=True)
    plt.show()

if __name__ == '__main__':
    main()
