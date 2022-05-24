#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        current_sum = 0
        for num in nums:
            current_sum += num
        return int((1 + len(nums)) * len(nums) / 2) - current_sum
# @lc code=end
