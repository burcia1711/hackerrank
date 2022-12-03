
# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    node = SinglyLinkedListNode(data)
    if llist:
        node.next = llist
    return node


