class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def max_value(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.val


def min_value(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.val


def sum_values(root):
    if root is None:
        return 0
    return root.val + sum_values(root.left) + sum_values(root.right)


def main():
    # Test
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    max = max_value(root)
    print("Max value:", max)
    min = min_value(root)
    print("Min value:", min)
    sum = sum_values(root)
    print("Sum:", sum)


if __name__ == "__main__":
    main()
