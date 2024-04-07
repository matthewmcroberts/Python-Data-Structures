def fibonacci():
    previous = 0
    current = 1
    while True:
        print(current)
        my_next = previous + current
        previous = current
        current = my_next


# fibonacci()


def Iteratorfibonacci():
    previous = 0
    current = 1
    while True:
        yield current
        """similar to calling return current, but it keeps track of the state we were currently at before yield got 
        called. Yield is returning an iterable. so it'll pause until __next__ is called"""

        my_next = previous + current
        previous = current
        current = my_next


gen = Iteratorfibonacci()
"""
This is what is happening behind the scenes of the for loop below
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
"""

count = 100
for x in Iteratorfibonacci():
    if count < 1:
        break
    print(x)
    count -= 1
