# [20. 有效的括号](https://leetcode.cn/problems/valid-parentheses/?favorite=2cktkvj)
class Solution:
    # 遇到左括号入栈，遇到右括号查找栈顶元素是否匹配
    def isValid(self, s: str) -> bool:
        left = []
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                left.append(ch)
            else:
                if left and self.findLeft(ch)  == left[len(left)-1]:
                    left.pop()
                else:
                    return False
        return not left

    def findLeft(self, ch: str):
        if ch == ')':
            return '('
        if ch == ']':
            return '['
        if ch == '}':
            return '{'
        
s = ")"
print(Solution().isValid(s))