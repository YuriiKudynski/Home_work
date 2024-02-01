class Node:

    def __init__(self, data, prev=None):
        self.next = None
        self.prev = prev
        self.data = data


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def del_from_head(self):
        if self.head is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def del_from_tail(self):
        if self.tail is None:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def remove_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def add_with_index(self, index, value):
        new_node = Node(value)
        if index == 1:
            self.add_to_head(value)
        else:
            current = self.get_node_at_index(index - 1)
            if current:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
            else:
                print("Invalid index. Element not added.")

    def get_node_at_index(self, index):
        current = self.head
        current_index = 1
        while current_index < index and current:
            current = current.next
            current_index += 1
        return current

    def display_after_head(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

    def display_from_tail(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("Null")

    def clear_list(self):
        self.head = None
        print("Очищено!")


d_linked_list = DoubleLinkedList()
d_linked_list.add_to_head(1)
d_linked_list.add_to_tail(2)
d_linked_list.add_to_head(0)
d_linked_list.add_to_tail(4)
d_linked_list.add_with_index(4, 3)
print("З голови: ")
d_linked_list.display_after_head()
print("З хвоста: ")
d_linked_list.display_from_tail()
d_linked_list.clear_list()
d_linked_list.display_after_head()