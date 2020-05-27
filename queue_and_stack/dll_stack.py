# import sys
# sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

# FILO = LIFO
class Stack:
    def __init__(self): 
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size +=1

    def pop(self):
        
        if self.size > 0:
            value = self.storage.remove_from_head()
            
            self.size -=1
            
            return value

        else:
            print("The stack is empty.")

    def len(self):
        return self.size
