from SudokuError import *
class SudokuBoard(object):
    '''
    Sudoku Board representation
    '''
    def __init__(self, board_file):
        self.SPACE_CHAR = '0'
        self.numEmptySpots = 999
        self.board_file = board_file
        self.board = self.initialize_board(board_file)

    def is_valid(self, board, initial):
        '''
        Checks to see if board is a valid configuration 
        '''
        rows = [[False for j in range(9)] for _ in range(9)]
        cols = [[False for j in range(9)] for _ in range(9)]
        box = [[False for j in range(9)] for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == self.SPACE_CHAR and not initial:
                    return False 
                if  board[i][j] != self.SPACE_CHAR:  # Or whatever character for empty space
                    index = ord(board[i][j]) - ord('1')   # because of zero indexing
                    boxIndex = i//3 * 3 + j//3
                    if rows[index][i] or cols[index][j] or box[index][boxIndex]:
                        return False
                    rows[index][i] =  cols[index][j] = box[index][boxIndex] = True

        return True

    def count_char(self, board):
        '''
        Returns the count of a particular character in board. Used to calculate
        number of empty spaces on board. 
        '''
        return sum([i.count(self.SPACE_CHAR) for i in board])

    def make_move(self, row, col, char):
        '''
        Inserts specific char at specific row and column. Updates numEmptySpots
        as necessary. 
        '''
        if self.board[row][col] == self.SPACE_CHAR and char != self.SPACE_CHAR:
            self.numEmptySpots -= 1
        self.board[row][col] = char

    def initialize_board(self, board_file):
        '''
        Initializes board by reading from file. Also checks if input board is valid.
        If input board is invalid, returns a custom Sudoku Error specifying the error 
        '''
        board = []
        inputFile = open(board_file)
        for line in inputFile:
            chars = list(line)
            if chars[-1] == '\n':
                chars.pop()
            if len(chars) != 9:
                board = []
                raise SudokuError("Each line in sudoku puzzle must be 9 characters long.")
            for c in chars:
                if not c.isdigit() or int(c) < 0 or int(c) > 9:
                    raise SudokuError("Each line must consist of numbers from 0 - 9.")
            board.append(chars)
        if len(board) != 9:
            raise SudokuError("Each board must be 9 rows.")

        if not self.is_valid(board, True):
            raise SudokuError("Board configuration has repeats and thus invalid. ")
        self.numEmptySpots = self.count_char(board)
        return board
