import scrape


class BoardState:
    # initializes board
    def __init__(self, board, parent):
        self.board = board
        self.cell = self.getnext()
        self.values = self.generatevalidvalues()
        self.parent = parent
        self.previous = []

    # get's the next blank spot of the puzzle
    def getnext(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                if self.board[row][column] == 0:
                    return row, column
        return None

    # checks if a number is valid in a given board state
    def isvalid(self, i):
        row, column = self.cell
        if i in self.board[row]:
            return False
        for rowe in self.board:
            if rowe[column] == i:
                return False

        boxx = (row // 3) * 3
        boxy = (column // 3) * 3

        for j in range(boxx, boxx + 3):
            for k in range(boxy, boxy + 3):
                if self.board[j][k] == i:
                    return False
        return True

    # returns a list of possible values for a given cell
    def generatevalidvalues(self):
        values = []
        for i in range(1, 10):
            if self.isvalid(i):
                values.append(i)
        return values

    # creates new set of valid values for a cell
    def setnewvalues(self):
        self.values.clear()
        for i in range(1, 10):
            if self.isvalid(i):
                self.values.append(i)

    # sets the value of a cell in the puzzle board
    def setvalue(self):
        row, column = self.cell
        for val in self.values:
            if val not in self.previous:
                self.board[row][column] = val
                return True
        return False

    # retrieves a value from the board
    def getvalue(self):
        row, column = self.cell
        return self.board[row][column]

    # adds a value to the previously explored list
    def addprev(self):
        self.previous.append(self.getvalue())

    # creates a new game state
    def createchild(self):
        return BoardState(self.board, self)

    # checks if a state is complete and correct
    def isgoalstate(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    # set a value on the board to 0
    def setzero(self):
        row, column = self.cell
        self.board[row][column] = 0

    # prints the board in an easier to read format
    def printboard(self):
        print("-------------------------")
        for row in self.board:
            print(row)
        print("-------------------------")


def main(board):
    # uses scrape to initialize the start state of the board
    state = BoardState(board, None)
    print("ORIGINAL PUZZLE:")
    state.printboard()

    while True:

        # tries to set a valid values
        if not state.setvalue():
            # no valid value, erase and go back to parent
            state.setzero()
            # backtrack to parent
            state = state.parent
            # state is null, so no solution can be found
            if not state:
                print("PUZZLE CANNOT BE SOLVED")
                break
            # generate new values for parent
            state.setnewvalues()
            # add previous value to list of already explored values
            state.addprev()
            continue

        # test if a goal has been reached
        if state.isgoalstate():
            # print("SOLUTION FOUND:")
            # state.printboard()
            return state.board

        # set state to next child
        state = state.createchild()

# uncomment to run
# main(scrape.getboard(1))












