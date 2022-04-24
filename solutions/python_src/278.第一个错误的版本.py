#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        lo = 1
        hi = n
        mid = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    hi = mid - 1
            else:
                lo = mid + 1

# @lc code=end
