# 【395】 [至少有k个重复字符的字符串](https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/)
from posixpath import split


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(subS, k) for subS in s.split(c))
        return n

solution = Solution()
print(solution.longestSubstring('aaabb', 3))
        