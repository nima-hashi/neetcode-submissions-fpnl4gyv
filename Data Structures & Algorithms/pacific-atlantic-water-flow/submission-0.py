def dfs(matrix, visited, r, c, prev_height):
        if ( r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0]) or (r, c) in visited or matrix[r][c] < prev_height):
            return

        visited.add((r, c))  # Mark current cell as visited

        # Explore all four directions
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(matrix, visited, r + dr, c + dc, matrix[r][c])

class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        for c in range(cols):
            dfs(heights, pac, 0, c, heights[0][c])
            dfs(heights, atl, rows-1, c, heights[rows-1][c])

        for r in range(rows):
             dfs(heights, pac, r, 0, heights[r][0])
             dfs(heights, atl, r, cols-1, heights[r][cols-1])
        
        res = list(pac & atl)
        return res



        