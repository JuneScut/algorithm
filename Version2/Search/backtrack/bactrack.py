from typing import List
# 回溯算法，时间复杂度都不可能低于 O(N!)
# 因为穷举整棵决策树是无法避免的。这也是回溯算法的一个特点，不像动态规划存在重叠子问题可以优化，回溯算法就是纯暴力穷举，复杂度一般都很高。
# 框架结构：
# for 选择 in 选择列表:
#     # 做选择
#     将该选择从选择列表移除
#     路径.add(选择)
#     backtrack(路径, 选择列表)
#     # 撤销选择
#     路径.remove(选择)
#     将该选择再加入选择列表

# [46. 全排列](https://leetcode.cn/problems/permutations/)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        track = []
        used = [False for _ in range(len(nums))]
        self.backtrack(nums, track, used)
        return self.res

    # 用 used 布尔数组取代路径，表示该节点是否已经在路径中
    def backtrack(self, nums: List[int], track: List[int], used: List[bool]):
        if len(track) == len(nums):
            self.res.append(track[:])
            return
        for (index, value) in enumerate(nums):
            if used[index]:
                continue
            # 做选择
            track.append(value)
            used[index] = True
            self.backtrack(nums, track, used)
            # 撤销选择
            used[index] = False
            track.pop()

nums = [1]
# print(Solution().permute(nums))

# [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/?favorite=2cktkvj)
# 区别于上一道题，这道题目是有拨号顺序的，所以每次记录一个开始点
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        if not digits:
            return self.res
        self.mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        track = []
        start = 0
        self.backtrack(digits, track, start)
        return self.res

    def backtrack(self, digits: str, track: List[str], start: int):
        if len(track) == len(digits):
            self.res.append(''.join(track))
            return
        
        # for digit in digits[start:]: 这里不需要循环，因为是有顺序的
        index = int(digits[start])
        for ch in self.mapping[index]:
            # 做选择
            track.append(ch)
            self.backtrack(digits, track, start+1)
            # 撤销选择，比如第一个选了A，撤销A， 选B
            track.pop()

digits = "1"
# print(Solution().letterCombinations(digits))

# [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/?favorite=2cktkvj)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.n = n
        track = []
        self.backtrack(n, n, track)
        return self.res

    # 用 leftNum 和 rightNum 记录还可以使用的左右括号数量
    # cur 记录当前已经有的括号数量
    def backtrack(self, leftNum: int, rightNum: int, track: List[str]):
        # 过滤不合格的括号组
        if leftNum > rightNum:
            return
        # 触发返回
        if leftNum < 0 or rightNum < 0:
            return
        if leftNum == 0 and rightNum == 0 and len(track) == 2 * self.n:
            self.res.append(''.join(track))
            return
        
        # 做选择
        track.append('(')
        self.backtrack(leftNum-1, rightNum, track)
        track.pop() # 撤销选择
        # 做选择
        track.append(')')
        self.backtrack(leftNum, rightNum-1, track)
        track.pop() # 撤销选择

# print(Solution().generateParenthesis(3))

# [39. 组合总和](https://leetcode.cn/problems/combination-sum/?favorite=2cktkvj)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        track = []
        self.backtrack(candidates, track, 0, target)
        return self.res

    def backtrack(self, candidates: List[int], track: List[int], start: int, diff: int):
        if diff == 0:
            self.res.append(track[:])
            return
        if diff < 0:
            return
        for idx in range(start, len(candidates)):
            value = candidates[idx]
            track.append(value)
            diff -= value
            # 注意这里，因为元素可以重复选择，所以 idx 不需要加 1 📢
            self.backtrack(candidates, track, idx, diff)
            diff += value
            track.pop()

candidates = [2]
target = 1
# print(Solution().combinationSum(candidates, target))

# [78. 子集](https://leetcode.cn/problems/subsets/?favorite=2cktkvj)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        track = []
        self.backtrack(nums, track, 0)
        return self.res

    def backtrack(self, nums: List[int], track: List[int], start: int):
        self.res.append(track[:])

        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, track, i+1) # 注意这里是 i 而不是 start
            track.pop()

nums = [0]
print(Solution().subsets(nums))