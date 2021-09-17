#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        first_node = result
        firstNode = l1
        secondNode = l2
        while True:
            first_value = 101
            second_value = 101
            if firstNode is not None:
                first_value = firstNode.val
            if secondNode is not None:
                second_value = secondNode.val
            
            current_value = min(first_value, second_value)
            if current_value == 101:
                break
    
            if current_value == first_value:
                firstNode = firstNode.next
            else:
                secondNode = secondNode.next
            
            result.next = ListNode()                 
            result = result.next
            result.val = current_value
        return first_node.next        
# @lc code=end

