import random
import sys

# controls
gt = ['*'] * 12  # gametable (gt)
winCombo = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
gameOn = 'play'
player, bot = '', ''

# player gets to choose X or O every game.
# the player is gt[10] and the bot is gt[11]
while gt[10] not in ['X', 'x', 'O', 'o']:
    gt[10] = input("Do you want to be 'X' or 'O' \nselect: ").upper()
    print(gt[10])

if gt[10] == 'X':
    gt[11] = 'O'
    player, bot = 'X', 'O'
else:
    gt[11] = 'X'
    player, bot = 'O', 'X'

# who goes first
print("Coin flip...")
flip = random.choice(['X', 'O'])
if flip == player:
    turn = 'player'
    print('player goes first')
else:
    turn = 'bot'
    print('bot goes first')

# display the board in a while loop that exits when the letter 'q' for quit is entered.
while gameOn != 'q':
    def gameTable():
        n = 1
        print("\n| {} | {} | {} |".format(gt[1], gt[2], gt[3]),
              "\n| {} | {} | {} |".format(gt[4], gt[5], gt[6]),
              "\n| {} | {} | {} |".format(gt[7], gt[8], gt[9]),
              )

    def gameover(power):
        sys.exit()

    def winnerCheck(self):
        for win in winCombo:
            # print(gt[win[0]], gt[win[1]], gt[win[2]])
            if gt[win[0]] == gt[win[1]] == gt[win[2]] != '*':
                if gt[win[0]] == player:
                    print('Player wins!')
                    gameover('restart')
                else:
                    print('You lose!')
                    gameover('restart')

                    # for astrix symbols in the gt list, if there are 0 '*' then there are no moves left.
        countAstrix = 0
        for c in range(1,10):
            if gt[c] == '*':
                countAstrix = countAstrix + 1
        if countAstrix == 0:
            print("The Cat won!")
            gameover('restartf')

    gameTable()
    winnerCheck('')

    # turn base mechanics
    move = ''
    print("{}'s turn..".format(turn))
    if turn == 'player':
        # collect the next move and verify the move is legal, i.e.
        # the next legal move is only in a space with an '*' symbol.
        while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            move = input("type a number 1 - 9, or 'q' to quit : "
                         "")
            if move == "q":
                print('quit')
                sys.exit()

        if gt[int(move)] != '*':
            move = 'illegal move'
            print("invalid move, try again")
        else:
            # apply the move and switch turn
            gt[int(move)] = gt[10]
            turn = 'bot'

    elif turn == 'bot':
        # the bot first checks if player is one move away from winning, and blocks it, if found.
        for win in winCombo:
            a, b, c = 0, 0, 0
            for w in win:
                if gt[w] == "*":
                    a = a + 1
                    move = w
                elif gt[w] == player:
                    b = b + 1
                else:
                    c = c + 1
            if a == 1:
                if c == 2: # bot checks for winning move.
                    print(win)
                    break
                elif b == 2:
                    print(win)
                    break
            else:
                move = ''

        # the bot then checks for an open middle spot; gt[5].
        if gt[5] == '*':
            move = int(5)

        # the bot then goes for the corner locations; ['1','3','5','7']
        if move == '':
            for n in ['1','3','5','7','4','6']:
                if gt[int(n)] == '*':
                    move = n
                    break

        gt[int(move)] = gt[11]
        turn = 'player'
