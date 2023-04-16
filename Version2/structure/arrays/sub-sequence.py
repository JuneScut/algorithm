from typing import List

# [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/?favorite=2cktkvj)
# 排序算法超出复杂度限制
# 利用空间换时间，用 set/Map 记录元素，查找速度快


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set()
        res = 0
        for val in nums:
            num_sets.add(val)
        for val in nums:
            # 如果不是第一个元素，就直接跳过吧
            if (val-1) in num_sets:
                continue
            # 第一个元素，查找最多能到哪
            curNum = val
            curLen = 1
            while (curNum+1) in num_sets:
                curLen += 1
                curNum += 1
            res = max(curLen, res)
        return res


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(nums))

nums = [1, 2]
a, b = nums
print(a, b)


while True:
    try:
        N, M = [int(each) for each in input().split()]
        scores = [int(each) for each in input().split()]
        operations = []

        for i in range(M):
            operations.append(input().split())
        results = []
        for opeartion in operations:
            if opeartion[0] == 'U':
                scores[int(opeartion[1])-1] = int(opeartion[2])
                continue
            else:
                start = min(int(opeartion[1]), int(opeartion[2]))
                end = max(int(opeartion[1]), int(opeartion[2]))
                ret = 0
                for i in range(start-1, end):
                    ret = max(ret, scores[i])
                results.append(ret)

        for each in results:
            print(each)

    except:
        break
