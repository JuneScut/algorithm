# !/usr/bin/env python3
# coding=utf-8

from re import I
from typing import List

from numpy import ptp
# 7 整数反转
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         ans = 0
#         absX = abs(x)
#         while (absX !=0):
#             pop = int(absX%10)
#             ans = ans * 10 + pop
#             absX = int(absX/10)
#         if x<0:
#             ans = -ans
#         return  ans if -2147483648 < ans < 2147483647 else 0

# solution = Solution()
# print(solution.reverse(-120))

# 最长公共前缀
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         strsLen = len(strs)
#         if strsLen == 0:
#             return ""
#         if strsLen == 1:
#             return strs[0]

#         def findCommon(str1, str2):
#             common = ""
#             l1 = len(str1)
#             l2 = len(str2)
#             list1 = list(str1)
#             list2 = list(str2)
#             if (l1 == 0 or l2 == 0):
#                 return common
#             else:
#                 index = 0
#                 minL = min(l1, l2)
#                 while index < minL:
#                     if (list1[index] == list2[index]):
#                         common += list1[index]
#                         index = index + 1
#                     else:
#                         break
#                 return common
#         common = strs[0]
#         for index in range(1, strsLen):
#             common = findCommon(common, strs[index])
#             if  common == "":
#                 break
#         return common


# solution = Solution()
# print(solution.longestCommonPrefix(["ab", "a"]))


# [268][丢失的数字](https://leetcode-cn.com/problems/missing-number/)

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         i, n, numsSum = 1, len(nums), sum(nums)
#         iSum = 0
#         while i <= n:
#             iSum += i
#             i += 1
#         return iSum - numsSum


# solution = Solution()
# print(solution.missingNumber([1]))

# 【169】[多数元素](https://leetcode-cn.com/problems/majority-element/)
# 摩尔投票！
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         if not nums:
#             return None
#         result, cnt = nums[0], 0
#         for n in nums:
#             if n == result:
#                 cnt += 1
#             else:
#                 cnt -= 1
#             if cnt < 0:
#                 result = n
#                 cnt = 0
#         return result


# solution = Solution()
# print(solution.majorityElement([3, 2, 3]))

#  重复 --> map
#  环入点 --> 快慢指针
# [202] [快乐树](https://leetcode-cn.com/problems/happy-number/)
# class Solution:
#     def getNext(self, n: int) -> int:
#         next = 0
#         while n > 0:
#             n, b = divmod(n, 10)
#             next += b ** 2
#         return next

#     def isHappy(self, n: int) -> bool:
#         slow, fast = n, self.getNext(n)
#         while fast != 1 and slow != fast:
#             slow = self.getNext(slow)
#             fast = self.getNext(self.getNext(fast))
#         return fast == 1


# solution = Solution()
# print(solution.isHappy(2))

# 【27】[移除元素](https://leetcode-cn.com/problems/remove-element/)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         start, end = 0, len(nums) - 1
#         while start <= end:
#             if nums[start] == val:
#                 nums[start] = nums[end]
#                 end -= 1
#             else:
#                 start += 1
#         return end + 1


# solution = Solution()
# arr = [0, 1, 2, 2, 3, 0, 4, 2]
# print(solution.removeElement(arr, 2))
# print(arr)

# 【205】[同构字符串](https://leetcode-cn.com/problems/isomorphic-strings/)
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         s2t = {}
#         t2s = {}
#         length = len(s)
#         idx = 0
#         while idx < length:
#             x, y = s[idx], t[idx]
#             if (s2t.get(x) != None and s2t.get(x) != y) or (t2s.get(y) != None and t2s.get(y) != x):
#                 return False
#             s2t[x] = y
#             t2s[y] = x
#             idx += 1
#         return True


# solution = Solution()
# print(solution.isIsomorphic('badc', 'baba'))

# 【290】[单词规律](https://leetcode-cn.com/problems/word-pattern/)
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         sArr = s.split(' ')
#         if len(pattern) != len(sArr):
#             return False
#         pTos, sTop = {}, {}
#         idx = 0
#         while idx < len(pattern):
#             x, y = pattern[idx], sArr[idx]
#             if (pTos.get(x) != None and pTos.get(x) != y) or (sTop.get(y) != None and sTop.get(y) != x):
#                 return False
#             pTos[x] = y
#             sTop[y] = x
#             idx += 1
#         return True


# solution = Solution()
# print(solution.wordPattern('abba', 'dog dog dog dog'))

# [242] [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList, tList = list(s), list(t)
        list.sort(sList)
        list.sort(tList)
        return ''.join(sList) == ''.join(tList)


solution = Solution()
print(solution.isAnagram("", ""))
