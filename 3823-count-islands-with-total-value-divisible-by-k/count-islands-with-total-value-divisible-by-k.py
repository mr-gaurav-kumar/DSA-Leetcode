
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    stack = [(i, j)]
                    total = 0
                    grid[i][j] = -grid[i][j]

                    while stack:
                        r, c = stack.pop()
                        total += -grid[r][c]

                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc

                            if (0 <= nr < m and 0 <= nc < n
                                    and grid[nr][nc] > 0):
                                grid[nr][nc] = -grid[nr][nc]
                                stack.append((nr, nc))

                    if total % k == 0:
                        count += 1

        return count
