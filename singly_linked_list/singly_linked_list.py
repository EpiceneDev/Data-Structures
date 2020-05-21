class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        
    # def insert_before(self, value):
    #     current_prev = self.prev
    #     self.prev = ListNode(value, current_prev, self)

    def delete(self):
        pass

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = Node(value, self.head)
        self.head = node

    def test_contains(self):
        pass

    def add_to_tail(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return

    def remove_head(self):
        pass

    def test_get_max(self):
        pass


    # def print(self):
    #     if self.head is None:
    #         print("List is empty")
    #         return
        
    #     here = self.head
    #     llstr = ''

    #     while here:
    #         llstr += str(here.data) + '-->'
    #         here = here.next
