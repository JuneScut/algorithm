# coding=utf-8
# (Easy)455. 分发饼干
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child = 0
        for cookie in s:
            if child == len(g):
                break
            if cookie >= g[child]:
                child += 1

        return child


solution = Solution()
print(solution.findContentChildren([1, 2, 3], [1, 1]))
