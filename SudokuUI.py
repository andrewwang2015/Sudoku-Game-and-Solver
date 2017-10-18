from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
MARGIN = 18
SIDE = 62
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9
class SudokuUI(Frame):
    '''
    The TKINTER UI, responsible for drawing the board and accepting user input.
    '''
    def __init__(self, parent, game):
        self.game = game
        self.parent = parent
        Frame.__init__(self, parent)

        self.row, self.col = 0, 0
        self.initUI()

    def initUI(self):
        ''' 
        Sets up the actual user interface 
        '''
        self.parent.title("Sudoku")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        restart_button = Button(self, text = "Reset Board", command=self.restart, font = ("Helvetica", 12),
            fg = "Gray")
        restart_button.pack(fill=BOTH, side=BOTTOM)

        self.draw_grid()
        self.draw_puzzle()

        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.canvas.bind("<Key>", self.key_pressed)

    def draw_grid(self):
        '''
        Draws grid divided with blue lines into 3x3 squares
        '''
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            # vertical lines
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN 
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            # horizontal lines
            x0 = MARGIN
            y0 = MARGIN + i * SIDE 
            x1 = WIDTH - MARGIN 
            y1 = MARGIN + i * SIDE 
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def draw_puzzle(self):
        '''
        Draws puzzle by filling in cells with pre-filled numbers defined
        in board 
        '''
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                answer = self.game.running_puzzle.board[i][j]
                if answer != self.game.running_puzzle.SPACE_CHAR:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    original = self.game.start_puzzle.board[i][j]
                    color = "black" if answer == original else "sea green"
                    self.canvas.create_text(
                        x, y, text = answer, tags = "numbers", fill = color)


    def restart(self):
        '''
        Restarts the game and returns it to original gameboard form
        '''
        self.canvas.delete("victory")
        self.canvas.delete("winner")
        self.game.start()

        self.draw_puzzle()

    def cell_clicked(self, event):
        if self.game.isSolved:
            return
        x, y = event.x, event.y 
        if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()

            # Get corresponding cell 
            row, col = int((y - MARGIN) / SIDE), int((x - MARGIN) / SIDE)

            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            elif self.game.start_puzzle.board[row][col] == self.game.running_puzzle.SPACE_CHAR:
                self.row, self.col = row, col 
        self.draw_cursor()

    def draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col+1) * SIDE - 1
            y1 = MARGIN + (self.row+1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1, outline = "red", tags = "cursor")

    def key_pressed(self, event):
        if self.game.isSolved:
            return
        if self.row >= 0 and self.col >= 0 and event.char in '1234567890':
            self.game.user_move(self.row, self.col, event.char)
            self.col, self.row = -1, -1
            self.draw_puzzle()
            self.draw_cursor()
            if self.game.check_win():
                self.draw_victory()

    def draw_victory(self):
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(x0, y0, x1, y1, tags = "victory", fill = 'dark orange', outline = "orange")

        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(
            x, y,
            text = "You win!", tags = "winner", fill = "white",
            font = ("Arial", 32))



