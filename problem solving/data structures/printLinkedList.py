
# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if (head == None):
        head = SinglyLinkedListNode(data)
    else:
        current = head
        whil e(current.next != None):
            current = current.next
        current.nex t =SinglyLinkedListNode(data)
    return head


