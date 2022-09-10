from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        cnt = 0  # 所有需要通过的方格
        start = (-1, -1)
        end = (-1, -1)
        ans = 0
        # 找到起点和终点
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cnt += 1
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)

        def dfs(i, j, flag):
            nonlocal ans
            # flag 当前通过的空格子
            nodes = [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]

            if flag == cnt:
                if end in nodes:
                    ans += 1
                return

            for a, b in nodes:
                if 0 <= a < m and 0 <= b < n and not grid[a][b]:
                    # 防止下次重复走过
                    grid[a][b] = -1
                    dfs(a, b, flag+1)
                    grid[a][b] = 0
            return

        x, y = start
        dfs(x, y, 0)
        return ans


solution = Solution()
# print(solution.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))

# 【93】[复原IP地址](https://leetcode.cn/problems/restore-ip-addresses/)


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        segCount = 4
        n = len(s)
        ans = []
        segments = [0]*segCount

        def dfs(segId: int, start: int):
            if segId == segCount:
                if start == n:
                    ipAddr = '.'.join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return
            if start == n:
                return
            # 前导0
            if s[start] == '0':
                segments[segId] = 0
                dfs(segId+1, start+1)
                return
            # 一般情况下：
            addr = 0
            for i in range(start, len(s)):
                addr = 10 * addr + (ord(s[i]) - ord('0'))
                if 0 <= addr <= 0xFF:
                    segments[segId] = addr
                    dfs(segId+1, i+1)
                else:
                    continue

        dfs(0, 0)
        return ans


solution = Solution()
print(solution.restoreIpAddresses('101023'))
