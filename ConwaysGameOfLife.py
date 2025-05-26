print("Name: Harsha D S, USN: 1AY24AI041, Sec: M")

import numpy as np
import os
import time

# Grid size
WIDTH = 20
HEIGHT = 20

# Time delay between generations (in seconds)
DELAY = 0.5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid, generation):
    clear_screen()
    print(f"Generation: {generation}")
    for row in grid:
        print(''.join(['█' if cell else ' ' for cell in row]))

def count_neighbors(grid, x, y):
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                ni = (x + i) % HEIGHT
                nj = (y + j) % WIDTH
                total += grid[ni][nj]
    return total

def next_generation(grid):
    new_grid = np.zeros((HEIGHT, WIDTH), dtype=int)
    for i in range(HEIGHT):
        for j in range(WIDTH):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1 and neighbors in [2, 3]:
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
    return new_grid

def main():
    try:
        max_generations = int(input("Enter number of generations to simulate: "))
        if max_generations <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    grid = np.random.choice([0, 1], size=(HEIGHT, WIDTH), p=[0.8, 0.2])

    for generation in range(1, max_generations + 1):
        print_grid(grid, generation)
        grid = next_generation(grid)
        time.sleep(DELAY)

    print("\nSimulation completed after", max_generations, "generations.")

if __name__ == "__main__":
    main()
