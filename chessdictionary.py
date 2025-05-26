print("Harsha D S, USN: 1AY24AI041, SEC: M")

def isValidChessBoard(board):
    valid_positions = {f"{c}{r}" for c in "abcdefgh" for r in range(1, 9)}
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    
    piece_count = {'w': 0, 'b': 0}
    king_count = {'w': 0, 'b': 0}
    pawn_count = {'w': 0, 'b': 0}
    
    for position, piece in board.items():
        
        if position not in valid_positions:
            return False
    
        if len(piece) < 2 or piece[0] not in 'wb' or piece[1:] not in valid_pieces:
            return False
        
        color = piece[0]
        piece_type = piece[1:]
        
        piece_count[color] += 1
        
        if piece_type == 'king':
            king_count[color] += 1
        if piece_type == 'pawn':
            pawn_count[color] += 1
    
  
    if king_count['w'] != 1 or king_count['b'] != 1:
        return False
    if piece_count['w'] > 16 or piece_count['b'] > 16:
        return False
    if pawn_count['w'] > 8 or pawn_count['b'] > 8:
        return False
    
    return True


chess_board = {
    'a1': 'wrook', 'b1': 'wknight', 'c1': 'wbishop', 'd1': 'wqueen',
    'e1': 'wking', 'f1': 'wbishop', 'g1': 'wknight', 'h1': 'wrook',
    'a2': 'wpawn', 'b2': 'wpawn', 'c2': 'wpawn', 'd2': 'wpawn',
    'e2': 'wpawn', 'f2': 'wpawn', 'g2': 'wpawn', 'h2': 'wpawn',
    'a7': 'bpawn', 'b7': 'bpawn', 'c7': 'bpawn', 'd7': 'bpawn',
    'e7': 'bpawn', 'f7': 'bpawn', 'g7': 'bpawn', 'h7': 'bpawn',
    'a8': 'brook', 'b8': 'bknight', 'c8': 'bbishop', 'd8': 'bqueen',
    'e8': 'bking', 'f8': 'bbishop', 'g8': 'bknight', 'h8': 'brook'
}


print(isValidChessBoard(chess_board))
