from typing import List
import random

# 【215】[数组中的第k个大的元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/)
# 借助快速排序思想


class Solution:
    def swap(self, nums: List[int], a: int, b: int):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        return self.quickSelect(nums, 0, size-1, size-k)

    def quickSelect(self, nums: List[int], low: int, high: int, key: int) -> int:
        p = self.randomPartition(nums, low, high)
        if p == key:
            return nums[p]
        else:
            return self.quickSelect(nums, low, p-1, key) if p > key else self.quickSelect(nums, p+1, high, key)

    def randomPartition(self, nums: List[int], low: int, high: int) -> int:
        p = random.randint(low, high)
        self.swap(nums, p, high)
        return self.partitaion(nums, low, high)

    def partitaion(self, nums: List[int], low: int, high) -> int:
        i = low-1
        x = nums[high]
        for j in range(low, high, 1):
            if (nums[j] <= x):
                i += 1
                self.swap(nums, i, j)
        i += 1
        self.swap(nums, i, high)
        return i


# solution = Solution()
# print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 3))

# 【341】 [扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/)
