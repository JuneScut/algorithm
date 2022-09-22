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
# print(solution.isAnagram("", ""))

# 【14】 [最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                return ''
        return prefix

    def lcp(self, s1, s2):
        minLen = len(s1) if len(s1) < len(s2) else len(s2)
        prefix = ''
        for i in range(minLen):
            if s1[i] == s2[i]:
                prefix += s1[i]
            else:
                return prefix
        return prefix


solution = Solution()
# print(solution.longestCommonPrefix(["dog"]))

# 【67】 [二进制求和](https://leetcode.cn/problems/add-binary/)


class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

    def addBinary2(self, a, b) -> str:
        return bin(int(a, 2)+int(b, 2))[2:]

    def addBinary3(self, a, b) -> str:
        if len(b) > len(a):
            a, b = b, a
        remain = 0
        res = ''
        i = len(a) - 1

        for j in range(len(b)-1, -1, -1):
            this = int(a[i]) + int(b[j]) + remain
            remain = this // 2
            res = str(this % 2) + res
            i -= 1

        for z in range(i, -1, -1):
            this = int(a[z]) + remain
            remain = this // 2
            res = str(this % 2) + res

        if remain:
            res = '1' + res

        return res


solution = Solution()
# print(solution.addBinary3("100", "110010"))

# 【28】 [实现strStr()](https://leetcode.cn/problems/implement-strstr/)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        if m < n:
            return -1
        for i in range(m):
            if haystack[i] == needle[0]:
                if haystack[i:i+n] == needle:
                    return i
        return -1


solution = Solution()
# print(solution.strStr('aaaaa', 'll'))

# 【118】 [杨辉三角](https://leetcode.cn/problems/pascals-triangle/)


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        res = [[1]]
        for i in range(1, numRows, 1):
            row = []
            row.append(1)
            preRow = res[i-1]
            for j in range(0, len(preRow)-1, 1):
                row.append(preRow[j]+preRow[j+1])
            row.append(1)
            res.append(row)
        return res


solution = Solution()
# print(solution.generate(5))

# 【406】[根据身高重建队列](https://leetcode.cn/problems/queue-reconstruction-by-height/)


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person]  # 等于 insert
        return ans


solution = Solution()
print(solution.reconstructQueue(
    [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]))
