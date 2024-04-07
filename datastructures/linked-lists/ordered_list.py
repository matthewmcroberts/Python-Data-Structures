from linked_list import LinkedList, identity
from link import Link


class OrderedList(LinkedList):
    def __init__(self, key=identity):
        super().__init__()
        self.__key = key

    def find(self, goal):
        link = self.first
        while link is not None and self.__key(link.data) < goal:  # this will be ascending order
            link = link.next
        return link  # this will either return the link or none depending on if we got to the end of the list

    def search(self, goal):
        link = self.find(goal)
        if link is not None and self.__key(link.data) == goal:
            return link.data

    def insert(self, data):
        goal = self.__key(data)
        previous = self  # points to self initially because there is no previous link for the first link
        while previous.next is not None and self.__key(previous.next.data) < goal:
            previous = previous.next
        new_link = Link(data, previous.next)
        previous.next = new_link

    def delete(self, goal):
        if self.is_empty():
            raise Exception("Underflow")
        previous = self
        while previous.next is not None and self.__key(previous.next.data) < goal:
            previous = previous.next

        if previous.next is None or goal != self.__key(previous.next.data):
            raise Exception("No matching link found")

        to_delete = previous.next
        previous.next = to_delete.next
