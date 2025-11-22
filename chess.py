import sys
import copy

# ----------------------------------------------------------------------
# Starting position (standard chess layout)
# ----------------------------------------------------------------------
STARTING_PIECES = {
    'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
    'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR',
    'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP',
    'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
    'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ',
    'e1': 'wK', 'f1': 'wB', 'g1': 'wN', 'h1': 'wR',
    'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
    'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP',
}

# ----------------------------------------------------------------------
# Visual template for the board
# ----------------------------------------------------------------------
BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

WHITE_SQUARE = '||'   # visual for an empty white square
BLACK_SQUARE = '  '   # visual for an empty black square


# ----------------------------------------------------------------------
# Print the board to the console
# ----------------------------------------------------------------------
def print_chess_board(board):
    squares = []
    is_white_square = True          # a8 is a dark square, but we start with white for visual symmetry
    for y in '87654321':
        for x in 'abcdefgh':
            coord = x + y
            if coord in board:
                squares.append(board[coord])
            else:
                # Alternate empty‑square graphics
                squares.append(WHITE_SQUARE if is_white_square else BLACK_SQUARE)
            is_white_square = not is_white_square
        # Flip at the end of each rank to keep the checker pattern
        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))


# ----------------------------------------------------------------------
# Help text
# ----------------------------------------------------------------------
def print_help():
    print('Interactive Chess Board')
    print()
    print('Pieces:')
    print('  w - White, b - Black')
    print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
    print('Commands:')
    print('  move e2 e4   - Moves the piece at e2 to e4.')
    print('  remove e2    - Removes the piece at e2.')
    print('  set e2 wP    - Sets square e2 to a white pawn.')
    print('  reset        - Reset pieces back to their starting squares.')
    print('  clear        - Clear the entire board.')
    print('  fill wP      - Fill entire board with white pawns.')
    print('  help         - Show this help information.')
    print('  quit         - Quits the program.')


# ----------------------------------------------------------------------
# Basic validation of a board dictionary
# ----------------------------------------------------------------------
def is_valid_chessboard(board):
    # Count kings – there must be exactly one of each colour
    black_king = sum(1 for p in board.values() if p == 'bK')
    white_king = sum(1 for p in board.values() if p == 'wK')
    if black_king != 1 or white_king != 1:
        return False

    # Count total pieces – cannot exceed 32 and each side ≤ 16
    if len(board) > 32:
        return False
    if sum(1 for p in board.values() if p.startswith('b')) > 16:
        return False
    if sum(1 for p in board.values() if p.startswith('w')) > 16:
        return False

    # Verify every key is a legal square
    valid_squares = {f'{x}{y}' for x in 'abcdefgh' for y in '87654321'}
    if any(sq not in valid_squares for sq in board):
        return False

    # Verify every value is a known piece code
    valid_pieces = {
        'wP', 'wN', 'wB', 'wR', 'wQ', 'wK',
        'bP', 'bN', 'bB', 'bR', 'bQ', 'bK'
    }
    if any(piece not in valid_pieces for piece in board.values()):
        return False

    return True


# ----------------------------------------------------------------------
# Main interactive loop
# ----------------------------------------------------------------------
def main():
    main_board = copy.copy(STARTING_PIECES)
    print_help()

    while True:
        print_chess_board(main_board)
        response = input('> ').strip().split()

        if not response:
            continue

        cmd = response[0].lower()

        if cmd == 'move' and len(response) == 3:
            src, dst = response[1], response[2]
            if src in main_board:
                main_board[dst] = main_board[src]
                del main_board[src]
            else:
                print(f'No piece on {src}')
        elif cmd == 'remove' and len(response) == 2:
            sq = response[1]
            main_board.pop(sq, None)          # safe removal
        elif cmd == 'set' and len(response) == 3:
            sq, piece = response[1], response[2]
            main_board[sq] = piece
        elif cmd == 'reset':
            main_board = copy.copy(STARTING_PIECES)
        elif cmd == 'clear':
            main_board.clear()
        elif cmd == 'fill' and len(response) == 2:
            piece = response[1]
            for y in '87654321':
                for x in 'abcdefgh':
                    main_board[f'{x}{y}'] = piece
        elif cmd == 'help':
            print_help()
        elif cmd == 'quit':
            sys.exit()
        else:
            print('Unknown command or wrong number of arguments.')

        # Optional: warn if the board is now illegal
        if not is_valid_chessboard(main_board):
            print('⚠️  Board state is invalid (e.g., missing a king or too many pieces).')


if __name__ == '__main__':
    main()
