def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    return count

rows = int(input("Enter number of rows: "))
grid = [list(input("Enter row {}: ".format(i+1))) for i in range(rows)]
print("Number of Islands:", numIslands(grid))

##Given a 2D grid where:

# '1' represents land.
# '0' represents water.
# Find the number of islands (connected groups of 1s).
