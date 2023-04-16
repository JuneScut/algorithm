from typing import List

# [303. 区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/)


class NumArray:
    sumArray = []

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.sumArray = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            self.sumArray[i] = self.sumArray[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.sumArray[right+1] - self.sumArray[left]


arr = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(arr)
# print(numArray.sumRange(0, 2))

# [1. 两数之和](https://leetcode.cn/problems/two-sum/?favorite=2cktkvj)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndex = {}
        for (idx, value) in enumerate(nums):
            need = target - value
            if valToIndex.get(need) != None:
                return [idx, valToIndex[need]]
            valToIndex[value] = idx
        return None


nums = [3, 3]
# print(Solution().twoSum(nums, 6))

# [4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/?favorite=2cktkvj)
# 题目是求中位数，其实就是求第 k 小数的一种特殊情况，而求第 k 小数有一种算法。
# 由于数列是有序的，其实我们完全可以一半儿一半儿的排除。假设我们要找第 k 小数，我们可以每次循环排除掉 k/2 个数。
# https://leetcode.cn/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        # 求两个正序数组的前 k 个数
        def findKthElement(k: int) -> float:
            idx1, idx2 = 0, 0
            while True:
                # 特殊情况或者已经找到：
                if idx1 == m:
                    return nums2[idx2 + k - 1]
                if idx2 == n:
                    return nums1[idx1 + k - 1]
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])
                # 查找过程
                newIdx1 = min(idx1 + k//2 - 1, m-1)
                newIdx2 = min(idx2 + k//2 - 1, n-1)
                pivot1 = nums1[newIdx1]
                pivot2 = nums2[newIdx2]
                if pivot1 >= pivot2:
                    k = k - (newIdx2 - idx2 + 1)
                    idx2 = newIdx2 + 1
                else:
                    k = k - (newIdx1 - idx1 + 1)
                    idx1 = newIdx1 + 1

        totalLength = m + n
        if totalLength % 2 == 1:
            return findKthElement((totalLength + 1)//2)
        else:
            return (findKthElement(totalLength//2) + findKthElement(totalLength//2 + 1)) / 2


nums1 = [1, 2]
nums2 = [3, 4]
# print(Solution().findMedianSortedArrays(nums1, nums2))

# [31. 下一个排列](https://leetcode.cn/problems/next-permutation/?favorite=2cktkvj)
# 下一个字典序算法：https://leetcode.cn/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
# 1. 从后向前找到第一个升序对 （i,j）
# 2. 从 [j, end] 寻找 A[k] > A[i], A[k] 尽量小
# 3. 交换 A[k] 和 A[i], 此时 [j..end] 必然还是保持倒序
# 4. 将 A[j..end] 调整为升序


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 1. 从后向前找到第一个升序对 （i,j）
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # 确保不是最后一个排列
        if i >= 0:
            # 2. 从 [j, end] 寻找 A[k] > A[i], A[k] 尽量小
            j = n-1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # 4. 将 A[j..end] 调整为升序
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        print(nums)


nums = [2, 1, 2, 2, 2, 2, 2, 1]
# Solution().nextPermutation(nums)

# [84. 柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/)
# 暴力解法：固定高度，找到最大宽度


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for left in range(0, len(heights)):
            minHeight = 99999
            for right in range(left, len(heights)):
                minHeight = min(minHeight, heights[right])
                res = max(res, minHeight*(right-left+1))
        return res

# 在一维数组中对每一个数找到第一个比自己小的元素。这类“在一维数组中找第一个满足某种条件的数”的场景就是典型的单调栈应用场景
# 操作规则（下面都以单调递增栈为例）
# 1. 如果新的元素比栈顶元素大，就入栈
# 2. 如果新的元素较小，那就一直把栈内元素弹出来，直到栈顶比新元素小


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 哨兵机制
        heights.insert(0, 0)
        heights.append(0)
        stack = []
        res = 0
        for i in range(0, len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                cur = heights[stack[-1]]
                stack.pop()
                right = i
                left = 0 if not stack else stack[-1]
                res = max(res, (right-left-1)*cur)
            stack.append(i)
        return res


heights = [2, 1, 5, 6, 2, 3]
# print(Solution().largestRectangleArea(heights))

# [287. 寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 1, n-1
        ans = -1
        while left <= right:
            # 不重复区间内的中位数
            mid = left + (right-left) // 2
            cnt = 0
            for i in range(0, n):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        return ans


nums = [1, 3, 4, 2, 2]
# print(Solution().findDuplicate(nums))

# [169. 多数元素](https://leetcode.cn/problems/majority-element/?favorite=2cktkvj)
# 寻找众数
# 联想正反电荷


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        target = nums[0]
        for val in nums:
            if count == 0:
                target = val
                count = 1
            else:
                if val == target:
                    count += 1
                else:
                    count -= 1
        return target


nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums))
