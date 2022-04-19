#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        same_count = 0
        result = nums[0]
        for num in nums:
            if result == num:
                same_count += 1
            else:
                if same_count == 0:
                    result = num
                    same_count += 1
                else:
                    same_count -= 1
        return result
# @lc code=end
