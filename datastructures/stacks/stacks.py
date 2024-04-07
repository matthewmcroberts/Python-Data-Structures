class Stack:
    def __init__(self, max_size):
        self._a = [None] * max_size

        # Unlike the pointer, the top points to the index of the actual element/stack, not the empty spot
        # So because it points to an index, we need to keep in mind that indexes start at 0 not 1, so while it's
        # empty just make it -1
        self._top = -1

    def push(self, item):
        if self._top + 1 == len(self._a):  # meaning stack is full
            raise Exception("Overflow")
        self._top += 1
        self._a[self._top] = item

    def pop(self):
        if self._top <= - 1:  # meaning there is nothing in the stack
            raise Exception("Underflow")
        copy = self._a[self._top]
        self._a[self._top] = None
        self._top -= 1
        return copy

    def peek(self):
        if self._top <= - 1:  # meaning peeking on an empty stack
            raise Exception("Underflow")
        return self._a[self._top]


# Ex. Reverse a word as quickly as possible

word = "animal"
s1 = Stack(len(word))

for letter in word:
    s1.push(letter)
    print("Current top: ", s1.peek())

backwards = ""

for i in range(len(word)):
    backwards += s1.pop()
print("Backwards: ", backwards)

# the speed for the example would be O(n) + O(n) = 2O(n), but we don't care about constants so it's just O(n)
