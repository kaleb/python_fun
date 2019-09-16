from optparse import OptionParser, OptionValueError, Option
from pieces import Knight, Queen, Rook, Position
import sys

pieces = {
    'knight': Knight,
    'queen': Queen,
    'rook': Rook,
}

def check_piece(option: Option, opt_str: str, value: str, parser: OptionParser):
    print(opt_str, option, value)
    if value.lower() not in pieces:
        raise OptionValueError(f'Invalid value "{value}" for option "{opt_str}". Choices: {", ".join(pieces.keys())}')
    setattr(parser.values, option.dest, pieces[value.lower()])

def check_position(option: Option, opt_str: str, value: str, parser: OptionParser):
    if len(value) != 2:
        raise OptionValueError(f'"{opt_str}" takes 2 characters')
    p = Position.from_algebraic_notation(value.lower())
    if not p.is_valid():
        raise OptionValueError(f'"{opt_str}" must be in the range a1 to h8')
    setattr(parser.values, option.dest, p)

option_parser = OptionParser()
option_parser.add_option('--piece', action='callback', callback=check_piece, type='string')
option_parser.add_option('--position', action='callback', callback=check_position, type='string')

def main():
    opts, args = option_parser.parse_args()
    if len(args):
        sys.exit('Invalid argument count.  Must be zero.')
    if not hasattr(opts, 'piece'):
        sys.exit('"--piece" must be specified')
    if not hasattr(opts, 'position'):
        sys.exit('"--position" must be specified')
    piece = opts.piece(opts.position)
    for move in piece.moves():
        print(move)

if __name__ == '__main__':
    main()
