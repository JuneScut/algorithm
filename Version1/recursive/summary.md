二维回溯， 可以类比二叉树的深度遍历
典型题型 79 单词搜索 200 海岛数量 130 被围绕的区域

```python
def inArea(grid, r, c):
    return 0 <= r and r < len(grid) and 0 <= c and c < len(grid[0]) if len(grid) > 0 else False

def dfs(grid, r, c):
    if inArea(grid, r, c) == False :
        return
    if grid[r][c] != '1':
        return
    grid[r][c] = '2'
    dfs(grid, r+1, c)
    dfs(grid, r, c+1)
    dfs(grid, r-1, c)
    dfs(grid, r, c-1)
```

深度遍历的开始条件根据题目决定
