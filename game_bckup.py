
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
        self._human_player_move() # first move is for human

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
        
        self._play_or_quit()
    
    def _play_or_quit(self):
        if input("Play again ?[y/n] : ") == "y":
            self.__init__()
        else:
            exit()

    # HUMAN #####################################################################
    def _human_player_move(self):
        
        # counting rounds
        print(f"\nROUND : {len(HUMAN.move) + 1}")
        print("\nYour move:")

        condition = False
        while not condition:
            
            # user input
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
        
        # updating the human move
        self._update_move(HUMAN, row - 1, col - 1)
    
    # ROBOT #####################################################################
    def _robot_player_move(self): 
        
        print("\nRobot's move:")

        "Defensive moves"
        n = len(HUMAN.move)
        
        "First move"
        if n == 1: # first move
            for x in range(BOARD_SIZE):
                for y in range(BOARD_SIZE):
                    if self.board[x][y] == "-": # checking for a empty spot
                        self._update_move(ROBOT, x, y)
        else:
            for i in range(n - 1):
                # row defence
                if HUMAN.move[i][0] == HUMAN.move[i - 1][0]: #row=0,col=1
                    print("strategy row")
                    row = HUMAN.move[i][0]
                    for y in range(BOARD_SIZE):
                        if self.board[row][y] == "-": # checking for a empty spot
                            col = y
                            self._update_move(ROBOT, row, col)

                # col defence
                elif HUMAN.move[i][1] == HUMAN.move[i - 1][1]:
                    print("strategy col")
                    col = HUMAN.move[i][1]
                    for x in range(BOARD_SIZE):
                        if self.board[x][col] == "-": # checking for a empty spot
                            row = x
                            self._update_move(ROBOT, row, col)
                
                # diagonal 1 defence
                elif HUMAN.move[i][0] == HUMAN.move[i][1] and HUMAN.move[i - 1][0] == HUMAN.move[i - 1][1]:
                    for z in range(BOARD_SIZE):
                        if self.board[z][z] == "-": # checking for a empty spot
                            self._update_move(ROBOT, z, z)
                
                # no defence
                else:
                    pass
                    #TODO:d2 defence

            # no defence
            for x in range(BOARD_SIZE):
                for y in range(BOARD_SIZE):
                    if self.board[x][y] == "-": # checking for a empty spot
                        self._update_move(ROBOT, x, y)

def main():
    game = TicTacToeGame()

if __name__ == "__main__":
    main()
