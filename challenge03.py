# Q3: Detect if a List is Cyclic using Hash Table

# Loop through the list, adding the visited nodes to the hash table, if the visited node is already on the hash table it means it Cyclic

def isCyclic(head):
    node = head 
    visitedNodes = { node }