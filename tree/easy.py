# !/usr/bin/env python3
# coding=utf-8

# 树 - 简单

from platform import node
from tkinter.tix import Tree
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 【1】94. 二叉树的中序遍历 【https://leetcode-cn.com/problems/binary-tree-inorder-traversal/】
# Definition for a binary tree node.
# 递归版本
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         result = []

#         def traversal(root: TreeNode):
#             if root == None:
#                 return
#             else:
#                 traversal(root.left)
#                 result.append(root.val)
#                 traversal(root.right)

#         traversal(root)
#         return result

# 迭代版本, 利用栈【先进先出】，因为递归和栈都具有回溯的特性


# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         stack, ret = [], []
#         cur = root  # 栈顶元素
#         while cur or stack:
#             if cur:
#                 stack.append(cur)
#                 cur = cur.left
#             else:
#                 cur = stack.pop()
#                 ret.append(cur.val)
#                 cur = cur.right
#         return ret


# 【2】[相同的树](https://leetcode-cn.com/problems/same-tree/)
# 同遍历，可迭代或递归

# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         if p == None and q == None:
#             return True
#         if p != None and q != None and p.val == q.val:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         else:
#             return False

# 【3】（对称二叉树）[https://leetcode-cn.com/problems/symmetric-tree/]
# 递归

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def camp(node1: TreeNode, node2: TreeNode) -> bool:
#             if not node1 and not node2:
#                 return True
#             if node1 and node2 and node1.val == node2.val:
#                 return camp(node1.left, node2.right) and camp(node1.right, node2.left)
#             else:
#                 return False

#         if not root:
#             return True
#         else:
#             return camp(root.left, root.right)


# solution = Solution()
# print(solution.isSymmetric(
#     TreeNode(1,
#              TreeNode(2, None, TreeNode(4)),
#              TreeNode(2, None, TreeNode(4)))))

# 【4】[层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)
# 改为每一轮循环，都将当前层的所有节点出栈 https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         queque, ret = [], []
#         queque.append(root)
#         while queque:
#             level = []
#             size = len(queque)
#             i = 0
#             while i < size:
#                 cur = queque.pop(0)
#                 if cur:
#                     level.append(cur.val)
#                     if cur.left:
#                         queque.append(cur.left)
#                     if cur.right:
#                         queque.append(cur.right)
#                 i += 1
#             if level:
#                 ret.append(level)
#         return ret


# solution = Solution()
# print(solution.levelOrder(
#     TreeNode(3,
#              TreeNode(9, None, None),
#              TreeNode(20, TreeNode(15), TreeNode(7)))))

# 【104】[二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


solution = Solution()
print(solution.maxDepth(
    TreeNode(3,
             TreeNode(9, None, None),
             TreeNode(20, TreeNode(15), TreeNode(7)))))
