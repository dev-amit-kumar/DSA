"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dict = {}
        if not head:
            return None 
        temp = head
        while temp:
            dict[temp] = Node(temp.val, None , None )
            temp = temp.next
        temp = head
        while temp:
            if temp.next:
                dict[temp].next = dict.get(temp.next)
            if temp.random:
                dict[temp].random = dict.get(temp.random)
            temp = temp.next
        return dict.get(head) 