#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        for index in range(0, len(nums)):
            current_num = nums[index]
            diff = target - current_num
            if diff in nums_index:
                return [nums_index[diff], index]
            else:
                nums_index[current_num] = index
# @lc code=end
