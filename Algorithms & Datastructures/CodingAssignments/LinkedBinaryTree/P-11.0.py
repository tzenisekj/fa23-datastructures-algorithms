import queue
 
 
class LinkedBinaryTree:
    class _Node:
        __slots__ = '_element', '_left', '_right'
 
 
        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._left = left
            self._right = right


    def __init__(self):
        self._root = None
        self._size = 0
 
 
    def __len__(self):
        return self._size
 
 
    def height(self):
        return self._height(self._root)
 
 
    def _height(self, p):
        if not p:
            return 0
        return 1 + max(self._height(p._left), self._height(p._right))
 
 
 
    def in_order(self):
        for e in self._in_order(self._root):
            yield e
 
 
    def _in_order(self, p):
        if p is not None:
            for other in self._in_order(p._left):
                yield other
 
 
            yield p._element
            for other in self._in_order(p._right):
                yield other
 
 
 
    def pre_order(self):
        for e in self._pre_order(self._root):
            yield e
 
 
    def _pre_order(self, p):
        if p:
            yield p._element
            for other in self._pre_order(p._left):
                yield other
 
 
            for other in self._pre_order(p._right):
                yield other
 
 
    def post_order(self):
        for e in self._post_order(self._root):
            yield e
 
 
    def _post_order(self, p):
        if p:
            for other in self._post_order(p._left):
                yield other
 
 
            for other in self._post_order(p._right):
                yield other
 
 
            yield p._element
 
 
    def breadth_first(self):
        q = queue.Queue()
        q.put(self._root)
        while not q.empty():
            p = q.get()
            print(p._element)
            if p._left:
                q.put(p._left)
            if p._right:
                q.put(p._right)
 
 
    def bst_insert(self, key):
        '''implement binary search tree insert algoritm'''
        if self._root is None:
            self._root = self._Node(key)
            self._size += 1
            return

        self._bst_insert(self._root, key)

    def _bst_insert(self, n, key):
        '''Helper Function to insert new key into tree'''
        if n._element <= key:
            if n._right is None:
                n._right = self._Node(key)
                self._size += 1
            else:
                self._bst_insert(n._right, key)
        else:
            if n._left is None:
                n._left = self._Node(key)
                self._size += 1
            else:
                self._bst_insert(n._left, key)

    def bst_search(self, key):
        '''implement binary search algorithm'''
        if self._root is None:
            return False

        n = self._root
        while n is not None:
            if n._element == key:
                return True
            else:
                if n._element > key:
                    n = n._left
                else:
                    n = n._right

        return False

    def print_in_order(self):
        '''implement print in order'''
        print(list(self.in_order()))


if __name__ == "__main__":
    bst = LinkedBinaryTree()
    print("Current Size of Tree: ", len(bst))
    bst.print_in_order()

    print("Inserting 8...")
    bst.bst_insert(8)
    print("Current Size of Tree: ", len(bst))
    bst.print_in_order()

    print("Inserting 20...")
    bst.bst_insert(20)
    print("Current Size of Tree: ", len(bst))
    bst.print_in_order()

    print("Inserting 4...")
    bst.bst_insert(4)
    print("Current Size of Tree: ", len(bst))
    bst.print_in_order()

    print("Inserting 5...")
    bst.bst_insert(5)
    print("Current Size of Tree: ", len(bst))
    bst.print_in_order()

    print("Inserting 5...")
    bst.bst_insert(5)
    print("Current Size of Tree: ", len(bst))
    bst.print_in_order()

    print("Inserting 5...")
    bst.bst_insert(5)
    print("Current Size of Tree: ", len(bst))
    bst.print_in_order()

    print("Inserting 6...")
    bst.bst_insert(6)
    print("Current Size of Tree: ", len(bst))
    bst.print_in_order()

    print("Searching for 8: ", bst.bst_search(8))
    print("Searching for 200: ", bst.bst_search(200))


