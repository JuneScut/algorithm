from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 【26】 [删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1


# solution = Solution()
# print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

# 【83】 [删除链表中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast:
            if slow.val != fast.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        if slow:
            slow.next = None
        return head


# solution = Solution()
# print(solution.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2)))))

# 【27】 [移除元素](https://leetcode.cn/problems/remove-element/)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


solution = Solution()
# print(solution.removeElement([3, 2, 2, 3], 3))

# 【283】 [移动零](https://leetcode.cn/problems/move-zeroes/)


class Solution:
    def removeElement(self, nums: List[int], val) -> int:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = self.removeElement(nums, 0)
        while p < len(nums):
            nums[p] = 0
            p += 1

# 【76】 [最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/)
# 滑动窗口


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        # need: 需要匹配的字符的计数
        for i in t:
            need[i] = need.get(i, 0) + 1
        valid = 0
        left, right = 0, 0
        start = 0
        curLen = 99999
        while right < len(s):
            c = s[right]  # 即将移入窗口的数据
            if need.get(c):
                # 如果属于需要匹配的字符，更新 window 个数以及 valid
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            right += 1

            # 判断左侧窗口是否需要收缩
            while valid == len(need):
                if right - left < curLen:
                    curLen = right - left
                    start = left
                d = s[left]  # 即将移出窗口的字符
                left += 1  # 缩小窗口
                # 更新 window 个数以及 valid
                if need.get(d):
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return "" if curLen == 99999 else s[start: start+curLen]


solution = Solution()
# print(solution.minWindow("ADOBECODEBANC", "ABC"))

# 【567】 [字符串的排列](https://leetcode.cn/problems/permutation-in-string/)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = {}, {}
        for i in s1:
            need[i] = need.get(i, 0) + 1
        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if need.get(c):
                window[c] = window.get(c, 0) + 1
                if need[c] == window[c]:
                    valid += 1
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if need.get(d):
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window[d] - 1
        return False


solution = Solution()
# print(solution.checkInclusion("ab", "eidbaooo"))

# 【438】 [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = {}, {}
        for i in p:
            need[i] = need.get(i, 0) + 1
        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if need.get(c):
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if need.get(d):
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res


solution = Solution()
# print(solution.findAnagrams("abab", "ab"))


# 【3】 [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = {}
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left)
        return res


solution = Solution()
# print(solution.lengthOfLongestSubstring("abcabcbb"))

# 【167】 [两数之和](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/)
# [剑指offer57]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                return [left+1, right+1]
            elif val < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            val = numbers[left] + numbers[right]
            if val == target:
                return [numbers[left], numbers[right]]
            elif val < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

# 【344】 [反转字符串](https://leetcode.cn/problems/reverse-string/)


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1


solution = Solution()
# print(solution.reverseString(["h", "e", "l", "l", "o"]))

# 【5】 [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/)
# 从中心向两端拓展的双指针


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i+1)
            i += 1
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res

    def palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


solution = Solution()
# print(solution.longestPalindrome("babad"))

# 【82】 [删除排序链表中的重复项II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        prev = dummy
        cur = prev.next
        while cur:
            fast = cur
            repeatNum = 0
            while fast and fast.val == cur.val:
                fast = fast.next
                repeatNum += 1
            if repeatNum > 1:
                prev.next = fast
            else:
                prev = cur
            cur = fast
        return dummy.next


solution = Solution()
# print(solution.deleteDuplicates(
#     ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(5)))))))

# 【剑指offer21】 [调整数组顺序使奇数位于偶数前面](https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/?show=1)


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] % 2 == 1:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow += 1
            fast += 1
        return nums

# 【1】 [两数之和](https://leetcode.cn/problems/two-sum/?show=1)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndex = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if valToIndex.get(need, -1) >= 0:
                return [valToIndex.get(need), i]
            valToIndex[nums[i]] = i
        return []


solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))

# 【80】 [删除有序数组中的重复项II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/?show=1)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        count = 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            elif slow < fast and count < 2:
                slow += 1
                nums[slow] = nums[fast]
            count += 1
            fast += 1
            if fast < len(nums) and nums[fast] != nums[fast-1]:
                count = 0
        return slow + 1


solution = Solution()
# print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))

# 【15】[三数之和](https://leetcode.cn/problems/3sum/)


class Solution:
    def twoSum(self, nums: List[int], start: int, target: int):
        left, right = start, len(nums)-1
        res = []
        while left < right:
            start = nums[left]
            end = nums[right]
            s = start + end
            if s == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == start:
                    left += 1
                while left < right and nums[right] == end:
                    right -= 1
            elif s < target:
                while left < right and nums[left] == start:
                    left += 1
            elif s > target:
                while left < right and nums[right] == end:
                    right -= 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i < n:
            twoSumRes = self.twoSum(nums, i+1, (-1)*nums[i])
            if twoSumRes:
                for val in twoSumRes:
                    val.insert(0, nums[i])
                    res.append(val)
            while i < (n-1) and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res


solution = Solution()
# print(solution.threeSum([1, 2, -2, -1]))

# 【209】[长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        n = len(nums)
        total = 0
        minLen = n+1
        while right < n:
            inNum = nums[right]
            right += 1
            total += inNum
            if total >= target:
                minLen = min(minLen, right-left)
            # 是否需要缩小窗口
            while total > target:
                outNum = nums[left]
                left += 1
                total -= outNum
                if total >= target:
                    minLen = min(minLen, right-left)

        return minLen if minLen <= n else 0


solution = Solution()
print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
