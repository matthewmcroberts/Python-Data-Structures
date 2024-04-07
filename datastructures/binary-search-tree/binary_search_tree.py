class BinarySearchTree:

    def __init__(self):
        self.__root = None  # Root pointer. Initialized to None since three tree is empty upon instantiation

    """
    We make the node class private to prevent manipulation of data in an illegal way that will mess with our
    Binary search tree itself
    """

    class __Node:

        def __init__(self, key, data, left=None, right=None):
            self.__key = key
            self.__data = data
            self.__left = left
            self.__right = right

        @property
        def key(self):
            return self.__key

        @key.setter
        def key(self, value):
            self.__key = value

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            self.__data = value

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, value):
            self.__left = value

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, value):
            self.__right = value

        def __str__(self):
            return f"({str(self.__key)}, {str(self.__data)})"

    def is_empty(self):
        return self.__root is None

    def root(self):
        if self.is_empty():
            raise Exception("The tree is empty")
        else:
            # We do not want to return the root, that is a node object, and our node class is private. So... return a
            # tuple
            return (self.__root.key, self.__root.data)

    """
    start at the root. while the current node we are looking at is not the end, continue down the tree. If key for
    our nodes are less than our goal, go left, if not, go right.
    """

    def __find(self, goal):
        current = self.__root
        parent = self
        while current and goal != current.key:
            parent = current
            if goal < current.key:
                current = current.left
            else:
                current = current.right
        return (current, parent)

    def search(self, goal):
        node, p = self.__find(goal)
        return node.data if node else None

    def insert(self, key, data):  # we need to make sure we specify what the key for our new data will be
        node, p = self.__find(key)  # this will either come up with a duplicate value or none
        if node:  # meaning our key does exist
            raise Exception("Duplicate key not allowed")
        if p is self:  # this will check if the current node we are on is None
            self.__root = self.__Node(key, data)
        elif key < p.key:
            p.left = self.__Node(key, data)
        else:
            p.right = self.__Node(key, data)
        return True

    # We are doing ascending order
    def __in_order_traversal(self, node, function):

        # Base case, if node exists
        if node:
            # Recursive Case
            self.__in_order_traversal(node.left, function)
            function(node)  # Remember, this will not run until the recursion above is completed
            self.__in_order_traversal(node.right, function)

    def in_order_traversal(self, function=print):
        self.__in_order_traversal(self.__root, function)

    """
    It would be better to use Enums for the traverse type, but python enums are weird
    
    Additionally, we are going to use a stack to determine our pre, in, and post traversal
    
    post: visits parent last
    pre: order in which nodes were inserted
    in: ascending order

    """

    def traverse(self, traverse_type="in"):
        if traverse_type not in ["pre", "in", "post"]:
            raise ValueError("Invalid traverse type, must be 'pre', 'in', or 'post'")

        # in reality, it would make more sense to use the stack class already built, but a list will work fine
        stack = []
        stack.append(self.__root)

        while not len(stack) == 0:
            item = stack.pop()
            if isinstance(item, self.__Node):
                if traverse_type == "post":
                    stack.append((item.key, item.data))
                stack.append(item.right)
                if traverse_type == "in":
                    stack.append((item.key, item.data))
                stack.append(item.left)
                if traverse_type == "pre":
                    stack.append((item.key, item.data))
            elif item:
                yield item

    def min_node(self):
        if self.is_empty():
            raise Exception("The tree is empty")
        else:
            node = self.__root
            while node.left:
                node = node.left
            return (node.key, node.data)

    def max_node(self):
        if self.is_empty():
            raise Exception("The tree is empty")
        else:
            node = self.__root
            while node.right:
                node = node.right
            return (node.key, node.data)


bst = BinarySearchTree()
bst.insert(5, 5)
bst.insert(4, 4)
bst.insert(3, 3)
bst.insert(20, 20)
bst.insert(15, 15)
bst.insert(25, 25)
for x in bst.traverse("post"):
    print(x)
