# 【230】 [二叉搜索树中第k小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/)
#  #BST
from itertools import count
from turtle import left
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.rank = 0
        self.res = -9999

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.travel(root, k)
        return self.res

    def travel(self, root: Optional[TreeNode], k: int):
        if not root:
            return
        self.travel(root.left, k)
        self.rank += 1
        if self.rank == k:
            self.res = root.val
            return
        self.travel(root.right, k)


# solution = Solution()
# print(solution.kthSmallest(
#     TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1))

# 【1038】 [从二叉搜索树到更大和树](https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/)
# 降序遍历即可
class Solution:
    def __init__(self) -> None:
        self.sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.travel(root)
        return root

    def travel(self, root: TreeNode):
        if not root:
            return
        self.travel(root.right)
        self.sum += root.val
        root.val = self.sum
        self.travel(root.left)


# solution = Solution()
# print(solution.bstToGst(
#     TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))).val)

# 【98】 [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/)
# 增加参数列表，通过递归参数把限制传递给节点

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.travel(root, None, None)

    def travel(self, root: Optional[TreeNode], min: Optional[TreeNode], max: Optional[TreeNode]):
        if not root:
            return True
        if min and min.val >= root.val:
            return False
        if max and max.val <= root.val:
            return False
        return self.travel(root.left, min, root) and self.travel(root.right, root, max)


# solution = Solution()
# print(solution.isValidBST(
#     TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))))


# 【700】 [二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/)
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if val == root.val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

# 【450】 [删除二叉搜索树中的节点](https://leetcode.cn/problems/delete-node-in-a-bst/)
# 基本操作：增【删】改查


class Solution:
    def getMin(self, node):
        while node.left:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 删除右子树的最小节点
            minNode = self.getMin(root.right)
            root.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            minNode.right = root.right
            # 替代 root
            root = minNode

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root


# solution = Solution()
# print(solution.deleteNode(
#     TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 3).val)

# 【95】 [不同的二叉搜索树II](https://leetcode.cn/problems/unique-binary-search-trees-ii/)
# build 函数：传入数组左右边界，返回不同的子树数组
# 递归调用，穷举不同 root 节点的所有可能，再分别获得不同的左右子树，再组合起来

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.build(1, n)

    def build(self, low: int, high: int) -> List[Optional[TreeNode]]:
        res = []
        if low > high:
            res.append(None)
            return res
        for i in range(low, high+1, 1):
            leftTree = self.build(low, i-1)
            rightTree = self.build(i+1, high)
            for left in leftTree:
                for right in rightTree:
                    root = TreeNode(i, left, right)
                    res.append(root)
        return res


# solution = Solution()
# print(solution.generateTrees(3))


# 【96】 [不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/)
# 这里不需要返回树的结构了，所以一层循环就行
class Solution:
    def __init__(self) -> None:
        self.memo = []

    def numTrees(self, n: int) -> int:
        self.memo = [[0]*(n+1) for _ in range(n + 1)]
        return self.count(1, n)

    def count(self, low: int, high: int) -> int:
        if low > high:
            return 1
        if self.memo[low][high] != 0:
            return self.memo[low][high]

        res = 0
        for i in range(low, high+1, 1):
            leftCount = self.count(low, i-1)
            rightCount = self.count(i+1, high)
            res += leftCount * rightCount
        self.memo[low][high] = res
        return res


# solution = Solution()
# print(solution.numTrees(1))

# 【669】[修剪二叉搜索树](https://leetcode.cn/problems/trim-a-binary-search-tree/)
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
