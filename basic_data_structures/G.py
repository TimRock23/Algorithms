class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution(node, elem):
    index = 0
    while node.next_item is not None:
        if node.value == elem:
            return index
        node = node.next_item
        index += 1
    return '-1'
