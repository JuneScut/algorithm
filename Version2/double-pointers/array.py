from typing import List
from sortedcontainers import SortedList
import bisect

# 数组指针：
# 1. 快慢指针修改数组
# 2. 快慢指针修改滑动窗口大小
# 3. 左右指针 二分查找


# [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums) - 1:
            fast += 1
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
nums = [1,1,2]
# print(Solution().removeDuplicates(nums))

# [27. 移除元素](https://leetcode.cn/problems/remove-element/)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
    
nums = [0,1,2,2,3,0,4,2]
# print(Solution().removeElement([], 0))

# [283. 移动零](https://leetcode.cn/problems/move-zeroes/)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 等于原地先删除元素 0， 再把后边的所有都置为 0
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        while slow < len(nums):
            nums[slow] = 0
            slow += 1

nums = [0]
Solution().moveZeroes(nums)
# print(nums)

# [1004. 最大连续1的个数 III](https://leetcode.cn/problems/max-consecutive-ones-iii/)
# 反转 0 1 数组，更容易判断 0 的个数，可以直接通过前缀和
# rsum 和 lsum 分别表示下标是 right 和 left 的前缀和
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        lsum, rsum = 0, 0
        ans = 0

        while right < len(nums):
            rsum += 1 - nums[right] 

            while lsum < rsum - k:
                lsum += 1 - nums[left]
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans
    
# print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

# [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0
        window = {}
        while right < len(nums):
            incoming = nums[right]
            window[incoming] = window.get(incoming, 0) + 1
            if window.get(incoming) > 1:
                return True
            right += 1

            while (right - left) > k:
                deleting = nums[left]
                window[deleting] = window[deleting] - 1
                left += 1

        return False
    
nums = [1,2,3,1,2,3]
# print(Solution().containsNearbyDuplicate(nums, 2))

# [220. 存在重复元素 III](https://leetcode.cn/problems/contains-duplicate-iii/)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx-1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx+1] - window[idx]) <= t:
                return True
        return False
    
nums = [1,5,9,1,5,9]
# print(Solution().containsNearbyAlmostDuplicate(nums, 2, 3))


# [424. 替换后的最长重复字符](https://leetcode.cn/problems/longest-repeating-character-replacement/?show=1)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        window = {}
        maxNumber = 0 # 拥有最多字符的字母的个数
        res = 0
        while right < len(s):
            incoming = s[right]
            window[incoming] = window.get(incoming, 0) + 1
            maxNumber = max(window.get(incoming), maxNumber)
            right += 1

            if (right - left - maxNumber) > k:
                deleting = s[left]
                window[deleting] = window.get(deleting) - 1
                left += 1

            res = max(res, right-left)
        return res

s = "ABAB"
# print(Solution().characterReplacement(s, 2))


# [713. 乘积小于 K 的子数组](https://leetcode.cn/problems/subarray-product-less-than-k/?show=1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        prod = 1
        res = 0
        while right < len(nums):
            prod = prod * nums[right]

            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1

            res += right - left + 1
            right += 1

        return res

nums = [1, 2, 3]
# print(Solution().numSubarrayProductLessThanK(nums, 0))


# [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/?favorite=2cktkvj)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            curHeight = min(height[left], height[right])
            cur = (right - left) * curHeight
            res = max(cur, res)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
    
nums = [5,4,3,2,1]
# print(Solution().maxArea(nums))


# [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/?favorite=2cktkvj)
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        l_max, r_max = 0, 0
        res = 0
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(Solution().trap(height))

# [15. 三数之和](https://leetcode.cn/problems/3sum/?favorite=2cktkvj)
class Solution:
    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        res = []
        left, right = start, len(nums)-1
        while left < right:
            l = nums[left]
            r = nums[right]
            cur = l + r
            if cur == target:
                res.append([l, r])
                while left < right and nums[left] == l:
                    left += 1
                while left < right and nums[right] == r:
                    right -= 1
            elif cur < target:
                while left < right and nums[left] == l:
                    left += 1
            else:   
                while left < right and nums[right] == r:
                    right -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        m = len(nums)
        while i < m - 1:
            curThird = nums[i]
            twoSumRes = self.twoSum(nums, i+1, -1*curThird)
            if twoSumRes:
                for twoSumResItem in twoSumRes:
                    res.append([nums[i], twoSumResItem[0], twoSumResItem[1]])
            while i < m and nums[i] == curThird:
                    i += 1
        return res
    
nums = [0,1,1]
# print(Solution().threeSum(nums))
            

# [75. 颜色分类](https://leetcode.cn/problems/sort-colors/?favorite=2cktkvj)
from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_counter = Counter(nums)
        i = 0
        bound = nums_counter.get(0, 0)
        while i < bound:
            nums[i] = 0
            i += 1
        bound += nums_counter.get(1, 0)
        while i < bound:
            nums[i] = 1
            i += 1
        bound += nums_counter.get(2, 0)
        while i < bound:
            nums[i] = 2
            i += 1

    # 使用双指针，把所有的 0 排到左边，把所有的 2 排到右边
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                if nums[i] != 1:
                    i -= 1
            i += 1

nums = [2,0,1]
Solution().sortColors2(nums)
print(nums)



