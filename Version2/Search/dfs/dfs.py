from typing import List

# [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # 遍历该点的四周，修改岛屿状态

        def dfs(x: int, y: int):
            # 边界判断
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if grid[x][y] == "0" or grid[x][y] == "2":
                return
            grid[x][y] = "2"
            for (addX, addY) in dirs:
                newX, newY = addX + x, addY + y
                dfs(newX, newY)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count


grid = grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

# print(Solution().numIslands(grid))
