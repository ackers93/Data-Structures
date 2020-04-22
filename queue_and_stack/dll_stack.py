from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # Adding an item onto the stack, first in, first out.
    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):  # Removing an item from off the top of the stack
        if self.storage.__len__() is 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):  # getting the length of items in a stack.
        return self.storage.__len__()
