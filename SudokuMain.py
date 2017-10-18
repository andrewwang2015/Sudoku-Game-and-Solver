import argparse 
from SudokuGame import *
from SudokuBoard import *
from SudokuUI import *
from SudokuSolver import *

def parse_arguments():
    """
    Parses arguments of the form:
        sudokuMain.py <board name>
    """
    SOLVE_CHOICES = ['Y', 'N', 'y', 'n']
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-s", "--solver", help='Use solver',
                            action="store_true")
    arg_parser.add_argument("--board",
                            help="Desired board name",
                            type=str,
                            required=True)

    # Creates a dictionary of keys = argument flag, and value = argument
    args = arg_parser.parse_args()
    return args.board, args.solver

if __name__ == "__main__":
    arguments = parse_arguments()
    board_file = arguments[0] + '.txt'
    to_solve = arguments[1]
    game = SudokuGame(board_file)
    game.start()

    root = Tk()
    if not to_solve :
        SudokuUI(root, game)
    else:
        temp = SudokuSolver(SudokuUI(root, game))
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    if to_solve:
        temp.solve_sudoku()
    root.mainloop()

