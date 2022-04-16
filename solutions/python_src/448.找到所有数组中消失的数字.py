#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            nums[abs(nums[index]) - 1] = -abs(nums[abs(nums[index]) - 1])
        result = []
        for index in range(len(nums)):
            if nums[index] > 0:
                result.append(index + 1)
        return result
# @lc code=end
