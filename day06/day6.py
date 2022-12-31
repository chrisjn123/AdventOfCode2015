from collections import defaultdict
from itertools import product
from re import findall


data = [line.strip() for line in open('input.txt').readlines()]
grid = defaultdict(int)

def operation(line):
    if 'on' in line:
        return lambda x: x + 1
    elif 'off' in line:
        return lambda x: max(x - 1, 0)
    else:
        return lambda x: x + 2

for line in data:
    coords = map(int, findall(r"\d+", line))
    x1, y1, x2, y2 = coords
    xrange = range(x1, x2 + 1)
    yrange = range(y1, y2 + 1)

    oper = operation(line)
    for c in product(xrange, yrange):
        grid[c] = oper(grid[c])

print(
    sum([grid[key] for key in grid])
)
