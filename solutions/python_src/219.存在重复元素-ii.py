#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from operator import truediv


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = {}
        for index in range(len(nums)):
            if nums[index] in num_index.keys() and index - num_index[nums[index]] <= k:
                return True
            else:
                num_index[nums[index]] = index

        return False
# @lc code=end
