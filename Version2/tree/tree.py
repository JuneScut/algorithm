from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [94. 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/?favorite=2cktkvj)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.path = []
        self.traverse(root)
        return self.path

    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return
        self.traverse(root.left)
        self.path.append(root.val)
        self.traverse(root.right)


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        if not root:
            return path
        path.extend(self.inorderTraversal(root.left))
        path.append(root.val)
        path.extend(self.inorderTraversal(root.right))
        return path


root = TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3), right=None))
# root = None
# print(Solution().inorderTraversal(root))

# [96. 不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/?favorite=2cktkvj)
# 遍历有序数组，每个点都可能作为顶点，左右两边分别作为左右子树


class Solution:
    def numTrees(self, n: int) -> int:
        self.memo = {}
        return self.count(1, n)  # 不包括 0

    # 在下标 [low...high] 区间能组成多少种不同的二叉搜索树
    def count(self, low: int, high: int) -> int:
        # 边界
        if low > high:
            return 1
        if self.memo.get((low, high), -1) >= 0:
            return self.memo[(low, high)]
        res = 0
        # high+1, 这样才能取到 n 做顶点
        for i in range(low, high+1):
            leftCount = self.count(low, i-1)
            rightCount = self.count(i+1, high)
            res += leftCount * rightCount
        self.memo[(low, high)] = res
        return res


n = 1
# print(Solution().numTrees(n))

# [98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/?favorite=2cktkvj)
# 所有的左子树的节点都要满足小于 root, 所有的右子树的节点都要满足大于 root
# 递归


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, None, None)

    def traverse(self, root: Optional[TreeNode], min: Optional[TreeNode], max: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        left = self.traverse(root.left, min, root)
        right = self.traverse(root.right, root, max)
        return left and right


root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
# print(Solution().isValidBST(root))

# [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.traverse(root.left, root.right)

    def traverse(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if (not left and right) or (left and not right):
            return False
        if left and right and left.val != right.val:
            return False
        return self.traverse(left.left, right.right) and self.traverse(left.right, right.left)


root = TreeNode(1,
                left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
# print(Solution().isSymmetric(TreeNode(1)))

# [102. 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/?favorite=2cktkvj)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        return res


root = TreeNode(1,
                left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)))
# print(Solution().levelOrder(TreeNode(1)))

# [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/?favorite=2cktkvj)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth, rightDepth) + 1

# print(Solution().maxDepth(TreeNode(1)))

# [105. 从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/?favorite=2cktkvj)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.map = {}
        for i in range(len(inorder)):
            self.map[inorder[i]] = i
        return self.build(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def build(self, preorder: List[int], preStart: int, preEnd: int,
              inorder: List[int], inStart: int, inEnd: int):
        if preStart > preEnd or preStart >= len(preorder):
            return None
        rootVal = preorder[preStart]
        rootInIndex = self.map.get(rootVal)
        leftSize = rootInIndex - inStart
        root = TreeNode(rootVal)
        root.left = self.build(
            preorder, preStart+1, preStart+leftSize, inorder, inStart, rootInIndex-1)
        root.right = self.build(
            preorder, preStart+leftSize+1, preEnd, inorder, rootInIndex+1, inEnd)
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
# root = Solution().buildTree(preorder, inorder)
# print(root)

# [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/?favorite=2cktkvj)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 各自拉开
        self.flatten(root.left)
        self.flatten(root.right)
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        prev, next = None, left
        # 拼接右子树
        while next:
            prev = next
            next = next.right
        if prev:
            prev.right = right
        else:
            root.right = right


# root = TreeNode(1,
#                 left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
#                 right=TreeNode(5, left=None, right=TreeNode(3)))
root = TreeNode(1,
                left=None,
                right=TreeNode(5, left=None, right=TreeNode(3)))
# Solution().flatten(root)
# print(root)


# [124. 二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ret = -float('inf')

        # 计算每个节点的最大贡献和
        # 空节点的最大贡献值等于 0，
        # 非空节点的最大贡献值等于节点值与其子节点中的最大贡献值之和（对于叶节点而言，最大贡献值等于节点值）。
        def maxGain(node: Optional[TreeNode]):
            if not node:
                return 0
            # 如果子节点的最大贡献值为正，则计入该节点的最大路径和，否则不计入该节点的最大路径和
            leftMaxGain = max(maxGain(node.left), 0)
            rightMaxGain = max(maxGain(node.right), 0)
            curVal = leftMaxGain + rightMaxGain + node.val
            self.ret = max(self.ret, curVal)
            return max(leftMaxGain, rightMaxGain) + node.val

        maxGain(root)
        return self.ret


root = TreeNode(-10,
                left=TreeNode(9),
                right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
print(Solution().maxPathSum(root))
