
def second_to_last(self):
    if self._size > 1:
        node = self._head
        while node.next.next != None:
                node = node.next

        return node