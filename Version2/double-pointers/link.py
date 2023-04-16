# coding=utf-8
import heapq
from typing import List, Optional

# 双链表
# 1. K 个链表 K 个指针
# 2. 一个链表，同个方向，两个指针先后去遍历
# 3. 一个链表，同个方向，两个指针不同速度去遍历


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p1 = list1
        p2 = list2
        p = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            elif p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        if p2:
            p.next = p2
        return dummy.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
# print(Solution().mergeTwoLists(list1, list2))


# [86. 分隔链表](https://leetcode.cn/problems/partition-list/)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1, p2 = dummy1, dummy2
        p = head
        while p:
            if (p.val >= x):
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            # 断开 p 和下一个节点的联系
            tmp = p.next
            p.next = None
            p = tmp
        p1.next = dummy2.next
        return dummy1.next


list = ListNode(1, ListNode(4, ListNode(
    3, ListNode(2, ListNode(5, ListNode(2))))))
# Solution().partition(list, 3)

# [23. 合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/)
# 🐻 N 个链表中取最小值 => 最小堆/优先队列
# ☘ Python 的 heapq 不支持传入比较器
# ☘ Trick: 利用二元组，传入下标定位是哪个链表


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy
        priorityList = []
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(priorityList, (node.val, index))
        while len(priorityList) > 0:
            (_, index) = heapq.heappop(priorityList)
            cur = lists[index]
            if cur:
                p.next = cur
                p = p.next
                if cur.next:
                    lists[index] = lists[index].next
                    heapq.heappush(priorityList, (lists[index].val, index))
        return dummy.next


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
# print(Solution().mergeKLists([[]]))


# [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        former = head
        dummy = ListNode(-1)
        dummy.next = head
        later = dummy
        for _ in range(n):
            former = former.next
        while former:
            former = former.next
            later = later.next
        temp = later.next
        if later and temp:
            later.next = temp.next
        return dummy.next


list1 = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6))))))
list2 = ListNode(1)
# Solution().removeNthFromEnd(None, 0)

# [876. 链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
# print(Solution().middleNode(list2).val)

# [剑指 Offer II 022. 链表中环的入口节点](https://leetcode.cn/problems/c32eOV/)


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 相遇点
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        # 无环
        if not fast or not fast.next:
            return None
        # 再同时走 k-m 步，会在入口节点再次相遇
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node4
# print(Solution().detectCycle(node1).val)

# [160. 相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1

# [剑指 Offer II 061. 和最小的 k 个数对](https://leetcode.cn/problems/qn8gGX/?show=1)


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        priorityList = []
        for (j, value) in enumerate(nums2):
            heapq.heappush(priorityList, (nums1[0]+value, nums1[0], value))
        res = []
        enumNums1Idx = 0
        while priorityList and k:
            minValTuple = heapq.heappop(priorityList)
            k -= 1
            (_, val1, val2) = minValTuple
            res.append([val1, val2])
            nextIdx = enumNums1Idx + 1
            if nextIdx < len(nums1):
                for (j, value) in enumerate(nums2):
                    heapq.heappush(
                        priorityList, (nums1[nextIdx]+value, nums1[nextIdx], value))
                enumNums1Idx += 1
        return res


nums1 = [1, 2]
nums2 = [3]
# print(Solution().kSmallestPairs(nums1, nums2, 3))

# [剑指 Offer II 078. 合并排序链表](https://leetcode.cn/problems/vvXgSW/?show=1)


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(-1)
        priorityList = []
        for (idx, node) in enumerate(lists):
            if node:
                heapq.heappush(priorityList, (node.val, idx, node))
        p = dummy
        while priorityList:
            (minVal, idx, cur) = heapq.heappop(priorityList)
            p.next = ListNode(minVal)
            p = p.next
            cur = cur.next
            if cur:
                heapq.heappush(priorityList, (cur.val, idx, cur))
        return dummy.next


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
# print(Solution().mergeKLists([[]]))

# [剑指 Offer 24. 反转链表](https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/?show=1)
# 🌻 递归思路


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)  # 返回新链表的起点
        head.next.next = head
        head.next = None
        return last


list = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6))))))
# Solution().reverseList(list)

# [剑指 Offer II 024. 反转链表](https://leetcode.cn/problems/UHnkqh/)
# 🌻 迭代思路
# 借助 prev 和 cur 指针，next 只在循环内使用，记录下一个节点而已


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
# Solution().reverseList(list)

# 反转链表前 N 个节点
# https://labuladong.github.io/algo/images/%e5%8f%8d%e8%bd%ac%e9%93%be%e8%a1%a8/6.jpg


class Solution:
    successor = None

    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n < 1:
            return head
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last

# Solution().reverseN(list, 1)

# [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/)


class Solution:
    successor = None

    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reverseN(head, right)

        if left > 1:
            # right 也需要 -1，从个数来看，这样才能保证反转的节点个数一致
            head.next = self.reverseBetween(head.next, left-1, right-1)
            # 同样都是返回新链表的起点
            return head

# Solution().reverseBetween(list, 2, 4)


# [109. 有序链表转换二叉搜索树](https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/?show=1)
# 递归， 利用快慢指针找到中点
class Solution:
    def getMedian(self, left: ListNode, right: ListNode) -> Optional[ListNode]:
        slow, fast = left, left
        while fast and fast != right and fast.next and fast.next != right:
            fast = fast.next.next
            slow = slow.next
        return slow

    def buildBST(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[TreeNode]:
        if left == right:
            return None
        mid = self.getMedian(left, right)
        root = TreeNode(mid.val)
        root.left = self.buildBST(left, mid)
        root.right = self.buildBST(mid.next, right)
        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.buildBST(head, None)


list = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
# Solution().sortedListToBST(list)


# [剑指 Offer II 027. 回文链表](https://leetcode.cn/problems/aMhZSa/)
class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if head and head.next:
            last = self.reverse(head.next)
            head.next.next = head
            head.next = None
            return last
        else:
            return head

    def isPalindrome(self, head: ListNode) -> bool:
        # 先找到中点
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next

        # 从中点开始反转链表
        p2 = self.reverse(slow)
        p1 = head
        while p1 and p2:
            if p1.val != p2.val:
                return False
            else:
                p1 = p1.next
                p2 = p2.next
        return True


# list = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
list = ListNode(1, ListNode(2))
# print(Solution().isPalindrome(list))

# [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/?show=1)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        while p1 or p2 or carry > 0:
            newVal = carry
            if p1:
                newVal += p1.val
                p1 = p1.next
            if p2:
                newVal += p2.val
                p2 = p2.next
            p.next = ListNode(newVal % 10)
            carry = (int)(newVal/10)
            p = p.next
        return dummy.next


l1 = ListNode(9, ListNode(9, ListNode(
    9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
# l1 = ListNode(2, ListNode(4, ListNode(3)))
# l2 = ListNode(5, ListNode(6, ListNode(4)))
# Solution().addTwoNumbers(l1, l2)

# [445. 两数相加 II](https://leetcode.cn/problems/add-two-numbers-ii/?show=1)
# 🍀 栈的实现：Python 的 List， LIFO, append and pop


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        s1, s2 = [], []
        while p1:
            s1.append(p1.val)
            p1 = p1.next
        while p2:
            s2.append(p2.val)
            p2 = p2.next
        dummy = ListNode(-1)
        carry = 0
        while s1 or s2 or carry > 0:
            newVal = carry
            if s1:
                ele1 = s1.pop()
                newVal += ele1
            if s2:
                ele2 = s2.pop()
                newVal += ele2
            node = ListNode(newVal % 10)
            node.next = dummy.next
            dummy.next = node
            carry = (int)(newVal/10)
        return dummy.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
# Solution().addTwoNumbers(l1, l2)

# [24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/?show=1)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # 反转一对（两个节点）
        prev = None
        cur = head
        for _ in range(2):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        head.next = self.swapPairs(cur)
        return prev


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# print(Solution().swapPairs(ListNode(1)).val)

# [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)


class Solution:
    # 迭代的方式来反转区间链表, 左闭右开
    def reverse(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = left
        while cur != right:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        a, b = head, head
        for _ in range(k):
            if not b:
                return head
            b = b.next
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead


l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# Solution().reverseKGroup(l1, 5)

# [83. 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next
            if fast.val != slow.val:
                slow.next = fast
                slow = slow.next
        if fast and slow:
            slow.next = None
        return head


l1 = ListNode(1, ListNode(1, ListNode(
    2, ListNode(3, ListNode(3, ListNode(4, ListNode(4)))))))

# Solution().deleteDuplicates(None)

# [148. 排序链表](https://leetcode.cn/problems/sort-list/)
# 归并排序


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sortFunc(head, None)

    def sortFunc(self, head: Optional[ListNode], tail: Optional[ListNode]):
        if not head:
            return head
        # 断开，另外一个节点在另个调用函数里
        if head.next == tail:
            head.next = None
            return head
        fast, slow = head, head
        while fast != tail:
            fast = fast.next
            slow = slow.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return self.merge(self.sortFunc(head, mid), self.sortFunc(mid, tail))

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        p = head
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
                p = p.next
            else:
                p.next = right
                right = right.next
                p = p.next
        if left and not right:
            p.next = left
        if right and not left:
            p.next = right
        return head.next


l1 = ListNode(4,
              ListNode(2,
                       ListNode(
                           1,
                           ListNode(3)
                       )
                       )
              )
result = Solution().sortList(None)
# print(result)

# [142. 环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/?favorite=2cktkvj)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先找相遇点
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        # 不存在环的情况下, fast 会到遇到空指针
        if not fast or not fast.next:
            return None
        # 把一个指针放到起点，另一个继续在相遇点，两者继续以同样的速度运动，会在环入口再次相遇
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1
# print(Solution().detectCycle(node1))


# [82 82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1, head)
        cur = head
        prev = dummy
        while cur:
            next = cur
            repeatNum = 0
            while next and next.val == cur.val:
                next = next.next
                repeatNum += 1
            if repeatNum > 1:
                prev.next = next
            else:
                prev = cur
            cur = next
        return dummy.next


l1 = ListNode(1, ListNode(2, ListNode(
    3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
Solution().deleteDuplicates(l1)
