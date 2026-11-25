n = int(input() or 5)

grid = [[-1]*n for _ in range(n)]

colSet = [set() for _ in range(n)]

for y in range(n):
    possibles = [*sorted(set(range(0,2*n)))]
    for x in range(n):
        for p in possibles:
            if p in colSet[x]:
                continue
            grid[y][x] = p
            colSet[x].add(p)
            possibles.remove(p)
            break

for row in grid:
    print(*row)