def count_neighbors(r, c, current_grid, rows, cols):
    count = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
        
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if current_grid[nr][nc] == '@':
                count += 1
    return count

def solve():
    with open("AOC2025/input04.txt") as f:
        lines = f.readlines()

    grid = [list(line.strip()) for line in lines if line.strip()]

    rows = len(grid)
    cols = len(grid[0])

    total_removed = 0
    part1_answer = 0
    iteration = 0

    while True:
        to_remove = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    if count_neighbors(r, c, grid, rows, cols) < 4:
                        to_remove.append((r, c))
        
        if not to_remove:
            break
            
        count = len(to_remove)
        total_removed += count

        if iteration == 0:
            part1_answer = count

        for r, c in to_remove:
            grid[r][c] = '.' 
            
        iteration += 1

    print("Part 1:", part1_answer)
    print("Part 2:", total_removed)

if __name__ == "__main__":
    solve()