from position import Position

a1 = Position.from_algebraic_notation('a1')

assert a1.x == 0, 'a1.x should be 0'
assert a1.y == 0, 'a1.y should be 0'
assert a1.is_valid(), 'a1 should be valid'

k12 = Position(10, 11)
assert not k12.is_valid(), 'k12 should not be valid'

assert k12.south.west.x == 9, 'j11 is sw of k12'
assert k12.north.east.y == 12, 'l13 is ne of k12'