import math

# 69. x 的平方根
# 左闭右闭
class Solution:
    def mySqrt(self, x: int) -> int:
        # return math.floor(math.sqrt(x))
        if x == 0:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = math.floor(left + (right - left) / 2)
            sqrt = math.floor( x / mid)
            if sqrt == mid:
                return mid
            elif sqrt > mid:
                left = mid + 1
            else:
                right = mid -1

        return right


solution = Solution()
print(solution.mySqrt(16))