class OrderedArray:
    def __init__(self, max_size):
        self._a = [None] * max_size
        self._nItems = 0

    """
    This find method is going to be the binary search algorithm
    """

    def find(self, item):
        low = 0  # First value in the array
        high = self._nItems - 1  # Last value in the array

        while low <= high:
            mid = (low + high) // 2  # This will cut off the decimal point by doing // operator
            if self._a[mid] == item:
                return mid
            elif self._a[mid] < item:
                low = mid + 1  # Move low to where mid is
            else:  # item is greater than mid
                high = mid - 1  # move high to where mid is
        return low

    def search(self, item):
        index = self.find(item)
        if index < self._nItems and self._a[index] == item:
            return index

    def insert(self, item):
        if self._nItems >= len(self._a):
            raise Exception("Overflow")

        index = self.find(item)
        for i in range(self._nItems, index, -1):  # Start at last item and loop backwards since shifting to right
            self._a[i] = self._a[i - 1]

        self._a[index] = item  # everything should be shifted to the right and index is now empty so insert item at
        self._nItems += 1

    def delete(self, item):
        if self._nItems <= 0:
            raise Exception("Underflow")
        index = self.find(item)

        # this check is necessary because find returns a value whether its equal to item or not
        if index < self._nItems and self._a[index] == item:
            self._nItems -= 1  # make sure pointer is pointing at the item and not empty spot
            for i in range(index, self._nItems):

                # we're shifting everything back to the left which also overrides what we are wanting to delete, so we dont have to manually delete it
                self._a[i] = self._a[i + 1]
            return True
        return False
