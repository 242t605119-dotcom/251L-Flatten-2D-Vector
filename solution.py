class Vector2D:

    def __init__(self, vec):
        self.vec = vec
        self.row = 0
        self.col = 0

    def next(self) -> int:
        self.move()
        value = self.vec[self.row][self.col]
        self.col += 1
        return value

    def hasNext(self) -> bool:
        self.move()
        return self.row < len(self.vec)

    def move(self):
        while self.row < len(self.vec) and self.col >= len(self.vec[self.row]):
            self.row += 1
            self.col = 0
