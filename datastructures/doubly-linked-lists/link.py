class Link:
    def __init__(self, data_pointer, next_pointer=None):
        self.__data = data_pointer
        self.__next = next_pointer
        # this technically isn't pointing to the actual link, it's pointing to the memory location of where the
        # link is stored

    @property
    def data(self):
        return self.__data

    """Not going to use the setter in this example, but this would be important for an update function"""

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    """Next should either be pointing to the next link or None"""

    @next.setter
    def next(self, link):
        if link is None or isinstance(link, Link):
            self.__next = link
        else:
            raise Exception("Invalid link")

    def is_last(self):
        return self.__next is None

    def __str__(self):
        return str(self.data)
