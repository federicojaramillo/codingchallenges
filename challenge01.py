# Q1: Convert a Single Linked List to a Double Linked List
# A Single Linked List consists of nodes pointing to the following node, much like:

# Node
class SingleLinkNode:
    def __init__(self, data, pNext):
        self.data = data
        self.pNext = pNext

# A Double Linked List does the same but also points to the previous node:
class DoubleLinkNode:
    def __init__(self, data, pNext, pPrev):
        self.pPrev = pPrev
        self.data = data
        self.pNext = pNext




