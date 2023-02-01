from typing import List

# 滑动窗口算法，利用左右指针维护窗口中的数据，窗口区间是左闭右开区间，[left,right)。

# 滑动窗口算法通用流程：

# 初始化：初始化左右指针，left, right = 0, 0；初始化窗口window={}，最初时window不包含数据；
# 寻找可行解：不断扩大窗口的右边界，右指针right+=1，将新数据加入窗口，并检测此时窗口中的字串是否满足题目要求；
# 优化可行解：当窗口包含的字串满足题目要求时，开始收缩窗口的左边界，left+=1，直至不再满足题目要求；
# 滑动窗口过程中，注意数据的实时更新，找到保存结果的位置。

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口
        need, window = {}, {}
        for c in t:
            need[c] = need.setdefault(c, 0) + 1    # need = {字符:出现次数}
        
        left, right = 0, 0
        valid = 0     # 验证window是否满足need条件，valid表示满足条件的字符个数
        start, length = 0, len(s)+1
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:         # 更新窗口数据
                window[c] = window.setdefault(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left < length:   # 优化结果
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:     # 更新窗口数据
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return s[start:start+length] if length != len(s)+1 else ''

solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))