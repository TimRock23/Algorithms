class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


def solution(node, idx):
    head = node
    index = 0
    prev_node = None
    while index != idx:
        index += 1
        prev_node = node
        node = node.next_item

    if prev_node:
        tmp = node.next_item
        prev_node.next_item = tmp
    else:
        head = node.next_item
        del node

    return head
