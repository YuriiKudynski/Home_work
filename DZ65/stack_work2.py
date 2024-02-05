class Stack:

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            return None


def check_brackets(inputs):
    stack = Stack()
    for item in inputs:
        if item in "(":
            stack.push(item)
        elif item in ")":
            if stack.is_empty():
                return False
            top_item = stack.pop()
            if item == ")" and top_item != "(":
                return False
    return stack.is_empty()


print(check_brackets("((()))"))
print(check_brackets("((()))"))
print(check_brackets("(()()())"))
print(check_brackets("((())"))
print(check_brackets("())("))

