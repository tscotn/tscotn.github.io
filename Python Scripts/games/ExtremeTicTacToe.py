import itertools

class Board:
    square_loc = ['top_left', 'top_center', 'top_right', 'middle_left', 'middle_center', 'middle_right', 'bottom_left', 'bottom_center', 'bottom_right']
    board = {
        square_loc[0]: '_', square_loc[1]: '_', square_loc[2]: '_',
        square_loc[3]: '_', square_loc[4]: '_', square_loc[5]: '_',
        square_loc[6]: '_', square_loc[7]: '_', square_loc[8]: '_'
    }
    
    def ChooseSquare(self, player):
        square = int(input('Which square do you want to play in? (1-9): '))-1
        if player not in [1,2]:
            print('invalid player number')
        elif player == 1:
            self.board[self.square_loc[square]] = 'X'
        elif player == 2:
            self.board[self.square_loc[square]] = 'O'
    
#    def PrintBoard(self, end=False):
#        for loc in board_loc:
#            if board_loc.index(loc) in [2, 5, 8]:
#                print(self.board[loc])
#            else:
#                print(self.board[loc]  + '|', end='')


class ExtremeBoard:
    board_loc = ['top_left', 'top_center', 'top_right', 'middle_left', 'middle_center', 'middle_right', 'bottom_left', 'bottom_center', 'bottom_right']
    
    extreme_board = dict.fromkeys(board_loc, Board())
    
    def RenderExtremeBoard(self):
        for x in range(3):
            for k in range(3):
                print('\n')
                for j in range(3):
                    print(' ', end='')
                    for i in range(0+k*3,3+k*3):
                        square = extreme_board[board_loc[(x*3)+j]].board[board_loc[i]]
                        if i == (3+k*3)-1:
                            print(square, end='')
                        else:
                            print(square, end='|')
    
    def ChooseBoard()
        playerChoice = input('')
        while playerChoice not in validBoards:
            !!!doSomething()

#extreme_board = [Board() for Board() in range(0, 9)]
#
#for board in extreme_board:
#    board.PrintBoard()
#
#def PlayGame():

#def RenderBoard():
#    boards = [i for i in range(9)]
#    for i in range(9):
#        boards[i] = [(str(i) + '_' + str(j)) for j in range(9)]
#    return boards
#

def PrintBoard(boards):
    for board in boards:
        for square in board:
            if board.index(square) in [2,5,8]:
                print(board.index(square))
#                print(square + '|', end='')
#            else:
#                print(square)


#Okay the way this prints needs to be a little funky.
#it goes print(board[0][0] + board[0][1] + board[0][2]) for the first three squares of the first board...then it needs to print print(board[1][0] + board[1][1] + board[1][2]) and so on. So the pattern for i is 0, 1, 2 with j = 0, 1, 2

for i in range(len(boards)):
    for j in range(len(boards[i]) - 2):
        print(boards[i][j] + '|' + boards[i][j+1] + '|' + boards[i][j+2])


if __name__ == '__main__':
    PlayGame()

# It needs to look like this:
#0_0|0_1|0_2 __ 1_0|1_1|1_2 __ 2_0|2_1|2_2
#0_3|0_4|0_5 __ 1_3|1_4|1_5 __ 2_3|2_4|2_5
#0_6|0_7|0_8 __ 1_6|1_7|1_8 __ 2_6|2_7|2_8

#3_0|3_1|3_2 __ 4_0|4_1|4_2 __ 5_0|5_1|5_2
#3_3|3_4|3_5 __ 4_3|4_4|4_5 __ 5_3|5_4|5_5
#3_6|3_7|3_8 __ 4_6|4_7|4_8 __ 5_6|5_7|5_8

#6_0|6_1|6_2 __ 7_0|7_1|7_2 __ 8_0|8_1|8_2
#6_3|6_4|6_5 __ 7_3|7_4|7_5 __ 8_3|8_4|8_5
#6_6|6_7|6_8 __ 7_6|7_7|7_8 __ 8_6|8_7|8_8

#this represents the board rendering logic:
for x in range(3):
    for k in range(3):
        print('\n')
        for j in range(3):
            print(' ', end='')
            for i in range(0+k*3,3+k*3):
                if i == (3+k*3)-1:
                    print(str((x*3)+j) + '_' + str(i), end='')
                else:
                    print(str((x*3)+j) + '_' + str(i), end='|')



#Steps:
#1) render board
#2) ask player 1 which board they want to play in
#3) ask player 1 which square they want to play in
#4) determine whether player 1 has won a board or not
#5) determine whether player 1 has won the game or not
#6) render board with player 1's new move
#7) tell player 2 which board they must play in (if the board they must play in is full, ask player 2 which board they want to play in. Ask until they choose a valid board)
#8) ask player 2 which square (0-9) they wish to play in
#9) determine whether player 2 has won a board or not
#10) determine whether player 2 has won the game or not
#11) repeat


XXX
XXX
XXX

012
345
678


#loop through these, and if any are the same...or,

square_loc = ['top_left', 'top_center', 'top_right', 'middle_left', 'middle_center', 'middle_right', 'bottom_left', 'bottom_center', 'bottom_right']
board = {
    square_loc[0]: '_', square_loc[1]: '_', square_loc[2]: '_',
    square_loc[3]: '_', square_loc[4]: '_', square_loc[5]: '_',
    square_loc[6]: '_', square_loc[7]: '_', square_loc[8]: '_'
}

board



#This gives the location of each token that contains either X or O
def CheckWinner():
    won = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)]
    for token in ['X', 'O']:
        if any(x in won for x in itertools.combinations([square_loc.index(loc) for loc, square in board.items() if square==token], 3)):
            return(token)
        
any(i in won for i in itertools.combinations([square_loc.index(loc) for loc, square in board.items() if square=='O'],3))
    
itertools.combinations([square_loc.index(loc) for loc, square in board.items() if square=='X'],3)





any(i in a for i in b)
