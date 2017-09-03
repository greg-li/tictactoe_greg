import random

class tic_tac_toe(object):
    def __init__(self,dic):
        self.dic = dic  
    def draw_board(self,dic):
        print(dic[1] + ' | ' + dic[2] + ' | ' + dic[3])
        print('----------')
        print(dic[4] + ' | ' + dic[5] + ' | ' + dic[6])
        print('----------')
        print(dic[7] + ' | ' + dic[8] + ' | ' + dic[9])


def select_player():
    select_player = input('Type X to play as Player 1 and go first. Type O to play as player 2 and go second')
    if select_player == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
def user_move(dict,play_as):
    my_value = input('Your move. Pick the number of an unoccupied space')
    while  (my_value in dict.values()) is False:
        my_value = input('Please select again. This space is occupied or out of range')
    else:
        dict[int(my_value)] = play_as

def computer_move(dict,play_as):
    from random import randint  
    comp_move = randint(min(dict.keys()),max(dict.keys()))
    while (str(comp_move) in dict.values()) is False:
        comp_move = randint(min(dict.keys()),max(dict.keys()))
    else:
        dict[comp_move] = play_as                        

def end_game(dict):
    for i in dict.keys():
        ##Check if there is a victory by row
        if i+2 not in dict.keys():
            pass
        else:
            if dict[i] == dict[i+1] == dict[i+2] and (i+2)%3==0:
                print('Game over ' + dict[i] + ' wins')
                return True
        ##Check if there is a victory by column
        if i+6 not in dict.keys():
            pass
        else:
            if dict[i] == dict[i+3] == dict[i+6]:
                print('Game over ' + dict[i] + ' wins')
                return True
    ##Special cases: Diagnols         
    if dict[1] == dict[5] == dict[9] or dict[3] == dict[5] == dict[7]:
        print('Game over ' + dict[5] + ' wins')
        return True
    
    ##No open spaces left. Game over
    if (sum(1 for value in dict.values() if value in ('X','O'))) == 9:
        print('Game over: No other move is possible. Tie')
        return True

    return False

def game_play():
    ##Define players
    players = select_player()
    user = players[0]
    computer = players[1]


    ##Main game play
    ttt_dic = {int(key): str(key) for key in range(1,10)}
    my_game = tic_tac_toe(ttt_dic)
    ##Show intial board
    my_game.draw_board(ttt_dic)
    last_move = ''

    ##Main loop alternates between computer and user
    for i in range(1,max(ttt_dic.keys())):
        ##first move
        if user == 'X' and i == 1:
            user_move(ttt_dic,user)
            last_move = user
        if user == 'O' and i == 1:
            computer_move(ttt_dic,computer)
            print('The computer just moved.')
            my_game.draw_board(ttt_dic)
            last_move = computer
        ##All subsequent moves)
        if last_move == user:
            computer_move(ttt_dic,computer)
            print('The computer just moved.')
            my_game.draw_board(ttt_dic)
            last_move = computer 
        else: 
            user_move(ttt_dic,user)
            last_move = user
        if end_game(ttt_dic) is True:
            break
                                
game_play()

