# !/usr/bin/env python3
# coding=utf-8

from typing import List

# [217][存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if nums == None:
#             return False
#         countMap = {}
#         for i in nums:
#             if countMap.get(i, -1) == -1:
#                 countMap[i] = 1
#             else:
#                 return True
#         return False


# solution = Solution()
# print(solution.containsDuplicate([1, 2, 3, 4]))

# [219][存在重复元素II](https://leetcode-cn.com/problems/contains-duplicate-ii/)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexMap = {}
        for index, item in enumerate(nums):
            idx = indexMap.get(item)
            if idx == None or index - idx > k:
                indexMap[item] = index
            else:
                return True

        return False


solution = Solution()
print(solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
