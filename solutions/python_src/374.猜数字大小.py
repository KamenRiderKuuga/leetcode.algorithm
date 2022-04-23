#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                hi = mid - 1
            elif result == 1:
                lo = mid + 1

        return -1
# @lc code=end
