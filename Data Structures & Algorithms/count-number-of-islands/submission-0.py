class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        islands = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or visited[r][c] or grid[r][c] == "0":
                return
            
            visited[r][c] = True
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r,c)
                    islands += 1
        
        return islands

        