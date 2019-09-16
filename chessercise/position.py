ORD_A = ord('a')

class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    @classmethod
    def from_algebraic_notation(cls, notation: str) -> 'Position':
        x = ord(notation[0]) - ORD_A
        y = int(notation[1]) - 1
        return cls(x, y)

    def to_algebraic_notation(self) -> str:
        x = chr(self.x + ORD_A)
        y = self.y + 1
        return f'{x}{y}'
    
    def __str__(self) -> str:
        return self.to_algebraic_notation()

    @property
    def north(self) -> 'Position':
        return Position(self.x, self.y + 1)

    @property
    def south(self) -> 'Position':
        return Position(self.x, self.y - 1)

    @property
    def east(self) -> 'Position':
        return Position(self.x + 1, self.y)

    @property
    def west(self) -> 'Position':
        return Position(self.x - 1, self.y)

    def is_valid(self):
        return 0 <= self.x <= 7 and 0 <= self.y <= 7