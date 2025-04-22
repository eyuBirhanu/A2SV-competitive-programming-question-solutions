# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr = l1
        l2_ptr = l2 
        list1 = []
        list2 = []
        while l1_ptr or l2_ptr:
            if l1_ptr:
                list1.append(l1_ptr.val)
                l1_ptr = l1_ptr.next
            if l2_ptr:
                list2.append(l2_ptr.val)
                l2_ptr = l2_ptr.next 
        list1 = list1[::-1]
        list2 = list2[::-1]
        len_ = abs(len(list1) - len(list2))
        if len(list1) < len(list2):
            list1 = list1 + ([0] * len_)
        if len(list2) < len(list1):
            list2 = list2 + ([0] * len_)

        i = 0
        j = 0
        res = []
        rem = 0
        while i < len(list1):
            sum_ = list1[i] + list2[j] + rem
            if sum_ >= 10:
                ones = sum_ % 10
                rem = sum_ // 10
                res.append(ones)
            else:
                res.append(sum_)
                rem = 0
            
            i += 1
            j += 1
        if rem > 0:
            res.append(rem)
        
        dummy = None
        node = ListNode(res[0])
        node.next = dummy
        for i in range(1, len(res)):
            new_node = ListNode(res[i])
            new_node.next = node
            node =new_node
        return node
