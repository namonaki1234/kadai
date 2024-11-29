# 駒の動き（成り駒も含む）
directions = {
    '歩': [(1, 0)], '香': [(1, 0)], '桂': [(2, 1), (2, -1)], '銀': [(1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
    '金': [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1)],
    '王': [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,1), (1,-1), (-1,-1)],
    '飛': [(0,1), (1,0), (0,-1), (-1,0)], '角': [(1,1), (1,-1), (-1,1), (-1,-1)],
    'と': [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1)],
    '竜': [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)],
    '馬': [(1,1), (1,-1), (-1,1), (-1,-1), (0,1), (1,0), (0,-1), (-1,0)]
}

promote = {'歩': 'と', '香': 'と', '桂': 'と', '銀': 'と', '飛': '竜', '角': '馬'}  # 成り駒

# 初期配置（簡略化のため一部の駒は省略）
board = [['香', '桂', '銀', '金', '王', '金', '銀', '桂', '香'],
         ['']*9, ['歩']*9, ['']*9, ['']*9, ['']*9, ['歩']*9,
         ['']*9, ['香', '桂', '銀', '金', '王', '金', '銀', '桂', '香']]

def print_board():
    for row in board: print(' '.join(row if row else '　' for row in row))

def move_piece(from_pos, to_pos, turn):
    x1, y1 = from_pos; x2, y2 = to_pos
    piece = board[x1][y1]
    if (x1, y1) != (x2, y2) and valid_move(piece, x1, y1, x2, y2, turn):
        board[x2][y2], board[x1][y1] = piece, ''
        if piece in promote and (turn == 1 and x2 <= 2 or turn == 2 and x2 >= 6):
            board[x2][y2] = promote[piece]  # 成り処理

def valid_move(piece, x1, y1, x2, y2, turn):
    if piece not in directions: return False  # 動けない駒
    if piece == '飛' or piece == '角':  # 飛車と角の連続移動を考慮
        dx, dy = x2 - x1, y2 - y1
        if dx and dy and abs(dx) == abs(dy) or not dx or not dy: return True
    return any((x1+dx, y1+dy) == (x2, y2) for dx, dy in directions[piece])

def check_victory():
    kings = sum(row.count('王') for row in board)
    return kings < 2

# メインループ
turn = 1
while not check_victory():
    print_board()
    from_pos = tuple(map(int, input(f"Player {turn} move from (x y): ").split()))
    to_pos = tuple(map(int, input("Move to (x y): ").split()))
    move_piece(from_pos, to_pos, turn)
    turn = 3 - turn  # ターン切り替え

print("ゲーム終了")
