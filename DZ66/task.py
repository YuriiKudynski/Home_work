class Task:

    def __init__(self, task_id, name, priority=None):
        self.next = None
        self.task_id = task_id
        self.name = name
        self.priority = priority

    def __str__(self):
        return f'Task №{self.task_id}: {self.name}; priority:{self.priority}'


class Queue:

    def __init__(self):
        self.head = None
        self.size_value = 0
        self.completed_task_size_value = 0

    def enqueue(self, task_id, name, priority):
        new_task = Task(task_id, name, priority)

        if not self.head or priority < self.head.priority:
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next and priority >= current.next.priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task

        self.size_value += 1

    def dequeue(self):
        if not self.is_empty():
            removed_task = self.head
            self.head = self.head.next
            removed_task.next = None
            self.size_value -= 1
            self.completed_task_size_value += 1
            return removed_task
        else:
            return None

    def is_empty(self):
        return self.size_value == 0

    @property
    def size(self):
        return self.size_value

    @property
    def completed_tasks_count(self):
        return self.completed_task_size_value


queue = Queue()
queue.enqueue(1, "Підготувати звіт про продажі", 3)
queue.enqueue(2, "Відправити заказ клієнту A", 1)
queue.enqueue(3, "Сформувати презентацію для команди", 3)
queue.enqueue(4, "Зателефонувати постачальнику щодо поставки товару", 2)
queue.enqueue(5, "Відправити заказ клієнту B", 1)
queue.enqueue(6, "Замовити нове обладнання для офісу.", 2)

print("Size is ", queue.size)
print("Completed task: ", queue.completed_tasks_count)
print(queue.dequeue())
print(queue.dequeue())
print("Completed task: ", queue.completed_tasks_count)
print("Size is ", queue.size)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print("Completed task: ", queue.completed_tasks_count)
print(queue.dequeue())
print("Size is ", queue.size)
print("Is empty? ", queue.is_empty())
