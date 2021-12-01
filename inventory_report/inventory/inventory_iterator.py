from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.counter = 0

    def __next__(self):
        try:
            next = self.data[self.counter]
        except IndexError:
            raise StopIteration()
        else:
            self.counter += 1
            return next
