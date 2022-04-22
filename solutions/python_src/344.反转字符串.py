#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for index in range(len(s) // 2):
            exchange = s[index]
            s[index] = s[len(s) - index - 1]
            s[len(s) - index - 1] = exchange
# @lc code=end
