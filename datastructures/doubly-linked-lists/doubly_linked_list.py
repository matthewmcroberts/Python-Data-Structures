from linked_list import LinkedList, identity
from doubly_link import Link


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self.__last = None

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, link):
        if link is None or isinstance(link, Link):
            self.__last = link
        else:
            raise Exception("Invalid link")

    def insert_first(self, data):
        link = Link(data, next=self.first)
        if self.is_empty():
            self.last = link
            self.first = link
        else:
            self.first.previous = link
            self.first = link

    """
    def insert(self, data):
        self.insert_first(data)
        
    Does the same thing as below
    """
    insert = insert_first  # Overrides the insert method in our super class, and setting it to insert_first to be run

    def insert_last(self, data):
        link = Link(data, previous=self.last)  # don't have to worry about next since this is the last link
        if self.is_empty():
            self.first = link
        else:
            self.last.next = link
            self.last = link

    # Key is simply so we can know what we are comparing each link with
    def insert_after(self, goal, data, key=identity):
        link = self.find(goal, key)
        if link is None:
            raise Exception("Link not found")
        if link.is_last():
            self.insert_last(data)
        else:
            new_link = Link(data, previous=link, next=link.next)
            link.next.previous = new_link
            link.next = new_link

    def delete_first(self):
        if self.is_empty():
            raise Exception("Underflow")
        first_copy = self.first  # this is the link we are removing
        self.first = first_copy.next
        if self.first:
            self.first.previous = None
        return first_copy.data

    def delete_last(self):
        if self.is_empty():
            raise Exception("Underflow")
        last_copy = self.last
        self.last = last_copy.previous
        if self.last:
            self.last.next = None
        return last_copy.data

    def delete(self, goal, key=identity):
        link = self.find(goal, key)
        if link is None:
            raise Exception("Link not found")
        if link.is_last():
            return self.delete_last()
        elif link.is_first():
            return self.delete_first()
        else:
            link.next.previous = link.previous
            link.previous.next = link.next
            return link.data

    def traverse_backwards(self, func=print):
        link = self.last
        while link is not None:
            func(link)
            link = link.previous


d1 = DoublyLinkedList()
d1.insert_first(5)
d1.insert_first(10)
d1.insert_first(15)
d1.insert(20) #should still do an insert first because we overrided the method above
d1.traverse_backwards()

print("\n")

d1.insert_last(0)
d1.insert_last(-5)
d1.insert_last(-10)
d1.insert_last(-15)
d1.insert_last(-20)
d1.traverse()

print("\n")

d1.insert_after(0, 2)
d1.insert_after(2, 3)
d1.insert_after(3, 4)
d1.traverse_backwards()

print("\n")

d1.delete_first()
d1.delete_first()
d1.traverse_backwards()

print("\n")

d1.delete(2)
d1.delete(3)
d1.delete(4)
d1.traverse_backwards()

print("\n")
d1.delete(-20)
d1.delete_last()
print(d1)