# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = '' 
        list2 = ''

        # convert the linked listes to array 

        while l1:
            list1 += str(l1.val)
            l1 = l1.next
        while l2:
            list2 += str(l2.val)
            l2 = l2.next
        zeros = 0
        smaller = False

        # make them equal in length 

        if len(list1) < len(list2):
            zeros = len(list2) - len(list1) 
            smaller = True
        elif len(list2) < len(list1):
            zeros = len(list1) - len(list2)
        if smaller:
            list1 = list1 + (zeros * '0') 
        else:
            list2 = list2 + (zeros * '0') 
        list1 = list(map(int, list1))
        list2 = list(map(int, list2)) 

        # add them using long addition method

        i = 0
        res = []
        rem = 0
        while i < len(list1):
            sum_ = list1[i] + list2[i] + rem
            if sum_ >= 10:
                str_ = str(sum_)
                ones = sum_ % 10
                rem = sum_ // 10
                res.append(ones)
            else:
                res.append(sum_)
                rem = 0
            i += 1
        if rem > 0:
            res.append(rem)

        # change the array to linked list 
        
        if not res:
            return None

        head = ListNode(res[0])
        curr = head
        for value in res[1:]:
            curr.next = ListNode(value)
            curr = curr.next
        return head
        