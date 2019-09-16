from position import Position
from abc import ABC, abstractmethod
from typing import Iterable, Callable
from itertools import takewhile

class ChessPiece(ABC):
    position: Position

    def __init__(self, position: Position):
        self.position = position

    @abstractmethod
    def moves(self) -> Iterable[Position]:
        pass

class Knight(ChessPiece):
    def _possible_moves(self) -> Iterable[Position]:
        yield self.position.north.north.west
        yield self.position.north.north.east
        yield self.position.west.north.west
        yield self.position.east.north.east
        yield self.position.west.south.west
        yield self.position.east.south.east
        yield self.position.south.south.west
        yield self.position.south.south.east

    def moves(self) -> Iterable[Position]:
        yield from (p for p in self._possible_moves() if p.is_valid())

def _travel(p: Position, f: Callable[[Position], Position]) -> Iterable[Position]:
    def go():
        nonlocal p
        p = f(p)
        return p
    yield from takewhile(Position.is_valid, iter(go, None))

class Rook(ChessPiece):
    def moves(self) -> Iterable[Position]:
        yield from _travel(self.position, lambda p: p.north)
        yield from _travel(self.position, lambda p: p.south)
        yield from _travel(self.position, lambda p: p.east)
        yield from _travel(self.position, lambda p: p.west)

class Bishop(ChessPiece):
    def moves(self) -> Iterable[Position]:
        yield from _travel(self.position, lambda p: p.north.east)
        yield from _travel(self.position, lambda p: p.north.west)
        yield from _travel(self.position, lambda p: p.south.east)
        yield from _travel(self.position, lambda p: p.south.west)

class Queen(ChessPiece):
    def moves(self) -> Iterable[Position]:
        yield from Rook.moves(self)
        yield from Bishop.moves(self)
