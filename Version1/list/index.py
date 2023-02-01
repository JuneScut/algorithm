# 【704】 [二分查找](https://leetcode.cn/problems/binary-search/)
from math import ceil
from turtle import left, right
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = ceil(left + (right-left)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


solution = Solution()
# print(solution.search([-1, 0, 3, 5, 9, 12], 9))

# 【34】[在排序数组查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.searchLeftBound(nums, target)
        r = self.searchRightBound(nums, target)
        return [l, r]

    def searchLeftBound(self, nums: List[int], target: int):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = ceil(left + (right-left)/2)
            if nums[mid] == target:
                right = mid-1
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
        if left == len(nums):
            return -1
        return left if nums[left] == target else -1

    def searchRightBound(self, nums: List[int], target: int):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = ceil(left+(right-left)/2)
            if nums[mid] == target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1

        if left-1 < 0:
            return -1
        return left-1 if nums[left-1] == target else -1


solution = Solution()
print(solution.searchRange([1], 1))
