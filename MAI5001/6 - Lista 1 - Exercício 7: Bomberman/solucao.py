from copy import deepcopy


data = input()


def explode_bombs(grid, bombs):
    new_grid = deepcopy(grid)
    for bomb in bombs:
        i, j = bomb
        new_grid[i][j] = "."
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != "0":
                new_grid[ni][nj] = "."
    return new_grid


def plant_bombs(grid):
    bombs = []
    new_grid = deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                pass
                # bombs.append((i, j))
                # print(type(new_grid[i][j]))
                # new_grid[i][j] = "0"
    return new_grid, bombs


def bomberman(m, n, t, grid):
    bombs = []
    for i in range(m):
        grid[i] = list(grid[i])

    for sec in range(t):
        if sec == 0:
            continue
        elif sec == 1:
            grid = ["".join(row) for row in grid]
        elif sec % 2 == 0:
            grid, bombs = plant_bombs(grid)
        else:
            grid = explode_bombs(grid, bombs)

    return grid


data = data.split()

m, n, t = 0, 0, 0
grid = data

if "." not in data[0:3]:
    m = int(data[0])
    n = int(data[1])
    t = int(data[2])
    
    grid = data[3:]

result = bomberman(m, n, t, grid)

for row in result:
    print(row)