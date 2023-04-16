from typing import List

# [136. 只出现一次的数字](https://leetcode.cn/problems/single-number/?favorite=2cktkvj)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            res ^= val
        return res


nums = [1]
print(Solution().singleNumber(nums))
