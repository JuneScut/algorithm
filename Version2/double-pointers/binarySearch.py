from typing import List

# [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/?favorite=2cktkvj)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.findLeftBound(nums, target)
        r = self.findRightBound(nums, target)
        return [l, r]

    def findLeftBound(self, nums: List[int], target: int) -> int:
        # 左闭右闭区间
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left == len(nums):
            return -1
        return left if nums[left] == target else -1

    def findRightBound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right < 0:
            return right
        return right if nums[right] == target else -1

nums = []
# print(Solution().searchRange(nums, 6))


# [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        # 左闭右闭区间
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            # 左边有序
            if nums[0] <= nums[mid]:
                # target 在左边
                if nums[0] <= target and target < nums[mid]:
                    right = mid -1
                # target 在右边
                else:
                    left = mid + 1
            # 右边有序
            elif nums[mid] <= nums[n-1]:
                # target 在右边
                if nums[mid] < target and target <= nums[n-1]:
                    left = mid + 1
                # target 在左边
                else:
                    right = mid - 1
        return -1

# nums = [4,5,6,7,0,1,2]
# nums = [6, 7, 0, 1, 2, 4, 5]
nums = [1]
print(Solution().search(nums, 0))
            
                

