class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self, max_size=-1):
        self.head = None
        self.max_size = max_size

    def push(self, data):
        new_node = Node(data)
        if self.max_size == 0:
            raise Exception("Stack is overflow")

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node
        self.max_size -= 1

    def pop(self):
        if self.head is not None:
            old_head = self.head
            self.head = self.head.next
            self.max_size += 1
            return old_head.data
        raise Exception("Stack is empty")

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head is not None:
            return self.head.data
        raise Exception("Stack is empty")

    def is_full(self):
        return self.max_size == 0

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    @property
    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def clear(self):
        self.head = None
        print("Стек очищено!")


if __name__ == "__main__":
    stack = Stack(max_size=3)

    while True:
        print("\nMenu"
              "\n1. Push"
              "\n2. Pop"
              "\n3. Is empty"
              "\n4. Is full"
              "\n5. Size"
              "\n6. Clear"
              "\n7. Peek"
              "\n8. Display"
              "\n9. Exit")

        choice = int(input("Enter option: "))
        if choice == 1:
            data = int(input("Enter value: "))
            stack.push(data)
        elif choice == 2:
            stack.pop()
            print("Value deleted!")
        elif choice == 3:
            if stack.is_empty():
                print("Stack is empty!")
            else:
                print("Stack is not empty!")
        elif choice == 4:
            if stack.is_full():
                print("Stack is full!")
            else:
                print("Stack is not full!")
        elif choice == 5:
            print(f"Size = {stack.size}")
        elif choice == 6:
            stack.clear()
        elif choice == 7:
            print(stack.peek())
        elif choice == 8:
            stack.display()
        elif choice == 9:
            print("Thanks for using program!")
            break
        else:
            print("Incorrect option. Try again!")
