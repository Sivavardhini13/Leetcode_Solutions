# Leetcode 237 : Delete Node in a Linked List
# Difficulty : Medium

class Solution:
    def deleteNode(self, node):
        node.val=node.next.val
        node.next=node.next.next