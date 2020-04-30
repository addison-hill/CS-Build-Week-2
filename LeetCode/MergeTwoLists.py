"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Understand - merge two linked lists together into a new linked list that is sorted
# Plan -    Create a empty linked list
#           while loop that loops through l1 and l2
#           take the lesser value and put in new linked list...this will make it sorted
#           iterate to next node and repeat until finished


# def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         head = ListNode(None)
#         l3 = head
#         while l1 and l2:
# 			if l1.val < l2.val:
# 				head.next = l1
#                 l1 = l1.next
# 			else:
# 				head.next = l2
#                 l2 = l2.next
#             head = head.next
#         head.next = l1 if l1 else l2
#         return l3.next
