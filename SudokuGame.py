from SudokuBoard import *
class SudokuGame(object):
    '''
    Sudoku Game representation 
    '''
    def __init__(self, board_file):
        self.board_file = board_file
        self.start_puzzle = SudokuBoard(board_file)

    def start(self):
        # We make copy of initial configuration in order to compensate for the 
        # clear functionality
        self.running_puzzle = SudokuBoard(self.board_file)
        self.isSolved = False

    def check_win(self):
        ''' 
        Checks to see if board is a win 
        '''

        if self.running_puzzle.is_valid(self.running_puzzle.board, False):
            self.isSolved = True
            return True
        return False 
        
    def user_move(self, row, col, char):
        '''
        Makes the move by placing the char in corresponding row and column 
        '''
        self.running_puzzle.make_move(row, col, char)










