ttt_dic = {int(key): str(key) for key in range(1,10)}
print(ttt_dic)

class tic_tac_toe(object):
    def __init__(self,dic):
        self.dic = dic  
    def draw_board(self,dic):
        print(dic[1] + ' | ' + dic[2] + ' | ' + dic[3])
        print('----------')
        print(dic[4] + ' | ' + dic[5] + ' | ' + dic[6])
        print('----------')
        print(dic[7] + ' | ' + dic[8] + ' | ' + dic[9])

def user_move(dict):
    my_value = input('Your move. Pick the number of an unoccupied space')
    while  (my_value in dict.values()) is False:
        my_value = input('Please select again. This space is occupied or out of range')
    else:
        dict[int(my_value)] = 'X'
        print(dict)

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
    return False
    
    ##No open spaces left. Game over
    if (sum(1 for value in dict.values() if value == 'X' or value == 'Y')) == 9:
        print('Game over: No other move is possible. Tie')

my_game = tic_tac_toe(ttt_dic)
my_game.draw_board(ttt_dic)
