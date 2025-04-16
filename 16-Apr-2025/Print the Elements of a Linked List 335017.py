# Problem: Print the Elements of a Linked List - https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next