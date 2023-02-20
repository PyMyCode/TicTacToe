import random

class Player:
    def __init__(self, _label) -> None:
        self.label = _label
        self.move = [] # to save player moves

# defining the player's labels
HUMAN = Player("X")
ROBOT = Player("O")

# defining board size
BOARD_SIZE = 3

class TicTacToeGame:

    def __init__(self):
        self.board = [["-" for j in range(BOARD_SIZE)]for i in range(BOARD_SIZE)] # creating the blank board
        self._choosing_starting_player() # first move is for human

    def _choosing_starting_player(self):
        if random.randint(0,1):
            self._human_player_move()
        else:
            self._robot_player_move()

    def _display_board(self):
        for r in self.board:
            for c in r:
                print(c, end=" ")
            print()
    
    def _update_move(self, player, row, col):
        
        # updating the move on the board
        self.board[row][col] = player.label
        
        # displying the board
        self._display_board()

        # saving the player's move
        player.move.append([row, col])

        #check win
        self._win_check(player)

        # draw check
        self._draw_check()

        # switching the player
        self._switch_player(player)

    def _switch_player(self, player):
        
        if player.label == "O":
            # human's move
            self._human_player_move()
        else:
            # robot's move
            self._robot_player_move()

    def _win_check(self, player):
        
        #row check
        for row in self.board:
            if all(x == player.label for x in row):
                # declaring winner
                self._winner(player)

        #col check
        for i in range(BOARD_SIZE):
            if all(x[i] == player.label for x in self.board):
                # declaring winner
                self._winner(player)
        
        # diagonal 1 check
        if all(self.board[x][x] == player.label for x in range(BOARD_SIZE)):
            # declaring winner
            self._winner(player)

        # diagonal 2 check
        if all(self.board[x][BOARD_SIZE - 1 - x] == player.label for x in range(BOARD_SIZE)):
            # declaring winner
            self._winner(player)

    def _winner(self, player):
        if player.label == "X":
            print("You won! :)\n")
        else:
            print("You lost! :(\n")
        
        self._quit()
    
    def _draw_check(self):
        for x in self.board:
            for y in x:
                if y == "-":
                    return
        
        print("It's a draw! :|\n")
        self._quit()

    def _quit(self):
            exit()

    # HUMAN #####################################################################
    def _human_player_move(self):
        
        # counting rounds
        print(f"\nROUND : {len(HUMAN.move) + 1}")
        print("\nYour move:")

        condition = False
        while not condition:
            
            # user input
            try:
                row, col = list(map(int, (input("Enter row and column numbers to fix spot: ").split())))
            
                # check the validity of the input
                condition = True
                if row > 3 or col > 3:
                    condition = False
                    print(f"Number needs to be lesser than {BOARD_SIZE}")
                try:
                    if self.board[row - 1][col - 1] != "-":
                        condition = False
                        print(f"Place already filled")
                except:
                    pass
            except:
                print(f"Incorrect input.Correct format is :r c")
        # updating the human move
        self._update_move(HUMAN, row - 1, col - 1)
    
    # ROBOT #####################################################################
    def _robot_player_move(self): 
        
        print("\nRobot's move:")
        if len(HUMAN.move) == 0 or len(HUMAN.move) == 1: # first move
            while True:
                row = random.randint(0, BOARD_SIZE - 1)
                col = random.randint(0, BOARD_SIZE - 1)
                if self.board[row][col] == "-": # checking for a empty spot
                    self._update_move(ROBOT, row, col)
        
        else: #second move onwards
            "Offensive"
            self._strategy(ROBOT)
            "Defensive"
            self._strategy(HUMAN)
        
    def _strategy(self, player):
        "iterating through all moves"
        for i in range(1, len(player.move)):
                # row strategy
                if player.move[i][0] == player.move[i - 1][0]: #row=0,col=1
                    row = player.move[i][0]
                    for y in range(BOARD_SIZE):
                        if self.board[row][y] == "-": # checking for a empty spot
                            col = y
                            self._update_move(ROBOT, row, col)

                # col strategy
                elif player.move[i][1] == player.move[i - 1][1]:
                    col = player.move[i][1]
                    for x in range(BOARD_SIZE):
                        if self.board[x][col] == "-": # checking for a empty spot
                            row = x
                            self._update_move(ROBOT, row, col)
                
                # diagonal 1 strategy
                elif player.move[i][0] == player.move[i][1] and \
                        player.move[i - 1][0] == player.move[i - 1][1]:
                    for z in range(BOARD_SIZE):
                        if self.board[z][z] == "-": # checking for a empty spot
                            self._update_move(ROBOT, z, z)
                
                # diagonal 2 strategy
                elif player.move[i][0] == (BOARD_SIZE - 1 - player.move[i][1]) and \
                        player.move[i - 1][0] == (BOARD_SIZE - 1 - player.move[i - 1][1]):
                    for z in range(BOARD_SIZE):
                        if self.board[z][BOARD_SIZE - 1 - z] == "-": # checking for a empty spot
                            self._update_move(ROBOT, z, BOARD_SIZE - 1 - z)

def main():
    TicTacToeGame()

if __name__ == "__main__":
    main()
