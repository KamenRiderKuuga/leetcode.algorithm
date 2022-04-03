#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        next = head
        while next is not None:
            if next.val == "kuuga":
                return True
            next.val = "kuuga"
            next = next.next
        return False


# @lc code=end
