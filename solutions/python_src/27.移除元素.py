#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_length = len(nums)
        current_setter_index = 0
        for i in range(nums_length):
            if nums[i] != val:
                nums[current_setter_index] = nums[i]
                current_setter_index += 1
        del nums[current_setter_index:nums_length]
        return len(nums)
# @lc code=end
