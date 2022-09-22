import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 【111】 [二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        queque = [root]
        while queque:
            n = len(queque)
            for _ in range(n):
                node = queque.pop(0)
                if not node.left and not node.right:
                    return depth
                else:
                    if node.left:
                        queque.append(node.left)
                    if node.right:
                        queque.append(node.right)

            depth += 1
        return depth


# 【752】 [打开转盘锁](https://leetcode.cn/problems/open-the-lock/)
class Solution:
    def plusUp(self, s: str, j: int):
        next = list(s)
        if s[j] == '9':
            next[j] = '0'
        else:
            next[j] = f'{int(s[j]) + 1}'
        return ''.join(next)

    def plusDown(self, s: str, j: int):
        next = list(s)
        if s[j] == '0':
            next[j] = '9'
        else:
            next[j] = str(int(s[j]) - 1)
        return ''.join(next)

    def openLock(self, deadends: List[str], target: str) -> int:
        step = 0
        q = []
        q.append('0000')
        deads = set(deadends)
        visited = set([])
        visited.add('0000')
        while q:
            n = len(q)
            for i in range(n):
                cur = q.pop(0)
                # 遍历终点
                if cur in deads:
                    continue
                if cur == target:
                    return step
                for j in range(4):
                    nextUp = self.plusUp(cur, j)
                    if not nextUp in visited:
                        q.append(nextUp)
                        visited.add(nextUp)
                    nextDown = self.plusDown(cur, j)
                    if not nextDown in visited:
                        q.append(nextDown)
                        visited.add(nextDown)
            step += 1
        return -1


# solution = Solution()
# print(solution.openLock(["0201", "0101", "0102", "1212", "2002"], '0202'))


# 【934】 [最短的桥](https://leetcode.cn/problems/shortest-bridge/)
# 1 遍历矩阵，找到的一个1，调用dfs把和1联通的所有1改成2；
# 2 调用bfs把第一个岛向周围扩散（即把它把周围的0改为2），直到在某次扩散时遇到1，说明已经遇到了另一个岛，此时返回扩散的次数即可。
# 变量说明：q双端队列，存储第一个岛； steps存储bfs的扩散的次数；dirs存储上下左右4个方向

class Solution:
    def shortestBridge(self, nums):
        def dfs(i, j):  # 把找到的一个岛染成2，同时把找个岛的所有坐标放到队列q
            if i < 0 or i >= len(nums) or j < 0 or j >= len(nums[0]) or nums[i][j] == 0 or nums[i][j] == 2:
                return
            if nums[i][j] == 1:
                nums[i][j] = 2
                q.append((i, j))
                for x, y in dirs:
                    newi, newj = x+i, y+j
                    dfs(newi, newj)

        def bfs(i, j):  # 从找到的岛开始扩展，每扩展一层，steps+1
            steps = 0
            while q:
                size = len(q)
                for _ in range(size):
                    i, j = q.popleft()
                    for x, y in dirs:
                        newi, newj = x+i, y+j
                        if newi < 0 or newi >= len(nums) or newj < 0 or newj >= len(nums[0]) or nums[newi][newj] == 2:
                            continue
                        if nums[newi][newj] == 1:
                            return steps
                        nums[newi][newj] = 2
                        q.append((newi, newj))
                steps += 1
        # main
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        q = collections.deque()
        for i, row in enumerate(nums):
            for j, ele in enumerate(row):
                if ele == 1:
                    dfs(i, j)
                    return bfs(i, j)


class Solution:
    def shortestBridge(self, nums: List[List[int]]) -> int:
        def dfs(i, j):
            # 找到岛屿
            # 边界判断
            if i < 0 or j < 0 or i >= len(nums) or j >= len(nums[0]) or nums[i][j] == 2:
                return
            if nums[i][j] == 1:
                nums[i][j] = 2
                q.append((i, j))
                for (x, y) in dirs:
                    newX, newY = i+x, j+y
                    dfs(newX, newY)

        def bfs(i, j):
            # 开始向外扩散
            step = 0
            while q:
                size = len(q)
                for _ in range(size):
                    i, j = q.popleft()
                    for (x, y) in dirs:
                        newi, newj = i+x, j+y
                        if newi < 0 or newj < 0 or newi >= len(nums) or newj >= len(nums[0]) or nums[newi][newj] == 2:
                            continue
                        if nums[newi][newj] == 1:
                            return step
                        nums[newi][newj] = 2
                        q.append((newi, newj))

                step += 1

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        q = collections.deque()
        for i, row in enumerate(nums):
            for j, ele in enumerate(row):
                if ele == 1:
                    dfs(i, j)
                    return bfs(i, j)


solution = Solution()
# print(solution.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
