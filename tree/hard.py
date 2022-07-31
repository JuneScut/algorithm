
from importlib.resources import path
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 【124】 [最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)
# 测试用例 [2, -1], 任意节点，不需要一定经过到子节点，到达任意节点即可


class Solution:
    def __init__(self):
        self.maxSum = -9999

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.travel(root)
        return self.maxSum

    def travel(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftPathSum = max(0, self.travel(root.left))
        rightPathSum = max(0, self.travel(root.right))
        pathSum = leftPathSum + rightPathSum + root.val
        self.maxSum = max(pathSum, self.maxSum)
        return max(rightPathSum, leftPathSum) + root.val


solution = Solution()
print(solution.maxPathSum(
    TreeNode(-3, None, None)))
