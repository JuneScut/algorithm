from typing import List

# [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/?favorite=2cktkvj)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            key = self.encode(word)
            if map.get(key):
                map[key].append(word)
            else:
                map[key] = [word]
        res = []
        for value in map.values():
            res.append(value)
        return res
    def encode(self, word: str) -> str:
        # arr = [0] * 26
        # for ch in word:
        #     arr[ord(ch)-ord('a')] += 1
        # # 个数超过 10 的话，这种 encoding 方式有问题
        # arr = [str(i) for i in arr]
        # return ''.join(arr)
        map = {}
        for ch in word:
            map[ch] = map.get(ch, 0) + 1
        keys = sorted(map.keys())
        ret = ""
        for key in keys:
            ret = ret + key + str(map[key])
        return ret

print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Solution().encode("bat")