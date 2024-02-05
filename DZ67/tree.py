class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node({self.value})'


class Tree:

    def __init__(self, root: Node):
        self.root = root

    def pre_order(self, node):
        if node is not None:
            print(node, end=" -> ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node, end=" -> ")
            self.in_order(node.right)

    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node, end=" -> ")

    def find_parent_by_value(self, node: Node, value: str):
        if node is None:
            return None

        if node.value == value:
            return node

        left_result = self.find_parent_by_value(node.left, value)
        right_result = self.find_parent_by_value(node.right, value)

        return left_result or right_result

    def __contains__(self, value: str):
        return self.find_parent_by_value(self.root, value) is not None


root = Node("A")
tree = Tree(root)


# left tree
tree.root.left = Node("B")
tree.root.left.left = Node("D")
tree.root.left.left.right = Node("I")
tree.root.left.right = Node("E")
tree.root.left.left.left = Node("H")

# right tree
tree.root.right = Node("C")
tree.root.right.left = Node("F")
tree.root.right.right = Node("G")
tree.root.right.right.left = Node("J")


# tree.pre_order(root)
# print()
# tree.in_order(root)
# print()
# tree.post_order(root)
# print()
print()
found_node = tree.find_parent_by_value(root, "N")
found_node2 = tree.find_parent_by_value(root, "F")
print(found_node)
print(found_node2)
print("E" in tree)

