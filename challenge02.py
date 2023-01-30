# Q2: Convert a Single Linked List to Circular Linked List

# To convert a Single Linked List to Circular Linked List the last (tail) node must point to head of the list,
# which is only possible on Linked Lists with more than one element since a one element list would only point to itself (not circular)

# Node
class SingleLinkNode:
    def __init__(self, data, pNext):
        self.data = data
        self.pNext = pNext

# Convert to circular linked list
def convertToCirular(head):
    # declare node youre on, you start at head and want to find the last one
    node = head
    # find last node
    while( node.pNext != None ):
        node = node.pNext
    # link last node to head
    node.pNext = head
    return head



