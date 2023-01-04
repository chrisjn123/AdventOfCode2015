from collections import defaultdict
data = open('input.txt').readlines()

grid = set()

for j, line in enumerate(data):
    for i, ch in enumerate(line):
        if ch == '#':
            grid.add((i, j))

grid.add((0, 0))
grid.add((0, 99))
grid.add((99, 0))
grid.add((99, 99))

for rnd in range(100):
    next_grid = set()
    for x in range(100):
        for y in range(100): 
            light = (x, y)
            count = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (i, j) == (0, 0):
                        continue

                    if (light[0] + i, light[1] + j) in grid:
                        count += 1
        
            if light in grid and count in [2, 3]:
                next_grid.add(light)
            elif light not in grid and count == 3:
                next_grid.add(light)
        
    grid = next_grid
    grid.add((0, 0))
    grid.add((0, 99))
    grid.add((99, 0))
    grid.add((99, 99))


print(len(grid))
