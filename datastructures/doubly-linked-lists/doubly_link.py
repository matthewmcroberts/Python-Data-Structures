from link import Link


class Link(Link):  # More user-friendly to call it Link as well
    def __init__(self, data, next=None, previous=None):
        super().__init__(data, next)
        self.__previous = previous

    @property
    def previous(self):
        return self.__previous

    """previous should either be pointing to the previous link or None"""

    @previous.setter
    def previous(self, link):
        if link is None or isinstance(link, Link):
            self.__previous = link
        else:
            raise Exception("Invalid link")

    def is_first(self):
        return self.__previous is None  # if its pointing to none, then that means its the first link in the list
