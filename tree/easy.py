# !/usr/bin/env python3
# coding=utf-8

# 树 - 简单
from curses.ascii import NUL
import heapq
import math
from os import path
from pickle import NONE
from platform import node
from tkinter import NS
from typing import List, Optional


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
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         else:
#             return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# solution = Solution()
# print(solution.maxDepth(
#     TreeNode(3,
#              TreeNode(9, None, None),
#              TreeNode(20, TreeNode(15), TreeNode(7)))))


# 【108】[将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)
# 这种区间分治类的题目，用左闭右闭就好，左闭右开不方便。
# 另外需要注意的是，求中点不要用 int mid = (l + r)/2，有溢出风险，稳妥的方法是 int mid = l + (r-l)/2。
# class Solution:
#     def sortedBoundedArrayToBST(self, nums, left, right):
#         if left > right:
#             return None
#         mid = int(left + (right - left) / 2)
#         root = TreeNode(nums[mid])
#         root.left = self.sortedBoundedArrayToBST(nums, left, mid - 1)
#         root.right = self.sortedBoundedArrayToBST(nums, mid + 1, right)
#         return root

#     def sortedArrayToBST(self, nums):
#         return self.sortedBoundedArrayToBST(nums, 0, len(nums) - 1)


# solution = Solution()
# print(solution.sortedArrayToBST([-10, -3, 0, 5, 9]))

# 【215】[数组中的第k个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)


# class Solution:
#     # 依次下沉
#     def downAdjust(self, nums: List[int], pIndex: int, length: int):
#         childIndex = 2 * pIndex + 1  # 左子节点
#         temp = nums[pIndex]
#         while childIndex < length:
#             if childIndex + 1 < length and nums[childIndex] < nums[childIndex + 1]:
#                 childIndex += 1  # 如果右子节点比较大，定位到右子节点
#             if (temp > nums[childIndex]):
#                 break
#             nums[pIndex] = nums[childIndex]
#             pIndex = childIndex
#             childIndex = 2 * childIndex + 1
#         nums[pIndex] = temp

#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         maxLength = len(nums)
#         if k > maxLength:
#             return None
#         # 调整成最大堆
#         idx = math.ceil((len(nums)-2) / 2)
#         while idx >= 0:
#             self.downAdjust(nums, idx, len(nums))
#             idx -= 1
#         # 删除节点
#         max = nums[0]
#         idx = 1
#         while idx <= k:
#             max = nums[0]
#             nums[0] = nums[maxLength - idx]
#             nums[maxLength - idx] = max
#             self.downAdjust(nums, 0, maxLength - idx)
#             idx += 1
#         return max


# solution = Solution()
# print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))


# 【703】[数据流中的第 k 大元素]（https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/）
# python 的最小堆实现 heapq
# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.pool = nums
#         self.k = k
#         heapq.heapify(self.pool)
#         while len(self.pool) > k:
#             heapq.heappop(self.pool)

#     def add(self, val: int) -> int:
#         if len(self.pool) < self.k:
#             heapq.heappush(self.pool, val)
#         elif val > self.pool[0]:
#             heapq.heapreplace(self.pool, val)
#         return self.pool[0]


# obj = KthLargest(3, [4, 5, 8, 2])
# print(obj.pool)
# param_1 = obj.add(3)
# print(param_1, obj.pool)
# param_1 = obj.add(5)
# print(param_1, obj.pool)
# param_1 = obj.add(10)
# print(param_1, obj.pool)
# param_1 = obj.add(9)
# print(param_1, obj.pool)
# param_1 = obj.add(4)
# print(param_1, obj.pool)

# [110] [平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)
# class Solution:
#     def getTreeHeight(self, root: TreeNode) -> int:
#         if root == None:
#             return 0
#         if root.left == None and root.right == None:
#             return 1
#         return 1 + max(self.getTreeHeight(root.left), self.getTreeHeight(root.right))

#     def isBalanced1(self, root: TreeNode) -> bool:
#         if root == None:
#             return True
#         lHeight, rHeight = self.getTreeHeight(
#             root.left), self.getTreeHeight(root.right)
#         if abs(lHeight-rHeight) > 1:
#             return False
#         return self.isBalanced1(root.left) and self.isBalanced1(root.right)

#     # 解决方法2：自底向上递归
#     def height(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         left, right = self.height(root.left), self.height(root.right)
#         if left == -1 or right == -1 or abs(left - right) > 1:
#             return -1
#         return 1 + max(right, left)

#     def isBalanced(self, root: TreeNode) -> bool:
#         return self.height(root) >= 0


# solution = Solution()
# print(solution.isBalanced(
#     TreeNode(1,
#              TreeNode(2,
#                       TreeNode(3, TreeNode(4), TreeNode(4)),
#                       TreeNode(3)),
#              TreeNode(2),
#              )
# ))

# [111] [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         queue = [root]
#         level = 1
#         while queue:
#             size = len(queue)
#             idx = 0
#             while idx < size:
#                 node = queue.pop(0)
#                 if not node.left and not node.right:
#                     # 找到叶子节点
#                     return level
#                 else:
#                     if node.left:
#                         queue.append(node.left)
#                     if node.right:
#                         queue.append(node.right)
#                 idx += 1
#             level += 1
#         return level


# solution = Solution()
# print(solution.minDepth(
#     TreeNode(1,
#              TreeNode(2,
#                       TreeNode(4),
#                       TreeNode(5)),
#              TreeNode(3),
#              )
# ))


# [112] [路径总和](https://leetcode-cn.com/problems/path-sum/)
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#         nodeQueue, sumQueue = [], []
#         nodeQueue.append(root)
#         sumQueue.append(root.val)
#         while len(nodeQueue) > 0:
#             cur = nodeQueue.pop()
#             curSum = sumQueue.pop()
#             if cur.left:
#                 nodeQueue.append(cur.left)
#                 sumQueue.append(curSum + cur.left.val)
#             if cur.right:
#                 nodeQueue.append(cur.right)
#                 sumQueue.append(curSum + cur.right.val)
#             if not cur.left and not cur.right:
#                 if curSum == targetSum:
#                     return True
#         return False

#     #  路径总和 II

#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         path = list()
#         result = list()

#         def dfs(root: Optional[TreeNode], targetSum: int):
#             if not root:
#                 return
#             path.append(root.val)
#             targetSum -= root.val
#             if not root.left and not root.right and targetSum == 0:
#                 result.append(path[:])
#             dfs(root.left, targetSum)
#             dfs(root.right, targetSum)
#             path.pop()
#         dfs(root, targetSum)
#         return result


# solution = Solution()
# print(solution.pathSum(
#     TreeNode(5,
#              TreeNode(4,
#                       TreeNode(11,
#                                TreeNode(7),
#                                TreeNode(2)),
#                       None),
#              TreeNode(8,
#                       TreeNode(13),
#                       TreeNode(4,
#                                TreeNode(5),
#                                TreeNode(1)))
#              ),
#     22
# ))

# 【144】[前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         result = []
#         result.append(root.val)
#         result.extend(self.preorderTraversal(root.left))
#         result.extend(self.preorderTraversal(root.right))
#         return result


# 【145】[后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         result = []
#         result.extend(self.postorderTraversal(root.left))
#         result.extend(self.postorderTraversal(root.right))
#         result.append(root.val)
#         return result


# solution = Solution()
# print(solution.postorderTraversal(
#     TreeNode(1,
#              TreeNode(2,
#                       TreeNode(4),
#                       TreeNode(5)),
#              TreeNode(3),
#              )
# ))

# 【226】[翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return root
#         temp = root.left
#         root.left = self.invertTree(root.right)
#         root.right = self.invertTree(temp)
#         return root


# solution = Solution()
# print(solution.invertTree(
#     TreeNode(1,
#              TreeNode(2,
#                       TreeNode(1),
#                       TreeNode(3)),
#              TreeNode(7,
#                       TreeNode(6),
#                       TreeNode(9)),
#              )
# ))


# 【235】[二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
# 📌 一次遍历, 节约路径比较和存储
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root:
#             return None
#         if not p:
#             return q
#         if not q:
#             return p
#         cur = root
#         while cur.val != p.left or cur.val != q.val:
#             if p.val < cur.val and q.val < cur.val:
#                 cur = cur.left
#             elif p.val > cur.val and q.val > cur.val:
#                 cur = cur.right
#             else:
#                 return cur


# solution = Solution()
# p = solution.lowestCommonAncestor(
#     TreeNode(6,
#              TreeNode(2,
#                       TreeNode(0),
#                       TreeNode(4,
#                                TreeNode(3),
#                                TreeNode(5))),
#              TreeNode(8,
#                       TreeNode(7),
#                       TreeNode(9)),
#              ), TreeNode(3), TreeNode(9))
# if p:
#     print(p.val)


# 【257】[二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/)
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        result = []
        path = ''

        def travelTreeNode(root: Optional[TreeNode], path: str):
            if not root:
                return
            if not root.left and not root.right:
                path = path + '->' + \
                    str(root.val) if path != '' else str(root.val)
                result.append(path)
            else:
                path = path + '->' + \
                    str(root.val) if path != '' else str(root.val)
                travelTreeNode(root.left, path)
                travelTreeNode(root.right, path)

        travelTreeNode(root, path)
        return result


solution = Solution()
print(solution.binaryTreePaths(
    TreeNode(1,
             TreeNode(2,
                      None,
                      TreeNode(5)),
             TreeNode(3)))
      )
