class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def insert_after(self, prev_data, new_data):
        new_node = Node(new_data)
        current_node = self.head
        while current_node:
            if current_node.data == prev_data:
                new_node.next_node = current_node.next_node
                current_node.next_node = new_node
                return
            current_node = current_node.next_node

    def del_last(self):
        if not self.head or not self.head.next_node:
            # Якщо список пустий або містить лише один елемент
            self.head = None
            return

        current_node = self.head
        while current_node.next_node.next_node:
            current_node = current_node.next_node

        current_node.next_node = None

    def del_first(self):
        if not self.head:
            return

        self.head = self.head.next_node

    def replace_value(self, old_value, new_value, replace_all=False):
        current_node = self.head

        while current_node:
            if current_node.data == old_value:
                current_node.data = new_value

                if not replace_all:
                    return

            current_node = current_node.next_node

    @property
    def size(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next_node

        return count

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")


def menu():
    linked_list = LinkedList()

    while True:
        print("\nMenu:"
              "\n1. Додати елемент у хвіст списку."
              "\n2. Додати елемент до списку на початок."
              "\n3. Вставити елемент в середину списку."
              "\n4. Видалити елемент з хвоста."
              "\n5. Видалити елемент з початку."
              "\n6. Видалити елемент в середині по значенню."
              "\n7. Замінити значення."
              "\n8. Розмір списку."
              "\n9. Показати вміст списку."
              "\n10. Вихід")

        choice = int(input("Виберіть пункт меню: "))
        if choice == 1:
            data = input("Введіть значення: ")
            linked_list.append(data)
            print(f"У хвіст списку додано елемент з значенням {data}")
        elif choice == 2:
            data = input("Введіть значення: ")
            linked_list.prepend(data)
            print(f"На початок списка додано елемент з значенням {data}")
        elif choice == 3:
            prev_data = input("Введіть значення після якого вставити елемент: ")
            new_data = input("Введіть нове значення: ")
            linked_list.insert_after(prev_data, new_data)
            print(f"У список додано елемент з значенням {data} після {prev_data}")
        elif choice == 4:
            linked_list.del_last()
            print("Останній елемент списку видалено!")
        elif choice == 5:
            linked_list.del_first()
            print("Перший елемент списку видалено!")
        elif choice == 6:
            pass
            print("На стадії розробки!")
        elif choice == 7:
            prev_data = input("Введіть значення для заміни: ")
            new_data = input("Введіть нове значення для заміни: ")
            menu_choice = input("Введіть 1 якщо заміна 1 елемента. 2 якщо всі елементи: ")
            if menu_choice == 1:
                linked_list.replace_value(prev_data, new_data, replace_all=False)
            elif menu_choice == 2:
                linked_list.replace_value(prev_data, new_data, replace_all=True)
            print("Заміна успішна!")
        elif choice == 8:
            print(f'Розмір списку: {linked_list.size}')
        elif choice == 9:
            linked_list.display()
        elif choice == 10:
            print("Дякуємо за користування програмою!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    menu()
