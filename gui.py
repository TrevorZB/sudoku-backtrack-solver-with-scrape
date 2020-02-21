from tkinter import *
import solver
import scrape

root = Tk()

startingboard = scrape.getboard(1)


def drawboard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            value = board[i][j]
            cell = Label(root, text=value)
            cell.grid(row=i, column=j)


def solve(board):
    drawboard(solver.main(board))


drawboard(startingboard)
solvebutton = Button(root, text='Solve', command=lambda: solve(startingboard))
solvebutton.grid(row=9, column=9)


root.mainloop()