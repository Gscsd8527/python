class Library2(object):
    def __init__(self):
        self.value = ['a', 'b', 'c', 'd', 'e']
        self.i = -1
    def __iter__(self):
        return self
    def next(self):
        self.i += 1
        if self.i >= len(self.value):
            raise StopIteration
        return self.value[self.i]
test = Library2()
print(test.next())
print(test.next())