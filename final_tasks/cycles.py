def hasCycle(head):
    rabbit = head
    turtle = head

    while True:
        if (turtle.next is None or rabbit.next is None or
                rabbit.next.next is None):
            return False
        turtle = turtle.next
        rabbit = rabbit.next.next

        if turtle is rabbit:
            return True
