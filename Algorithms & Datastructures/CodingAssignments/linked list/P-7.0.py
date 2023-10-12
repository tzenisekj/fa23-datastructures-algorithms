my_name = "Tyler Zenisek"
 
class Node:
    """
    This class represents a node in a singly linked list.
    Each node has a value and a reference to the next node in the list.
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None
 
class SinglyLinkedList:
 
    # Assignment: Programming Project, Chapter 7
 
    def __init__(self):
        self.head = None
        self.tail = None
 
    def add_head(self, e):
        """
        This function adds an element at the head of the list.
 
        Parameters:
        e (Any): The element to add.
 
        Returns:
        None
        """
        # WRITE YOUR CODE HERE
 
    def add_tail(self, e):
        """
        This function adds an element at the tail of the list.
 
        Parameters:
        e (Any): The element to add.
 
        Returns:
        None
        """
        # WRITE YOUR CODE HERE
 
    def find_3rd_to_last(self):
        """
        This function finds the third-to-last element in the list.
 
        Parameters:
        None
 
        Returns:
        Any: The third-to-last element in the list, or None if the list has fewer than three elements.
        """
        # WRITE YOUR CODE HERE
        return None
 
    def reverse(self):
        """
        This function reverses the list.
 
        Parameters:
        None
 
        Returns:
        None
        """
        # WRITE YOUR CODE HERE
 
if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.add_head(1)
    linked_list.add_tail(2)
    linked_list.add_tail(3)
    linked_list.add_tail(4)
    print(linked_list.find_3rd_to_last())  # 2
    linked_list.reverse()
    print(linked_list.find_3rd_to_last())  # 3