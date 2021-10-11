#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre_val = -101
        result = head
        current_node = head
        while current_node is not None:
            if current_node.val != pre_val:
                if pre_val != -101:
                    result.next = current_node
                result = current_node
            pre_val = current_node.val
            current_node = current_node.next
        
        if result is not None and result.next is not None:
            result.next = None

        return head
# @lc code=end

