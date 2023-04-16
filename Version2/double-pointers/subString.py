from typing import List

# 快慢指针修改滑动窗口大小
# 1. 子串问题（子串是指连续的某段，如 s = "ADOBECODEBANC", t = "ABC"，最小覆盖子串 "BANC" ）
# 2.



#  [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)
# 窗口： 左闭右开，初始化：left=0, right=0。用
# Map 数组记录需要满足的条件：Need={'A': 1, 'B': 1, 'C': 1}, 
# Map 数组记录需要当前窗口：Window={'A': 0, 'B': 0, 'C': 0}, 

# 1️⃣ 先不断地增加 right 指针扩大窗口 [left, right)，直到窗口中的字符串符合要求（包含了 T 中的所有字符）
# 😯 停止增加 right，转而不断增加 left 指针缩小窗口 [left, right)，直到窗口中的字符串不再符合要求 ====> 记录这个时候的结果更新
# 🌲 重复这两步，直到 right 到达字符串 S 的尽头。


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 初始化
        left, right = 0, 0
        needs = {}
        for c in t:
            needs[c] = needs.get(c, 0) + 1
        windows = {}
        valid = 0 # 记录已经满足 needs 的字符数
        # 记录最小覆盖子串的起始索引及长度
        start=0
        length = 999999

        while right < len(s):
            incomingChar = s[right]
            right += 1
            # 更新 窗口 数据
            if needs.get(incomingChar):
                windows[incomingChar] = windows.get(incomingChar, 0) + 1
                currCharCount = windows.get(incomingChar)
                if currCharCount == needs.get(incomingChar):
                    valid += 1
            
            # 判断是否需要收缩窗口，不断收缩
            while valid >= len(needs):
                delettingChar = s[left]
                if needs.get(delettingChar):
                    if(right - left) < length:
                        length =  right - left
                        start = left
                    windows[delettingChar] = windows.get(delettingChar) - 1
                    if windows.get(delettingChar) < needs.get(delettingChar):
                        valid -= 1
                    
                left += 1
        
        return "" if length == 999999 else s[start:start+length]



s = ""
t = ""
# print(Solution().minWindow(s, t))

# [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needs = {}
        for ch in p:
            needs[ch] = needs.get(ch, 0) + 1
        window = {}
        left, right = 0, 0
        res = []
        valid = 0
        while right < len(s):
            incomingChar = s[right]
            # 需要修改窗口数据
            if needs.get(incomingChar, 0) > 0:
                window[incomingChar] = window.get(incomingChar, 0) + 1
                if window.get(incomingChar) == needs.get(incomingChar):
                    valid += 1
            right += 1
            # 这里判断窗口收缩的条件有更改，由于是要求子串，不是覆盖子串，所以长度必须保持一致
            while (right-left) >= len(p):
                if valid == len(needs):
                    res.append(left)
                deletingChar = s[left]
                if needs.get(deletingChar, 0) > 0:
                    if window.get(deletingChar, 0) == needs.get(deletingChar):
                        valid -= 1
                    window[deletingChar] = window.get(deletingChar, 0) - 1
                left += 1
        return res
    
s = "cbaebabacd"
p = "bcae"
# print(Solution().findAnagrams(s, p))

# [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = {}
        left, right = 0, 0
        while right < len(s):
            incomingChar = s[right]
            window[incomingChar] = window.get(incomingChar, 0) + 1
            right += 1
            while window.get(incomingChar) > 1:
                deletingChar = s[left]
                window[deletingChar] = window.get(deletingChar) - 1
                left += 1
            # 每次进来一个新字符，都收集下结果，第二个 while 确保窗口内无重复字符
            res = max(res, right - left)
        return res
s = "pwwkew"
# print(Solution().lengthOfLongestSubstring(s))


# [395. 至少有 K 个重复字符的最长子串](https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/)
# 不知道什么时候收缩窗口
# 当限定字符种类数目为 t 时，满足题意的最长子串，就一定出自某个 s[l...r]. 因此，在滑动窗口的维护过程中，就可以直接得到最长子串的大小。
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for t in range(1, 27): # 26 个字母
            left, right = 0, 0
            window = {}
            category = 0
            valid = 0
            while right < len(s):
                incoming = s[right]
                if window.get(incoming, 0) == 0:
                    category += 1
                window[incoming] = window.get(incoming, 0) + 1
                if window.get(incoming) == k:
                    valid += 1
                
                while category > t and left <= right:
                    # 此处收缩窗口
                    deleting = s[left]
                    if window.get(deleting) == k:
                        valid -= 1
                    window[deleting] = window[deleting] - 1
                    if window[deleting] == 0:
                        category -= 1
                    left += 1

                if valid == category:
                    res = max(res, right - left + 1)
                
                right += 1

        return res

s = "ababbc"
# print(Solution().longestSubstring(s, 2))

# [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/?favorite=2cktkvj)
# 找回文串的难点在于，回文串的的长度可能是奇数也可能是偶数，解决该问题的核心是从中心向两端扩散的双指针技巧。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.findPalindrom(s, i, i)
            s2 = self.findPalindrom(s, i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res

    def findPalindrom(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1: right]