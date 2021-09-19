#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_len = len(nums)
        started = False
        previous_num = 0
        current_setter_index = 0
        for index in range(nums_len):
            if started:
                if nums[index] != previous_num:
                    previous_num = nums[index]
                    nums[current_setter_index] = previous_num
                    current_setter_index += 1
                continue

            previous_num = nums[index]
            started = True
            current_setter_index += 1

        current_setter_index -= 1
        del nums[current_setter_index + 1: nums_len]
        return len(nums)


# @lc code=end
