#!usr/bin/env python3
import re
 
class board_game():

    def __init__(self):
        
        self.first_row = " 1 | 2 | 3"
        self.second_row = " 4 | 5 | 6"
        self.third_row = " 7 | 8 | 9"
        
        self.rows = [self.first_row,
                     self.second_row,
                     self.third_row ]
        
        self.markers = {'X': [],
                        'O': []}
        
        self.positions = [1, 2, 3,
                          4 ,5 ,6,
                          7, 8, 9]

        self.avaliable_positions = [1, 2, 3,
                                    4 ,5 ,6,
                                    7, 8, 9]
    

    def print_board_coordinates(self):
        
        print('Board Coordinates:\n')
        print(" " + self.first_row)
        print(" ---|---|---")
        print(" " + self.second_row)
        print(" ---|---|---")
        print(" " + self.third_row)
        print('\n')


    def _render_row_state(self, row, marker):

        for k in marker.keys():
            for v in marker[k]:
                row = row.replace(str(v), k)
        row = re.sub(r'\d', ' ', row)
        
        return row


    def print_board(self):

        row_states = []
        for i , r in enumerate(self.rows):
            temp = self._render_row_state(r, self.markers)
            row_states.append(temp)
        
        print('Board:\n')
        print("    |   |    ")
        print(" " + row_states[0])
        print("----|---|----")
        print(" " + row_states[1])
        print("----|---|----")
        print(" " + row_states[2])
        print("    |   |    ")
        print('\n')


    def mark_board(self, marker, position):

        if marker not in ['X', 'O']:
            print('Wrong marker try again!')

        elif position not in self.positions:
            print('Invalid move')
        
        elif position not in self.avaliable_positions:
            print("Position already taken, choose another")

        else:    
            self.markers[marker].append(position)
            self.avaliable_positions.remove(position)


class player():
    
    def __init__(self, marker, first_play = False):
        
        assert marker in ['X', 'O'], f'Marker not allowed'
        self.marker = marker

        self._first_play = first_play
        self.owned_positions = []
        self.adversary_positions = []
        self.avaliable_positions = [1, 2, 3,
                                    4, 5, 6,
                                    7, 8, 9]


    def make_move(self, position):

        mark = self.marker
        return mark, position

    def ack_own_position(self, position):

        self.owned_positions.append(position)

    def look_adversary_position(self, position):

        self.adversary_position.append(position)

    def look_game_board(self, avaliable_positions):

        self.avaliable_positions = avaliable_positions


class game():

    def __init__(self, players):
        self._players = players
        # self

    # def 



print('\nPlayer 1 choose between markers X or O')
game_markers = ['X', 'O']

marker_player_1 = input('')

dumb_player_count = 0
while marker_player_1 not in game_markers:
    print('You didnt chose a valid marker try again!')
    marker_player_1 = input('')
    dumb_player_count += 1
    
    if dumb_player_count == 2:
        exit('You are boring go play Tibia!')


player_1 = player(marker_player_1)
marker_player_2 = [_ for _ in game_markers if _ != marker_player_1][0]
player_2 = player(marker_player_2)


print(f'\nPlayer 1 marker: {player_1.marker}')
print(f'Player 2 marker: {player_2.marker}\n')


print('Are you going to choose who plays first or should we chose randomly?')
_ = input('press R for randomly picking the fisrt player:\n')

if _ in ['r', 'R']:
    
# print('\nPlayer 1 choose your marker:')



# player_1 = player('X')
# player_2 = player('O')

# bg = board_game()

# bg.print_board_coordinates()
# bg.print_board()

# print(player_1.marker)
# print(player_1.make_move(4))
# marker, position = player_1.make_move(4)
# bg.mark_board(marker, position)
# bg.print_board()



#    |   |
#  O | X | X
#----|---|----
#    | O |
#----|---|----   
#    | X |
#    |   |

#  1 | 2 | 3
# ---|---|---
#  4 | 5 | 6
# ---|---|---   
#  7 | 8 | 9