"""Write a Squares(n) iterator class that produces 1, 4, 9, ... up to n squared."""


class Squares:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.n:
            raise StopIteration
        return self.current * self.current


print(*Squares(5))
