from link import Link


def identity(x):
    return x


class LinkedList:
    def __init__(self):
        self.__first = None

    class __ListIterator:
        def __init__(self, linked_list):
            self._linked_list = linked_list
            self._next = linked_list.next

        def next(self):
            if self._next is None:
                raise StopIteration
            item = self._next.data
            self._next = self._next.next  # they called next, so we need to set our new next
            return item

        def current(self):
            if self._next is not None:
                return self._next.data
            else:
                return None

        def has_next(self):
            return self._next is not None

    def iterator(self):
        return LinkedList.__ListIterator(self)

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise Exception("Invalid link")

    """Both next props are doing the same thing as the first props, the whole is just to make it more understandable
    for the user"""

    @property
    def next(self):
        return self.first

    @next.setter
    def next(self, link):
        self.first = link

    def is_empty(self):
        return self.__first is None

    def get_first_data(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.first.data

    def traverse(self, func=print):
        link = self.first
        while link is not None:
            func(link.data)
            link = link.next

    def insert(self, data):  # inserting at the beginning of the linked list, this is O(1)
        link = Link(data, self.first)
        self.first = link

    def insert_after(self, data, goal, key=identity):  # O(n)
        link = self.find(goal, key)
        if link is not None:
            new_link = Link(data, link.next)
            link.next = new_link
        else:
            raise Exception("Data does not exist in LinkedList")

    def find(self, goal, key=identity):  # goal is the datapoint we are looking for
        link = self.first
        while link is not None:
            # pass our current link data into our key function and check if the data is equal to the goal link data
            if key(link.data) == goal:
                return link
            link = link.next
        return None

    def search(self, goal, key=identity):
        link = self.find(goal, key)
        if link is not None:
            return link.data
        raise Exception("Data does not exist in LinkedList")

    def delete_first(self):
        if self.is_empty():
            raise Exception("Underflow")
        first = self.first
        self.first = first.next
        return first.data

    def delete(self, goal, key=identity):
        if self.is_empty():
            raise Exception("Underflow")
        previous = self
        while previous.next is not None:
            link = previous.next
            if goal == key(link.data):
                previous.next = link.next
                return link.data
            previous = link
        raise Exception("Data does not exist in LinkedList")

    def __len__(self):
        curr_length = 0
        link = self.first
        while link is not None:
            curr_length += 1
            link = link.next
        return curr_length

    def __str__(self):
        result = "["
        link = self.first
        while link is not None:
            if len(result) > 1:
                result += " > "
            result += str(link)
            link = link.next
        return result + "]"


"""
EXAMPLE USAGE OF ITERATOR IF WE DON'T USE PYTHON'S BUILT IN MAGIC METHOD ITERATOR

l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)

it = l1.iterator()
try:
    while True:
        print("Next item is ", it.next())
except StopIteration:
    pass

it = l1.iterator()
while it.has_next():
    print("Next item is ", it.next())

it = l1.iterator()
while it.current() is not None:
    print("Next item is ", it.next())
"""