# coding=utf-8
# (Easy)455. 分发饼干
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


# (Medium) 435. 无重叠区间
class Solution(object):
    def takeSecond(self, elem):
        return elem[1]

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 按区间尾排序
        if len(intervals) == 0:
            return 0
        intervals.sort(key=self.takeSecond)
        prev = intervals[0][1]
        count = 0
        for idx in range(1, len(intervals)):
            if intervals[idx][0] < prev:
                count += 1
            else:
                prev = intervals[idx][1]
        return count


solution = Solution()
print(solution.eraseOverlapIntervals([]))

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
