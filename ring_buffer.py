
import sys

sys.path.append('./doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

# a ring buffer is a type of queue: FIFO
# stores in fixed size array
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity # size of buffer
        self.current_pointer = None # used for temp storage
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if buffer is empty, add item to head and set current_pointer as head
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current_pointer = self.storage.head

        # if self.current is the head and buffer is full
        elif self.storage.length == self.capacity and self.current_pointer is self.storage.head:
            # remove from head
            self.storage.remove_from_head()
            # add item to tail
            self.storage.add_to_tail(item)
            # set item at tail as current item
            self.current_pointer = self.storage.tail

        # if buffer full and pointer not at head --no need to move pointer
        elif self.storage.length == self.capacity and self.current is not self.storage.head:
            
            self.storage.remove_from_head()

            self.storage.add_to_tail(item)

        # if buffer not full then add to tail
        else:
            self.storage.add_to_tail(item)

        
    def get(self):
        list_buffer_contents = []

        # If not all ring buffer's content is in the list_buffer_contents
        while self.storage.length != len(list_buffer_contents):

            # add the current value in storage to the list
            list_buffer_contents.append(self.current_pointer.value)

            # if there is another item, set current pointer to it and add to list
            if self.current.next:
                self.current = self.current.next

            # when down to the last item with no next...
            else:
                self.current = self.storage.head

        return list_buffer_contents