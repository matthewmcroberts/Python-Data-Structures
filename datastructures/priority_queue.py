# default priority function
def identity(x):
    return x


class PriorityQueue:
    def __init__(self, max_size, priority=identity):
        self.__max_size = max_size
        self.__a = [None] * max_size
        self.__priority = priority  # this will be a function that returns what is being compared about the item
        self.__n_items = 0  # remember, n_items points to the empty index

    def is_empty(self):
        return self.__n_items == 0

    def is_full(self):
        return self.__n_items == self.__max_size

    def insert(self, item):
        if self.is_full():
            raise Exception("Overflow")
        i = self.__n_items - 1  # make the i pointer point at the last item in the queue instead of empty spot

        # the higher the number returned from priority(item), the higher the priority it gets
        # Say the items are equal, then the item being inserted gets lower priority, hence <=
        while i >= 0 and (self.__priority(item) <= self.__priority(self.__a[i])):
            self.__a[i + 1] = self.__a[i]
            i -= 1
        self.__a[i + 1] = item
        self.__n_items += 1

    def remove(self):
        if self.is_empty():
            raise Exception("Underflow")
        self.__n_items -= 1
        copy = self.__a[self.__n_items]
        self.__a[self.__n_items] = None
        return copy

    def peek(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.__a[self.__n_items - 1]  # Remember, n_items by itself is pointing to the empty spot in the queue

    def __len__(self):
        return self.__n_items

    def __str__(self):
        s = ""
        for i, x in enumerate(self.__a):
            s += "{Index: " + str(i) + " Value: " + str(x) + "}"
        return s


"""p1 = PriorityQueue(5)
p1.insert(1)
p1.insert(5)
p1.insert(2)
p1.insert(10)
p1.insert(3)
print(p1)
p1.remove()
p1.remove()
p1.insert(0.5)
print(p1)
"""


def identify2(x):
    return x.get("age")


p2 = PriorityQueue(5, identify2)
p2.insert({"name": "andrew", "age": 45})
p2.insert({"name": "bob", "age": 22})
p2.insert({"name": "Jill", "age": 55})
print(p2)
