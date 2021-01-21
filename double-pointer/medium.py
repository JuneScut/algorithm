from typing import List
import math
# 142. Linked List Cycle II (Medium)
# 对于链表找环路的问题，有一个通用的解法——快慢指针(Floyd 判圈法)。给定两个指针， 分别命名为 slow 和 fast，起始位置在链表的开头。每次 fast 前进两步，slow 前进一步。如果 fast 可以走到尽头，那么说明没有环路;如果 fast 可以无限走下去，那么说明一定有环路，且一定存 在一个时刻 slow 和 fast 相遇。当 slow 和 fast 第一次相遇时，我们将 fast 重新移动到链表开头，并 让 slow 和 fast 每次都前进一步。当 slow 和 fast 第二次相遇时，相遇的节点即为环路的开始点。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         fast = head
#         slow = head
#         while fast != None:
#             slow = slow.next
#             if fast.next != None:
#                 fast = fast.next.next
#             else:
#                 return None
#             if fast == slow:
#                 ptr = head
#                 while ptr != slow:
#                     ptr = ptr.next
#                     slow = slow.next
#                 return ptr


# a = ListNode(3)
# b = ListNode(2)
# c = ListNode(0)
# d = ListNode(-4)
# a.next = b
# b.next = c
# c.next = d
# d.next = b

# solution = Solution()
# print(solution.detectCycle(a).val)


# 524. Longest Word in Dictionary through Deleting (Medium)
# list.sort(key=None,reverse=False)
# 对原列表进行排序，完成排序后，原列表变为有序列表。默认情况（不传入任何参数时）按字典顺序排序。
# class Solution:
#     def findLongestWord(self, s: str, d: List[str]) -> str:
#         d.sort(key=None, reverse=False)
#         sortedStr = sorted(d, key=lambda str: len(str), reverse=True)
#         m = len(s)
#         for item in sortedStr:
#             i = 0
#             j = 0
#             n = len(item)
#             while i < m and j < n:
#                 if s[i] == item[j]:
#                     i = i + 1
#                     j = j + 1
#                 else:
#                     i = i + 1
#                 if j == n and i <= m:
#                     return item
#         return ""


# solution = Solution()
# print(solution.findLongestWord("abpcplea", [""]))


# 633. 平方数之和
# 开方 需要引入math库 math.sqrt

# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         left = 0
#         right = math.floor(math.sqrt(c))
#         while left <= right:
#             sum = pow(left, 2) + pow(right, 2)
#             if sum == c:
#                 return True
#             elif sum > c:
#                 right -= 1
#             else:
#                 left += 1
#         return False
        

# solution = Solution()
# print(solution.judgeSquareSum(1))

# 680. 验证回文字符串 Ⅱ
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]: 
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True


solution = Solution()
print(solution.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
