class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.value


def solution(node):
    temp = None
    current = node
    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    if temp is not None:
        head = temp.prev

    return head
