# coding=utf-8
# To be able to annotate what types your list should accept, you need to use typing.List
from typing import List

# 167. Two Sum II - Input array is sorted (Easy)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         i = 0
#         j = len(numbers)-1
#         if j <= 0:
#             return None
#         while i < j:
#             sum = numbers[i] + numbers[j]
#             if sum == target:
#                 break
#             elif sum < target:
#                 i = i + 1
#             else:
#                 j = j - 1
#         return [i+1, j+1] if i < j else None

# solution = Solution()
# result = solution.twoSum([2, 2], 4)
# print(result)


# 88. Merge Sorted Array (Easy)
# 这里多保存了一个指针，方便复制剩余数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        pos = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[pos] = nums1[i]
                i -= 1
                pos -= 1
            else:
                nums1[pos] = nums2[j]
                j -= 1
                pos -= 1
        while pos >= 0 and j >= 0:
            nums1[pos] = nums2[j]
            pos -= 1
            j -= 1


solution = Solution()
arr1 = [1]
solution.merge(arr1, 1, [0], 0)
print(arr1)
