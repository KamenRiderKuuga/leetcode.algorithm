#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre_node = None
        while head is not None:
            next_node = head.next
            head.next = pre_node
            pre_node = head
            head = next_node

        return pre_node
# @lc code=end

