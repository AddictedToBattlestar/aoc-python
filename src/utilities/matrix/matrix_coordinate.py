class MatrixCoordinate:
    def __init__(self, x: int, y: int, identifier: str):
        self.x = x
        self.y = y
        self.identifier = identifier

    def __str__(self):
        return '({self.x},{self.y})'.format(self=self)

    def __lt__(self, other):
        if self.x < other.x:
            return True
        else:
            return self.x == other.x and self.y < other.y