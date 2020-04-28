"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Iteratively - traverse linked lists while adding values together and creating a new linked list with sum
# if sum > 10 you have to carry over to next and update sum

# convert values to string and reverse order, convert to int and add.
# then convert back to string and insert into linked list

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        string1 = ''
        string2 = ''
        while l1:
            # convert values to a string
            string1 += str(l1.val)
            l1 = l1.next
        while l2:
            string2 += str(l2.val)
            l2 = l2.next
        # convert from string to int and reverse order
        int1 = int(string1[::-1])
        int2 = int(string2[::-1])
        # Add both linkedlists, convert back to string
        result_str = str(int1 + int2)[::-1]
        # Build linked list out of the result string
        result_ll = ListNode(result_str[0])
        # Set pointer to head
        current_node = result_ll
        for i in range(1, len(result_str)):
            # Add new node with value at i
            current_node.next = ListNode(result_str[i])
            current_node = current_node.next

        return result_ll
