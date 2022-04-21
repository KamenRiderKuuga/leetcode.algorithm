#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next

        first_node = head
        previous_head = head

        while head is not None:
            if head.val == val:
                if head.next is None:
                    previous_head.next = None
                else:
                    previous_head.next = head.next
                head = previous_head.next
            else:
                previous_head = head
                head = head.next

        return first_node
# @lc code=end
