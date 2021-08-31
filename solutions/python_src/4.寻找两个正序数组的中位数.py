#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
from typing import List
import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_nums = [0] * (len(nums1) + len(nums2))
        index = 0
        for item in nums1:
            all_nums[index] = item
            index += 1
        for item in nums2:
            all_nums[index] = item
            index += 1
        # 复数，取中间两个数求平均值
        all_nums_count = len(all_nums)
        all_nums.sort()
        if all_nums_count % 2 == 0:
            return (all_nums[int(all_nums_count/2)-1] + all_nums[int(all_nums_count/2)])/2
        else:
            return all_nums[math.floor(all_nums_count/2)]
# @lc code=end
