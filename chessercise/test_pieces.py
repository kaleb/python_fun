from pieces import Knight, Queen, Position

d2 = Position.from_algebraic_notation('d2')
nd2 = Knight(d2)
nd2_moves = list(str(move) for move in nd2.moves())

assert len(nd2_moves) == 6
assert 'b1' in nd2_moves
assert 'f1' in nd2_moves
assert 'b3' in nd2_moves
assert 'f3' in nd2_moves
assert 'c4' in nd2_moves
assert 'e4' in nd2_moves

a1 = Position.from_algebraic_notation('a1')
qa1 = Queen(a1)
qa1_moves = list(str(move) for move in qa1.moves())

assert len(qa1_moves) == 21