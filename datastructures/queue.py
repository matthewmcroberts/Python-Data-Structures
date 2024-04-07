class Queue:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__a = [None] * max_size
        self.__front = 1
        self.__rear = 0
        self.__n_items = 0

    def is_full(self):
        return self.__n_items == self.__max_size

    def is_empty(self):
        return self.__n_items == 0

    def insert(self, item):
        if self.is_full():  # If we don't check if its full then we run into memory leaks
            raise Exception("Overflow")
        self.__rear += 1
        if self.__rear == self.__max_size:
            self.__rear = 0  # Go back to the beginning of the array if we are at the end
        self.__a[self.__rear] = item
        self.__n_items += 1

    def remove(self):
        if self.is_empty():
            raise Exception("Underflow")
        copy = self.__a[self.__front]
        self.__a[self.__front] = None
        self.__front += 1
        if self.__front == self.__max_size:
            self.__front = 0  # Go back to beginning of the array if we are at the end
        self.__n_items -= 1

        return copy

    def peek(self):
        if self.is_empty():
            raise Exception("Underflow (Peeking on an empty queue)")
        return self.__a[self.__front]

    """This is what gets ran when the builtin len() is called on the array"""

    def __len__(self):
        return self.__n_items

    def __str__(self):
        s = ""
        for i, x in enumerate(self.__a):
            s += "{Index " + str(i) + " Value: " + str(x) + "} "
        return s


q1 = Queue(3)
#      [ | | ]
#  Rear ^ ^ Front
q1.insert(1)
#      [ |1| ]
#         ^ Front
#         ^ Rear
q1.insert(2)
#      [ |1|2]
#   Front ^ ^ Rear
q1.insert(3)
#      [3|1|2]
#  Rear ^ ^ Front
print(q1)
q1.remove()
#      [3| |2]
#  Rear ^   ^ Front
q1.insert(5)
#      [3|5|2]
#    Rear ^ ^ Front
print(q1)
