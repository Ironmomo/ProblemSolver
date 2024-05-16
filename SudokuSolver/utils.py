import copy

class State:
    
    def __init__(self, board, action):
        self.board = board
        self.action = action


def findEmptyPosition(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
               return x,y
    
    return None

    
def checkIfValid(board, num, pos):
    x, y = pos
    # check row
    for i in range(len(board[x])):
        if board[x][i] == num and i != y:
            return False
        
    # check column
    for i in range(len(board)):
        if board[i][y] == num and i != x:
            return False

    # check box
    row_idx = x // 3
    col_idx = y // 3
    for i in range(3):
        for j in range(3):
            if board[(row_idx * 3) + (x + i) % 3][(col_idx * 3) + (y + j) % 3] == num and (i != x or j != y):
                return False
    
    return True

def addNumber(board, num, pos):
    x,y = pos
    newBoard = copy.deepcopy(board)
    newBoard[x][y] = num

    return State(newBoard, 0)

def printBoard(board):
    print()
    for row in range(len(board)):
        toPrint = ""
        for col in range(len(board[row])):
            if col % 3 == 0 and col != 0:
                toPrint += " | "
            toPrint += f" {board[row][col]} "
        
        if row % 3 == 0 and row != 0:
            print()
            
        print(toPrint)    
    print()