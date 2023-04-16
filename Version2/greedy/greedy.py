from collections import deque
from sortedcontainers import SortedList
from typing import List

# [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/?favorite=2cktkvj)
# 维持一个最长距离
# 特殊情况，遇到 0


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            # 遇上 0, 判断下是否能跳过去
            if farthest <= i:
                return False
        return farthest >= n-1


nums = [3, 2, 1, 0, 4]
# print(Solution().canJump(nums))


# [2071. 你可以安排的最多任务数目](https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/)
# 二分查找+贪心算法
# 二分查找，看 task[...mid] 之前的任务是否都能被 workers 做完，逐步扩大看范围
# 贪心算法，每次都先做难的任务
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        # 看 task[...mid] 之前的任务是否都能被 workers 做
        def check(mid: int) -> bool:
            p = pills
            for i in range(mid-1, -1, -1):
                curTask = tasks[i]
                # 先看最大的 worker 能不能完成这个任务
                ws = SortedList(workers[m-mid:])
                max_worker = ws[-1]
                if max_worker > curTask:
                    ws.pop()  # 可以完成，从待选列表中选出排除掉
                else:
                    if p == 0:
                        return False  # 已经没有药了
                    rep = ws.bisect_left(curTask-strength)
                    if rep == len(ws):
                        return False  # 磕了药还是无法完成
                    p -= 1
                    ws.pop()
            return True

        def check2(mid: int) -> bool:
            p = pills
            ws = deque()
            ptr = m - 1
            # 从大到小枚举每一个任务
            for i in range(mid - 1, -1, -1):
                while ptr >= m - mid and workers[ptr] + strength >= tasks[i]:
                    ws.appendleft(workers[ptr])
                    ptr -= 1
                if not ws:
                    return False
                # 如果双端队列中最大的元素大于等于 tasks[i]
                elif ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    p -= 1
                    ws.popleft()
            return True

        left, right = 1, min(n, m)
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            if check2(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


tasks = [5, 9, 8, 5, 9]
workers = [1, 6, 4, 2, 6]
pills = 1
strength = 5
print(Solution().maxTaskAssign(tasks, workers, pills, strength))
