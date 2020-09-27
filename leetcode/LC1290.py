class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Node) -> int:
        num = head.val
        while head.next:
            num = num << 1
            num = num | head.next.val
            head = head.next
        return num