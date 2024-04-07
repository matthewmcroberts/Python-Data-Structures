"""Creating our own basic Array class with python instead of using python's built in arraylist"""


class Array:
    def __init__(self, max_size):
        self._a = [None] * max_size  # Multiplying a list by some int recreates that list there that many times
        self._nItems = 0  # Pointer

    """
    Go to the index of the pointer in the array (will be at an empty spot if not full, and set the value of that index 
    to param item
    """

    def insert(self, item):
        self._a[self._nItems] = item
        self._nItems += 1

    """
    Looping up to the range of every spot that is filled (no sense in looping empty spaces too, so thats why we go only
    to where the pointer is, because that's end of every filled index.
    i is an index, so use that index to check the spot in the array at i for a match against the item. if there is a 
    match, just return i, if not, return None
    """

    def search(self, item):
        for i in range(
                self._nItems):  # We are using nItems instead of maxsize so that we don't loop over all the empty indexes
            if self._a[i] == item:
                return i
        return None

    """
    Same functionality as a search from line 37-38, after that we create a new pointer where item is that basically moves all
    elements back, overriding the item and replacing it with whatever was to the right of the pointer
    """

    def delete(self, item):
        for i in range(self._nItems):
            if self._a[i] == item:
                for k in range(i, self._nItems):
                    if i - self._nItems != -1:  # meaning we can still shift to the right and nItems isn't pointing to an invalid location
                        self._a[k] = self._a[k + 1]  # This is where the deletion occurs, the spot is being overriden
                self._nItems -= 1
                return True
        return False

    """
    Simply loop up to the pointer (so that we do not loop over indexes that contain no item) and then call the param
    function passing in the item
    """
    def traverse(self, function=print):
        for i in range(self._nItems):
            function(
                self._a[i])  # Take note that traverse could become O(n^2) etc if the callback function contains loops


a1 = Array(5)
a1.insert(10)
a1.insert(15)
a1.traverse()

a1.delete(10)
print("Search: ", a1.search(15))
a1.delete(15)
print("Delete: ", a1.delete(50))
a1.traverse()

a1.insert(15)
a1.insert(15)
a1.insert(15)
a1.insert(15)
a1.insert(15)
a1.traverse()
