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

    def __init__(self):






bg = board_game()

bg.print_board_coordinates()
bg.print_board()
print(bg.markers)
bg.mark_board('X', 1)
bg.print_board()
bg.mark_board('O', 2)
bg.print_board()


player_1 = player('X')
print(player_1.marker)
print(player_1.make_move(4))
marker, position = player_1.make_move(4)
bg.mark_board(marker, position)
bg.print_board()



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