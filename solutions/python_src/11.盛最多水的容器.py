#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        len_height = len(height)
        result = 0
        left_index = 0
        right_index = len_height - 1
        while left_index < right_index:
            result = max((right_index - left_index) *
                        min(height[left_index], height[right_index]), result)
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
        return result
# @lc code=end

