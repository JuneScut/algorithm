# coding=utf-8
# (Easy) 分配问题 455. 分发饼干
# class Solution(object):
#     def findContentChildren(self, g, s):
#         """
#         :type g: List[int]
#         :type s: List[int]
#         :rtype: int
#         """
#         g.sort()
#         s.sort()
#         child = 0
#         for cookie in s:
#             if child == len(g):
#                 break
#             if cookie >= g[child]:
#                 child += 1

#         return child


# solution = Solution()
# print(solution.findContentChildren([1, 2, 3], [1, 1]))


# (Medium) 区间问题 435. 无重叠区间
# class Solution(object):
#     def takeSecond(self, elem):
#         return elem[1]

#     def eraseOverlapIntervals(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: int
#         """
#         # 按区间尾排序
#         if len(intervals) == 0:
#             return 0
#         intervals.sort(key=self.takeSecond)
#         prev = intervals[0][1]
#         count = 0
#         for idx in range(1, len(intervals)):
#             if intervals[idx][0] < prev:
#                 count += 1
#             else:
#                 prev = intervals[idx][1]
#         return count


# solution = Solution()
# print(solution.eraseOverlapIntervals([]))

# (Easy) 453. 最小操作次数使数组元素相等
# 暴力法 每次增加1，循环判断最小 != 最大时，排序，除了最后一位，都+1
# 暴力法改进2  循环判断最小 != 最大时，排序，除了最后一位，都增加（最大-最小）
# 暴力法改进3  其实并不需要真正改变数组
# class Solution(object):
#     def minMoves(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nums.sort()
#         count = 0
#         index = len(nums) - 1
#         while index > 0:
#             count += nums[index] - nums[0]
#             index -= 1
#         return count


# solution = Solution()
# print(solution.minMoves([5, 6, 8, 8, 5]))


# 贪心算法，只要满足某一项为0且左右两项均为0就种下一棵树
# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         count = 0
#         lastIdx = len(flowerbed) - 1
#         if lastIdx == 0:
#             if flowerbed[0] == 0:
#                 count += 1
#             return count >= n

#         if flowerbed[0] == 0 and flowerbed[1] == 0:
#             flowerbed[0] = 1
#             count += 1

#         for idx in range(1, lastIdx):
#             if flowerbed[idx] == 0 and flowerbed[idx-1] == 0 and flowerbed[idx+1] == 0:
#                 flowerbed[idx] = 1
#                 count += 1
#         if flowerbed[lastIdx] == 0 and flowerbed[lastIdx-1] == 0:
#             flowerbed[lastIdx] = 1
#             count += 1

#         return count >= n


# solution = Solution()
# print(solution.canPlaceFlowers([0, 0], 2))


# 【Medium】452. 用最少数量的箭引爆气球
# 和435对比起来看
# class Solution(object):
#     def takeSecond(self, element):
#         return element[1]

#     def findMinArrowShots(self, points):
#         """
#         :type points: List[List[int]]
#         :rtype: int
#         """
#         if len(points) == 0:
#             return 0
#         points.sort(key=self.takeSecond)
#         count = 1
#         prev = points[0][1]
#         for idx in range(1, len(points)):
#             if points[idx][0] > prev:
#                 count += 1
#                 prev = points[idx][1]
#         return count


# solution = Solution()
# print(solution.findMinArrowShots([[2, 3], [2, 3]]))


# 【medium】763. 划分字母区间
# class Solution(object):
#     def takeFirst(self, element):
#         return element[0]

#     def partitionLabels(self, S):
#         """
#         :type S: str
#         :rtype: List[int]
#         """

#         d = {}
#         for idx, char in enumerate(S):
#             if char in d:
#                 d[char][1] = idx
#             else:
#                 d[char] = [idx, idx]

#         vectors = list(d.values())
#         if len(vectors) == 0:
#             return []
#         vectors.sort(key=self.takeFirst)
#         prevS = vectors[0][0]
#         prevE = vectors[0][1]
#         result = []
#         for idx in range(1, len(vectors)):
#             currentS = vectors[idx][0]
#             currentE = vectors[idx][1]
#             if currentS > prevE:
#                 result.append(prevE-prevS + 1)
#                 prevS = currentS
#                 prevE = currentE
#             elif currentE > prevE:
#                 prevE = currentE
#         result.append(prevE-prevS + 1)

#         return result


# solution = Solution()
# print(solution.partitionLabels(""))


# 122 股票交易
from typing import List


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        profit = 0
        lst = prices[0]
        for index in range(1, length):
            if prices[index] > lst:
                profit += prices[index] - lst
                lst = prices[index]
            else:
                lst = prices[index]
        return profit


solution = Solution()
# print(solution.maxProfit([7, 6, 4, 3, 1]))


# 【402】 [移掉k位数字](https://leetcode.cn/problems/remove-k-digits/)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []

        # 构造一个递增的子序列
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        finalStack = numStack if k <= 0 else numStack[:-k]
        return ''.join(finalStack).lstrip('0') or '0'


solution = Solution()
# print(solution.removeKdigits('1432219', 3))

# 【860】[柠檬水找零](https://leetcode.cn/problems/lemonade-change/)


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            elif bill == 20:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif not ten and five >= 3:
                    five -= 3
                else:
                    return False
        return True


solution = Solution()
print(solution.lemonadeChange([5, 5, 10, 10, 20]))
