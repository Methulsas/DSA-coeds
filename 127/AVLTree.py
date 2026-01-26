

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0   # leaf node height = 0

    # Balance Factor = height(left) - height(right)
    def get_balance_factor(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        return left_height - right_height

    # Update node height
    def update_height(self):
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = max(left_height, right_height) + 1


class AVLTree:
    def __init__(self):
        self.root = None

    # ---------------- Rotations ----------------
    def _rotateRight(self, y):
        x = y.left
        T2 = x.right

        # Rotation
        x.right = y
        y.left = T2

        # Update heights
        y.update_height()
        x.update_height()

        return x

    def _rotateLeft(self, x):
        y = x.right
        T2 = y.left

        # Rotation
        y.left = x
        x.right = T2

        # Update heights
        x.update_height()
        y.update_height()

        return y

    # ---------------- Balancing ----------------
    def _balance(self, node):
        if not node:
            return None

        node.update_height()
        bf = node.get_balance_factor()

        # Left Heavy
        if bf > 1:
            if node.left and node.left.get_balance_factor() < 0:
                node.left = self._rotateLeft(node.left)   # LR case
            return self._rotateRight(node)                 # LL case

        # Right Heavy
        if bf < -1:
            if node.right and node.right.get_balance_factor() > 0:
                node.right = self._rotateRight(node.right) # RL case
            return self._rotateLeft(node)                  # RR case

        return node

    # ---------------- Insertion ----------------
    def _insert(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node  # No duplicates allowed

        return self._balance(node)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    # ---------------- Deletion ----------------
    def getMin(self, node):
        while node.left:
            node = node.left
        return node

    def _delete(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Two children
            successor = self.getMin(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)

        return self._balance(node)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    # ---------------- Search ----------------
    def _search(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    # ---------------- Traversal ----------------
    def _preOrder(self, node):
        if not node:
            return []
        return [node.value] + self._preOrder(node.left) + self._preOrder(node.right)

    def __str__(self):
        return "Preorder: " + str(self._preOrder(self.root))


# =================== TEST ===================
if __name__ == "__main__":
    tree = AVLTree()

    values = [10, 20, 30, 40, 50, 25]

    for v in values:
        tree.insert(v)

    print(tree)  # Balanced AVL Tree

    print("Search 25:", "Found" if tree.search(25) else "Not Found")
    print("Search 75:", "Found" if tree.search(75) else "Not Found")

    tree.delete(40)
    print(tree)

    tree.insert(28)
    print(tree)

    tree.delete(25)
    print(tree)

    tree.insert(60)
    print(tree)

    tree.delete(60)
    print(tree)

    tree.insert(55)
    print(tree)

    tree.delete(10)
    print(tree)

    tree.delete(20)
    print(tree)

    tree.delete(55)
    print(tree)
