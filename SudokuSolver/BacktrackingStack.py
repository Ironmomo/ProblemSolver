from utils import *
    
    
####################
# Solve Sudoku     #
####################

initialBoard = [
    [7,3,4,0,0,0,0,2,1],
    [6,8,5,0,0,2,0,9,0],
    [2,0,0,0,0,4,0,0,0],
    [5,6,0,0,2,0,0,3,9],
    [3,0,0,0,1,0,0,7,6],
    [0,0,0,0,0,0,5,0,2],
    [0,2,6,0,7,0,0,5,3],
    [8,5,1,3,4,0,2,0,0],
    [4,0,3,0,5,0,0,1,0]
]

initialState = State(initialBoard, 0)

stateStack = [initialState]

hasSolution = False

curState = stateStack.pop()

while curState and not hasSolution:
    # find empty position
    pos = findEmptyPosition(curState.board)
    if pos == None:
        hasSolution = True
        break
    # find valid action
    for i in range(curState.action + 1, 10):
        if checkIfValid(curState.board, i, pos):
            # create new State
            newState = addNumber(curState.board, i, pos)
            # add states to stack
            curState.action = i
            stateStack.append(curState)
            stateStack.append(newState)
            break
    # set curState
    try:
        curState = stateStack.pop()
    except IndexError:
        curState = None
 
if hasSolution:   
    print("Solution found:")
    printBoard(curState.board)
else:
    print("No Solution found")