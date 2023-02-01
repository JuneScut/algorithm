# !/usr/bin/env python3
# coding=utf-8

import heapq
import random
from typing import List, Optional


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

# solution = Solution()
# c = solution.getIntersectionNode(list1, list2)
# print(c.val if c != None else c)

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


# solution = Solution()
# l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
# solution.reverseBetween(l, 2, 4)


# 【25】 [K个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/)
# 翻转链表 非常经典
class Solution:
    # 翻转某个区间的链表
    def reverse(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = a
        next = a
        while cur != b:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        a = head
        b = head
        for i in range(k):
            # base case: 如果不满足k个，则将最后剩余的节点保持原有顺序。
            if not b:
                return head
            b = b.next
        newHead = self.reverse(a, b)
        head.next = self.reverseKGroup(b, k)
        return newHead

# 【234】 [回文链表](https://leetcode.cn/problems/palindrome-linked-list/)
# 利用后序遍历来反转链表的值


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        return self.travel(head)

    def travel(self, right: Optional[ListNode]) -> bool:
        if not right:
            return True
        res = self.travel(right.next)
        res = res and right.val == self.left.val
        self.left = self.left.next
        return res

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        # 快慢指针找到中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next  # 说明是长度奇数

        # 然后把右侧的反转
        right = self.reverse(slow)
        left = head
        # 从两端开始比较
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        next = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


solution = Solution()
# print(solution.isPalindrome2(ListNode(1, ListNode(1, ListNode(2, ListNode(1))))))

# 【912】[排序数组](https://leetcode.cn/problems/sort-an-array/)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return nums
        p = self.partition(nums, left, right)
        self.quickSort(nums, left, p-1)
        self.quickSort(nums, p+1, right)
        return nums

    def partition(self, nums: List[int], startIndex: int, endIndex: int):
        pivotIdx = random.randint(startIndex, endIndex)
        nums[startIndex], nums[pivotIdx] = nums[pivotIdx], nums[startIndex]

        pivot = nums[startIndex]
        left = startIndex
        right = endIndex

        while left != right:
            while nums[right] > pivot and right > left:
                right -= 1

            while nums[left] <= pivot and left < right:
                left += 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]

        nums[startIndex] = nums[left]
        nums[left] = pivot

        return left


class Solution:
    def randomized_partition(self, nums, l, r):
        # 单边循环法
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[r]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums


solution = Solution()
# print(solution.sortArray([5, 1, 1, 2, 0, 0]))

# 【605】[种花问题](https://leetcode.cn/problems/can-place-flowers/)


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while n > 0 and i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2  # 避开相邻地
            else:
                if i == (len(flowerbed)-1) or flowerbed[i+1] != 1:
                    n -= 1
                    i += 2
                else:
                    i += 3
        return True if n <= 0 else False


solution = Solution()
# print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))


# 【937】[重新排列日志文件](https://leetcode.cn/problems/reorder-data-in-log-files/)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def trans(val: str) -> List[int]:
            a, b = val.split(' ', 1)
            res = (0, b, a) if b[0].isalpha() else (1,)
            return res

        logs.sort(key=trans)  # sort 是稳定排序
        return logs


solution = Solution()
# print(solution.reorderLogFiles(
#     ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))

# 【804】 [唯一摩斯密码词](https://leetcode.cn/problems/unique-morse-code-words/)


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = len(set("".join(MORSE[ord(ch)-ord('a')]
                  for ch in word) for word in words))
        return res


solution = Solution()
# print(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

# 【1859】[将句子排序](https://leetcode.cn/problems/sorting-the-sentence/)


class Solution:
    def sortSentence(self, s: str) -> str:
        def trans(s: str) -> int:
            return int(s[len(s)-1])
        arr = s.split(" ")
        arr.sort(key=trans)
        return " ".join([word[:-1] for word in arr])


solution = Solution()
# print(solution.sortSentence("Myself2 Me1 I4 and3"))


# 【539】[最小时间差](https://leetcode.cn/problems/minimum-time-difference/)
class Solution:
    def getMinutes(self, t: str) -> int:
        base = ord('0')
        return ((ord(t[0])-base)*10+(ord(t[1])-base)) * 60 + (ord(t[3])-base)*10 + (ord(t[4])-base)

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()  # 从小到大
        n = len(timePoints)
        ans = 60*24
        t0Minutes = self.getMinutes(timePoints[0])
        prev = t0Minutes
        for i in range(1, n):
            cur = self.getMinutes(timePoints[i])
            ans = min(ans, cur-prev)
            prev = cur
        ans = min(ans, t0Minutes+60*24 -
                  self.getMinutes(timePoints[n-1]))  # 首尾时间差
        return ans


solution = Solution()
# print(solution.findMinDifference(["23:59", "00:00"]))

# 【1669】 [合并两个链表](https://leetcode.cn/problems/merge-in-between-linked-lists/)


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        idx = 1
        cur = list1
        while idx < a and cur:
            cur = cur.next
            idx += 1
        prevNode = cur
        while idx <= b and cur:
            cur = cur.next
            idx += 1
        cur = cur.next
        nextNode = cur
        prevNode.next = list2
        cur = list2
        prev = None
        while cur:
            prev = cur
            cur = cur.next
        prev.next = nextNode
        return list1


# solution = Solution()
# print(solution.mergeInBetween(
#     ListNode(0,
#              ListNode(1,
#                       ListNode(2,
#                                ListNode(3,
#                                         ListNode(4,
#                                                  ListNode(5)))))), 3, 3,

#     ListNode(1000000, ListNode(1000001))
# ))


# 【83】[分隔链表](https://leetcode.cn/problems/partition-list/)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p = head
        p1, p2 = dummy1, dummy2
        while p:
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next
            temp = p.next
            p.next = None
            p = temp
        p1.next = dummy2.next
        return dummy1.next


# 【23】[合并k个链表](https://leetcode.cn/problems/merge-k-sorted-lists/)
# python heapq 不支持传入比较函数
# trick: 利用元组记录是第几个链表
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = []
        dummy = ListNode(-1)
        cur = dummy
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heads, (lists[i].val, i))
                lists[i] = lists[i].next
        while heads:
            val, i = heapq.heappop(heads)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(heads, (lists[i].val, i))
                lists[i] = lists[i].next
        return dummy.next


# solution = Solution()
# solution.mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(
#     1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])


# 【19】[删除链表的倒数第N个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = head
        p2 = dummy
        for _ in range(0, n):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next


solution = Solution()
# print(solution.removeNthFromEnd(ListNode(1), 1))

# 【876】[链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


solution = Solution()
# print(solution.middleNode(ListNode(1, ListNode(
#     2))))

# 【141】[环形链表](https://leetcode.cn/problems/linked-list-cycle/)
# 类似876，同样使用快慢指针
# 判断是否有环：快慢指针是否能相遇


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


# 【142】[环形链表](https://leetcode.cn/problems/linked-list-cycle-ii/)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先到相遇点
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        # 可能没有环
        if not fast or not fast.next:
            return None
        # 相遇后，一个放到起点，一个继续在相遇点，以同样的速度，再次相交时便在环的起点了（画图分析）
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
node4.next = node2

solution = Solution()
# print(solution.detectCycle(node1))


# 【160】[相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/)
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
