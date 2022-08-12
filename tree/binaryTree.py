
import math
from optparse import Option
from turtle import right
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 【124】 [最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/)
# 【51】 [节点之和的最大路径](https://leetcode.cn/problems/jC7MId/submissions/)
# 测试用例 [2, -1], 任意节点，不需要一定经过到子节点，到达任意节点即可


class Solution:
    def __init__(self):
        self.maxSum = -9999

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.oneSidePathSum(root)
        return self.maxSum

    def oneSidePathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftPathSum = max(0, self.oneSidePathSum(root.left))
        rightPathSum = max(0, self.oneSidePathSum(root.right))
        pathSum = leftPathSum + rightPathSum + root.val
        self.maxSum = max(pathSum, self.maxSum)
        return max(rightPathSum, leftPathSum) + root.val


# solution = Solution()
# print(solution.maxPathSum(
#     TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))))

# 【513】 [找树左下角的值](https://leetcode.cn/problems/find-bottom-left-tree-value/?show=1)
# 考察点：🌲的深度、🌲的遍历顺序


class Solution:
    def __init__(self) -> None:
        self.maxDepth = 0
        self.depth = 0  # 当前游走的深度
        self.res = None  # 左下角节点

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.travel(root)
        return self.res.val

    def travel(self, root: Optional[TreeNode]):
        if not root:
            return
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
            self.res = root
        # 先左边再右边，这样当上边的条件判断进入时总是左边的节点
        self.travel(root.left)
        self.travel(root.right)
        self.depth -= 1


# solution = Solution()
# print(solution.findBottomLeftValue(
#     TreeNode(1,
#              TreeNode(2, TreeNode(4, None, None), None),
#              TreeNode(3, TreeNode(5, TreeNode(7, None, None), None),
#                       TreeNode(6, None, None))
#              )
# ))


# 【508】 [出现次数最多的子树元素和](https://leetcode.cn/problems/most-frequent-subtree-sum/)
# 既然找最大，就用 map 存储

class Solution:
    def __init__(self) -> None:
        self.valueMap = {}

    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.calculateTreeSum(root)
        max_value = max(self.valueMap.values())
        max_key = []
        for key, value in self.valueMap.items():
            if value == max_value:
                max_key.append(key)
        return max_key

    def calculateTreeSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftSum = self.calculateTreeSum(root.left)
        rightSum = self.calculateTreeSum(root.right)
        treeSum = leftSum + rightSum + root.val
        if treeSum in self.valueMap:
            self.valueMap[treeSum] += 1
        else:
            self.valueMap[treeSum] = 1
        return treeSum


# solution = Solution()
# print(solution.findFrequentTreeSum(
#     TreeNode(5, TreeNode(2, None, None), TreeNode(-5, None, None))))


# 【36】 [二叉搜索树和双向链表](https://leetcode.cn/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/?show=1)
# 二叉树节点数据结果和双向链表一致
# 二叉搜索树：双向遍历
# BST
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # 各自将左右子树组成双向链表, 左子树的根节点的左节点才是左子树的尾巴
        leftHead = self.treeToDoublyList(root.left)
        rightHead = self.treeToDoublyList(root.right)
        leftTail, rightTail = None, None

        # 将左右子树和中间节点拼接成双向链表，左右对称
        if leftHead:
            leftTail = leftHead.left
            root.left = leftTail
            leftTail.right = root
        else:
            leftTail = leftHead = root

        if rightHead:
            rightTail = rightHead.left
            root.right = rightHead
            rightHead.left = root
        else:
            rightTail = rightHead = root

        leftHead.left = rightTail
        rightTail.right = leftHead

        return leftHead


# solution = Solution()
# print(solution.treeToDoublyList(
#     TreeNode(4, TreeNode(2, TreeNode(1, None, None),
#              TreeNode(3, None, None)), TreeNode(5, None, None))
# ).right.right.val)


# 【856】 [具有所有最深节点的最小子树](https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/?show=1)
# 最深节点只有一个，则返回最深节点
# 最深节点有多个，则返回他们的最小共同父节点
# [遍历思想]

class Solution:
    class Result:
        def __init__(self, node: TreeNode, depth: int) -> None:
            self.node = node
            self.depth = depth

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        res = self.maxDepth(root)
        return res.node

    def maxDepth(self, root: TreeNode) -> Result:
        if not root:
            return self.Result(None, 0)

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left.depth == right.depth:
            res = self.Result(root, left.depth)
        else:
            res = left if left.depth > right.depth else right

        res.depth += 1

        return res


# solution = Solution()
# print(solution.subtreeWithAllDeepest(TreeNode(0,
#                                               TreeNode(1, None, TreeNode(2, None, None)), TreeNode(3, None, None))).val)

# 【543】 [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/)
class Solution:
    def __init__(self) -> None:
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.travel(root)
        return self.diameter

    def travel(self, root: Optional[TreeNode]):
        if not root:
            return 0
        else:
            left = self.travel(root.left)
            right = self.travel(root.right)
            value = left + right
            self.diameter = max(self.diameter, value)
            return 1 + max(right, left)


# solution = Solution()
# print(solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(
#     4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))))

# 【剑指offer55】 [二叉树的深度](https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# solution = Solution()
# print(solution.maxDepth(TreeNode(3, TreeNode(9, None, None),
#       TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))))

# 【116】 [填充每个节点的下一个右侧节点指针](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)
# 不同子树的相邻节点的 next 指针应该如何指？ ---> 三叉树

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        self.travel(root.left, root.right)
        return root

    def travel(self, node1: 'Optional[Node]',  node2: 'Optional[Node]'):
        if not node1 or not node2:
            return

        node1.next = node2
        # 各自子树串
        self.travel(node1.left, node1.right)
        self.travel(node2.left, node2.right)
        # 相邻子树
        self.travel(node1.right, node2.left)


# 【114】 [二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # 先把左右子树各自拉平
        self.flatten(root.left)
        self.flatten(root.right)

        # 将左子树作为右子树
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        # 把原有的右子树连到新的右子树上
        p = root
        while p.right:
            p = p.right
        p.right = right


# 【27】 [二叉树的镜像](https://leetcode.cn/problems/er-cha-shu-de-jing-xiang-lcof/)
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = self.mirrorTree(root.left)
        right = self.mirrorTree(root.right)
        root.left = right
        root.right = left
        return root

# 【剑指offer 26】 [树的子结构](https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/)


class Solution:
    # 遍历思维，A和B完全相同、A的左子树和B相同、A的右子树和B相同
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A or not B:
            return False
        if A.val == B.val and self.comapare(A, B):
            return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    # 分解思维，两颗🌲相等：当根节点值相同且左右子树也相同
    def comapare(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return True
        if not A and B:
            return False
        if A.val != B.val:
            return False
        return self.comapare(A.left, B.left) and self.comapare(A.right, B.right)

# 【654】 [最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/)


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums)-1)

    def build(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        # base case
        if left > right:
            return None
        # 找出最大值和对应下标
        maxVal, maxIndex = -9999, -1
        for i in range(left, right+1, 1):
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxIndex = i
        # 构建🌲
        root = TreeNode(maxVal)
        root.left = self.build(nums, left, maxIndex-1)
        root.right = self.build(nums, maxIndex+1, right)
        return root


# solution = Solution()
# print(solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]).val)

# 【105】 [从前序和中序遍历中构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
# https://labuladong.github.io/algo/images/%e4%ba%8c%e5%8f%89%e6%a0%91%e7%b3%bb%e5%88%972/6.jpeg

class Solution:
    def __init__(self) -> None:
        self.map = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(0, len(inorder)):
            self.map[inorder[i]] = i
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def build(self, preorder: List[int], preStart: int, preEnd: int, inorder: List[int], inStart: int, inEnd: int) -> Optional[TreeNode]:
        # base case
        if preStart > preEnd:
            return None
        # root 是 preorder 的第一个结点
        root = TreeNode(preorder[preStart])
        # 划分出 inorder 左右子树
        index = self.map.get(preorder[preStart])
        leftSize = index - inStart
        root.left = self.build(preorder, preStart+1, preStart+leftSize,
                               inorder, inStart, index-1)
        root.right = self.build(preorder, preStart+leftSize+1, preEnd,
                                inorder, index+1, inEnd)
        return root


# solution = Solution()
# print(solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).val)

# 【889】 [](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)
class Solution:
    def __init__(self) -> None:
        self.postMap = {}

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        for i in range(0, len(postorder)):
            self.postMap[postorder[i]] = i
        root = self.build(preorder, 0, len(preorder)-1,
                          postorder, 0, len(postorder)-1)
        return root

    def build(self, preorder: List[int], preStart: int, preEnd: int, postorder: List[int], postStart, postEnd) -> Optional[TreeNode]:
        # base case
        if preStart > preEnd:
            return None
        # root
        rootVal = preorder[preStart]
        root = TreeNode(rootVal)
        if preStart + 1 > preEnd:
            return root
        # 左子树的根节点
        leftRootVal = preorder[preStart+1]
        index = self.postMap.get(leftRootVal)
        leftSize = index - postStart + 1
        root.left = self.build(preorder, preStart+1,
                               preStart+leftSize, postorder, postStart, index)
        root.right = self.build(
            preorder, preStart+leftSize+1, preEnd, postorder, index+1, postEnd - 1)
        return root


# solution = Solution()
# print(solution.constructFromPrePost(
#     [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]).val)


# 【1008】 [前序遍历构建二叉搜索树](https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/)
# BST
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.build(preorder, 0, len(preorder)-1)

    def build(self, preorder: List[int], start: int, end: int) -> Optional[TreeNode]:
        if start > end:
            return None
        rootVal = preorder[start]
        root = TreeNode(rootVal)
        p = start + 1
        while p <= end and preorder[p] < rootVal:
            p += 1
        root.left = self.build(preorder, start+1, p-1)
        root.right = self.build(preorder, p, end)
        return root


# solution = Solution()
# print(solution.bstFromPreorder([8, 5, 1, 7, 10, 12]).val)

# 【297】 [二叉树的序列化和反序列化](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/)
class Codec:

    def __init__(self) -> None:
        self.sb = ''
        self.NULL = '#'
        self.SEP = ','

    def serialize(self, root: Optional[TreeNode]):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            self.sb += self.NULL
            self.sb += self.SEP
            return self.sb
        self.sb += f'{root.val}'
        self.sb += self.SEP
        self.serialize(root.left)
        self.serialize(root.right)
        return self.sb

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(self.SEP)
        return self.deserializeTool(nodes)

    def deserializeTool(self, nodes: list) -> Optional[TreeNode]:
        if not nodes or len(nodes) == 0:
            return None
        first = nodes.pop(0)
        if first == self.NULL or not first:
            return None
        root = TreeNode(int(first))
        root.left = self.deserializeTool(nodes)
        root.right = self.deserializeTool(nodes)
        return root


# solution = Codec()
# val = solution.serialize(root=TreeNode(1, TreeNode(2, None, None), TreeNode(
#     3, TreeNode(4, None, None), TreeNode(5, None, None))))
# print(val)
# root = solution.deserialize(val)
# print(root.val)


# 【652】 [寻找重复的子树](https://leetcode.cn/problems/find-duplicate-subtrees/)
class Solution:
    def __init__(self) -> None:
        self.memo = {}
        self.res = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.travel(root)
        return self.res

    def travel(self, root: Optional[TreeNode]) -> str:
        if not root:
            return '#'
        left = self.travel(root.left)
        right = self.travel(root.right)
        data = f'{left},{right},{root.val}'
        val = self.memo.get(data, 0)
        if val == 1:
            self.res.append(root)
        self.memo[data] = val + 1
        return data


# solution = Solution()
# print(solution.findDuplicateSubtrees(
#     TreeNode(2, TreeNode(1, None, None), TreeNode(1, None, None)))[0].val)

# 【315】 [计算右侧小于当前元素的个数](https://leetcode.cn/problems/count-of-smaller-numbers-after-self/)
# 利用归并排序，两边都是有序数组的特性
class Solution:
    class Pair:
        def __init__(self, val: int, index: int) -> None:
            self.val = val
            self.index = index

    def __init__(self) -> None:
        # 记录元素原始的索引位置
        self.temp = []
        # 记录每个元素后面比自己小的元素个数
        self.count = []

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append(self.Pair(nums[i], i))
        self.temp = [None] * n
        self.count = [0] * n
        self.sort(arr, 0, n-1)
        return self.count

    def sort(self, nums: List[Pair], low: int, high: int):
        if low == high:
            return
        mid = int(low + (high - low)/2)
        self.sort(nums, low, mid)
        self.sort(nums, mid+1, high)
        self.merge(nums, low, mid, high)

    # 合并两个有序数组
    def merge(self, arr: List[Pair], low: int, mid: int, high: int):
        for i in range(low, high+1, 1):
            self.temp[i] = arr[i]
        i, j = low, mid+1
        for p in range(low, high+1, 1):
            if i == mid + 1:
                arr[p] = self.temp[j]
                j += 1
            elif j == high + 1:
                arr[p] = self.temp[i]
                i += 1
                # 更新 count 数组
                self.count[arr[p].index] += j - mid - 1
            elif self.temp[i].val > self.temp[j].val:
                arr[p] = self.temp[j]
                j += 1
            else:
                arr[p] = self.temp[i]
                i += 1
                # 更新 count 数组
                self.count[arr[p].index] += j - mid - 1


# solution = Solution()
# print(solution.countSmaller([-1, -1]))

# 【235】 [二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)
# 剑指offer68
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val > q.val:
            return self.lowestCommonAncestor(root, q, p)
        if p.val <= root.val and q.val >= root.val:
            return root
        if p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val >= root.val and q.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)


# 【236】 [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)
# #难理解
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 情况 1 如果 p 和 q 都在以 root 为根的树中，那么 left 和 right 一定分别是 p 和 q（从 base case 看出来的）。
        if left and right:
            return root

        # 情况 2，如果 p 和 q 都不在以 root 为根的树中，直接返回 null。
        if not left and not right:
            return None

        # 情况 3，如果 p 和 q 只有一个存在于 root 为根的树中，函数返回该节点。
        return right if not left else left


p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q = TreeNode(1, TreeNode(0), TreeNode(8))
z = TreeNode(0)
root = TreeNode(3, p, q)
solution = Solution()
print(solution.lowestCommonAncestor(root, p, z).val)
