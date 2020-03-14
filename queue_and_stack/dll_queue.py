import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# FIFO
class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList

    def enqueue(self, value):
        # place in queue
        self.storage.add_to_tail(value)

        self.size += 1

    def dequeue(self):
        # delete from queue
        if self.len() > 0:
            value = self.storage.remove_from_head()

            self.size -= 1

            return value

        else:
            print("The queue is empty.")

    def len(self):
        # what is the length of queue
        return self.size
