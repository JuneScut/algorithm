# !/usr/bin/env python3
# coding=utf-8

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [141] [环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow, fast = head, head
#         while fast != None and fast.next != None:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False

# 【21】[合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         head = ListNode(0, None)
#         cur = head
#         while list1 != None and list2 != None:
#             if list1.val <= list2.val:
#                 cur.next = list1
#                 list1 = list1.next
#             else:
#                 cur.next = list2
#                 list2 = list2.next
#             cur = cur.next
#         if list1 == None:
#             cur.next = list2
#         if list2 == None:
#             cur.next = list1
#         return head.next

# solution = Solution()
# list1 = ListNode(1, ListNode(2, ListNode(4, None)))
# list2 = ListNode(1, ListNode(3, ListNode(4, None)))

# c = solution.mergeTwoLists(list1, list2)
# while c != None:
#     print(c.val)
#     c = c.next

# [160] [相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 != None else headB
            p2 = p2.next if p2 != None else headA
        return p1


cross = ListNode(2, ListNode(4, None))
list1 = ListNode(1, ListNode(9, ListNode(1, cross)))
list2 = ListNode(3, cross)

solution = Solution()
c = solution.getIntersectionNode(list1, list2)
print(c.val if c != None else c)

# 【206】 [反转链表](https://leetcode.cn/problems/reverse-linked-list/)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if not head or not head.next:
            return head
        # 翻转除了 head 的剩余部分, 返回的为最后一个节点
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

# 【92】 [反转链表II](https://leetcode.cn/problems/reverse-linked-list-ii/)


class Solution:
    def __init__(self) -> None:
        self.successor = None

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == 1:
            return self.reveresN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)
        return head

    # 反转链表的前 n 个节点 https://labuladong.github.io/algo/images/%e5%8f%8d%e8%bd%ac%e9%93%be%e8%a1%a8/7.jpg

    def reveresN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            self.successor = head.next  # 记录第 n+1 个节点
            return head
        last = self.reveresN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last


solution = Solution()
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
solution.reverseBetween(l, 2, 4)