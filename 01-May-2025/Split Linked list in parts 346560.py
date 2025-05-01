# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        len_ = 0 
        while current:
            len_ += 1
            current = current.next
        
        min_len = len_ // k
        add_one = len_ % k
        

        res = []
        
        curr = head
        created_cnt = 0
        while created_cnt < k:
            cnt = 0
            innerNode = ListNode(0)
            inner_ptr = innerNode
            if add_one > 0:
                while curr and cnt < min_len +1:
                    inner_ptr.next = curr
                    inner_ptr = inner_ptr.next
                    curr = curr.next
                    cnt += 1
                inner_ptr.next = None
                add_one -= 1
            else:
                while curr and cnt < min_len:
                    inner_ptr.next = curr
                    inner_ptr = inner_ptr.next
                    curr = curr.next
                    cnt += 1
                inner_ptr.next = None

            res.append(innerNode.next)
            created_cnt += 1
        return res