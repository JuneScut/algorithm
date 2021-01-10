# 7 整数反转
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         ans = 0
#         absX = abs(x)
#         while (absX !=0):
#             pop = int(absX%10)
#             ans = ans * 10 + pop
#             absX = int(absX/10)
#         if x<0:
#             ans = -ans
#         return  ans if -2147483648 < ans < 2147483647 else 0

# solution = Solution()
# print(solution.reverse(-120))

# 最长公共前缀
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strsLen = len(strs)
        if strsLen == 0:
            return ""
        if strsLen == 1:
            return strs[0]

        def findCommon(str1, str2):
            common = ""
            l1 = len(str1)
            l2 = len(str2)
            list1 = list(str1)
            list2 = list(str2)
            if (l1 == 0 or l2 == 0):
                return common
            else:
                index = 0
                minL = min(l1, l2)
                while index < minL:
                    if (list1[index] == list2[index]):
                        common += list1[index]
                        index = index + 1
                    else:
                        break
                return common
        common = strs[0]
        for index in range(1, strsLen):
            common = findCommon(common, strs[index])
            if  common == "":
                break
        return common
                

solution = Solution()
print(solution.longestCommonPrefix(["ab", "a"]))