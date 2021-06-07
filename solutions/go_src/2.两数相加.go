package main

import "fmt"

/*
 * @lc app=leetcode.cn id=2 lang=golang
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	firstList := new(ListNode)
	firstList.Val = 2
	firstList.Next = new(ListNode)
	nextList := firstList.Next
	nextList.Val = 4
	nextList.Next = new(ListNode)
	nextList = nextList.Next
	nextList.Val = 3

	secondList := new(ListNode)
	secondList.Val = 5
	secondList.Next = new(ListNode)
	nextList = secondList.Next
	nextList.Val = 6
	nextList.Next = new(ListNode)
	nextList = nextList.Next
	nextList.Val = 4

	addTwoNumbers(firstList, secondList)
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	firstNode := new(ListNode)
	nextNode := firstNode.Next
	// plusOne := false

	for l1 != nil {
		nextNode = l1
		nextNode.Next = l1.Next
		l1 = l1.Next
	}

	printList(nextNode)

	return nil
}

func printList(node *ListNode) {
	fmt.Printf("[")
	for node.Next != nil {
		fmt.Printf("%d,", node.Val)
		node = node.Next
	}

	fmt.Printf("%d", node.Val)

	fmt.Printf("]\n")
}

// @lc code=end
