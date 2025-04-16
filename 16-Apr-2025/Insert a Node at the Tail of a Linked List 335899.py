# Problem: Insert a Node at the Tail of a Linked List - https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

def insertNodeAtTail(head, data):
    newNode =  SinglyLinkedListNode(data)
    curr = head
    if curr is None:
        curr = newNode
        return newNode
    while curr.next:
        curr = curr.next
    curr.next = newNode
    return head
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
