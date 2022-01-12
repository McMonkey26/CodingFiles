board = [
    ['r','n','b','k','q','b','n','r'],
    ['p','p','p','p','p','p','p','p'],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    ['P','P','P','P','P','P','P','P'],
    ['R','N','B','K','Q','B','N','R']
]

def getIndex(coord):
    letters = ['a','b','c','d','e','f','g','h']
    x = letters.index(coord[0])
    y = 8-int(coord[1])
    return (y, int(x))

def getPossMoves(piece, x, y):
    print(piece)
    x += 1
    y = 8 - y
    print(x)
    print(y)
    if piece == 'p':
        if y == 7:
            return [(x, y-1),(x, y-2)]
        elif y-2 in range(8):
            return [(x, y-1)]
        else:
            return []
    elif piece == 'P':
        if y == 2:
            return [(x, y+1),(x, y+2)]
        elif y in range(8):
            return [(x, y+1)]
        else:
            return []
    elif piece.lower() == 'r':
        tempMoves = []
        for i in range(1,8):
            if i != x:
                tempMoves.append((i, y))
            if i != y:
                tempMoves.append((x, i))
        return tempMoves
    elif piece.lower() == 'n':
        tempMoves = []
        if x-3 in range(8):
            if y-2 in range(8):
                tempMoves.append((x-2, y-1))
            if y in range(8):
                tempMoves.append((x-2, y+1))
        if x-2 in range(8):
            if y-3 in range(8):
                tempMoves.append((x-1, y-2))
            if y+1 in range(8):
                tempMoves.append((x-1, y+2))
        if x in range(8):
            if y-3 in range(8):
                tempMoves.append((x+1, y-2))
            if y+1 in range(8):
                tempMoves.append((x+1, y+2))
        if x+1 in range(8):
            if y-2 in range(8):
                tempMoves.append((x+2, y-1))
            if y in range(8):
                tempMoves.append((x+2, y+1))
        return tempMoves
    elif piece.lower() == 'b':
        tempMoves = []
        for i in range(1-x, 9-x):
            if y+i-1 in range(8):
                tempMoves.append((x+i, y+i))
            if y-i-1 in range(8):
                tempMoves.append((x+i, y-i))
        return tempMoves
    elif piece.lower() == 'k':
        tempMoves = []
        if x-2 in range(8):
            if y-2 in range(8):
                tempMoves.append((x-1, y-1))
            if y-1 in range(8):
                tempMoves.append((x-1, y))
            if y in range(8):
                tempMoves.append((x-1, y+1))
        if x-1 in range(8):
            if y-2 in range(8):
                tempMoves.append((x, y-1))
            if y in range(8):
                tempMoves.append((x, y+1))
        if x in range(8):
            if y-2 in range(8):
                tempMoves.append((x+1, y-1))
            if y-1 in range(8):
                tempMoves.append((x+1, y))
            if y in range(8):
                tempMoves.append((x+1, y+1))
        return tempMoves
    elif piece.lower() == 'q':
        tempMoves = []
        for i in range(1-x, 9-x):
            if y+i-1 in range(8):
                tempMoves.append((x+i, y+i))
            if y-i-i in range(8):
                tempMoves.append((x+i, y-i))
        for i in range(1,8):
            if i != x:
                tempMoves.append((i, y))
            if i != y:
                tempMoves.append((x, i))
        return tempMoves

def toIndex(coords):
    print(coords)
    tempValues = []
    for value in coords:
        x = 8-value[1]
        y = value[0]-1
        tempValues.append((x, y))
    return tempValues

for i in board:
    print(i)

move = input()
while move != 'stop':
    (start, end) = move.split(' to ')
    start = getIndex(start)
    end = getIndex(end)
    print(getPossMoves(board[start[0]][start[1]], start[1], start[0]))
    if board[end[0]][end[1]] == ' ' and (end[0],end[1]) in toIndex(getPossMoves(board[start[0]][start[1]], start[1], start[0])):
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = ' '
    for i in board:
        print(i)
    move = input()

#any('k' in sublist for sublist in board)