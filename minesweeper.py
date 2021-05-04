import random

# lets create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object" or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # let's keep track of these parameters. They'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # let's create the board
        # helper function
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()
       

        # initialize a set to keep track og which locations we've uncovered
        # we'll save (row, col) tuples into this set
        self.dug = set()    # if we dig at 0, 0, then self.dug = {(0,0)}

    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here (or whatever representation you prefer
        # but since we have a 2-D board, list of lists is most natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # this creates an array like this:
        # [[None, None, ..., None]],
        #   [None, None, ..., None],
        #   [...                  ],
        #   [None, None, ..., None]
        # we can see how this represents a board

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)    # return a random integer N such that a <= N <= b
            row = loc // self.dim_size  # we want the number of times dim_size goes into loc to tell us
            col = loc % self.dim_size   # we want the remainder to tell us what index in that row to look for

            if board[row][col] == '*':
                # this means we've actually planted a bomb there already so keep going
                continue

            board[row][col] = '*'   # plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # now that we have the bombs planted, we assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. We can precompute these and it'll save us some
        # effort checking what's around the board later on
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    # if this is already a bomb, we don't want to calculate everything
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # lets iterate through each of the neighboring positions and sum number of bombs
        #   top left: (row - 1, col - 1)
        #   top middle: (row - 1, col)
        #   top right: (row - 1, col + 1)
        #   left: (row, col - 1)
        #   right: (row, col + 1)
        #   bottom left: (row + 1, col - 1)
        #   bottom middle: (row + 1, col)
        #   bottom right: (row + 1, col + 1)

        # make sure not to go out of bounds!

        num_neighboring_bombs = 0
        for r in random(max(0, row - 1), min(self.dim_size -1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    # our original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs
                
    def dig(self, row, col):
        # dig at that location
        # return True if successful dig, False if bomb dug

        # a few scenarios:
        #   hit a bomb -> game over
        #   dig at location with neighboring bombs -> finish dig
        #   dig at location with no neighboring bombs -> recursively dig neighbors

        self.dug.add((row, col))    # keep track that we dug here

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row - 1), min(slef.dim_size, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue    # dont't dig where you've already dug
                self.dig(r, c)

        # if our initial dig didn't hit a bomb, we *shouldn't* hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if yuo call print on this object
        # it'll print out what this function return!
        # retrun a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(Self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
                string_rep = ''
        
        #get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
        
        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []

# play the game
def play(dim_size = 10, num_bombs = 10):
    # Step 1: create the board and plant the bombs
    boar = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #           is nect to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig --> Victory!
    pass