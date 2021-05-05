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

        self.first_row_state = re.sub(r'\d', ' ', self.first_row)
        self.second_row_state = re.sub(r'\d', ' ', self.second_row)
        self.third_row_state = re.sub(r'\d', ' ', self.third_row)
    

    def print_board_coordinates(self):
        print('Board Coordinates:\n')
        print(" " + self.first_row)
        print(" ---|---|---")
        print(" " + self.second_row)
        print(" ---|---|---")
        print(" " + self.third_row)
        print('\n')

    # def _render_state

    def print_board(self):
        print('Board:\n')
        print(" " + self.first_row_state)
        print(" ---|---|---")
        print(" " + self.second_row_state)
        print(" ---|---|---")
        print(" " + self.third_row_state)
        print('\n')



bg = board_game()
# bg.print_board_coordinates()
# bg.print_board()

marker = {'X': [1],
           'O': [3]}

def _render_row_state(row, marker):

    for k in marker.keys():
        for v in marker[k]:
            row = row.replace(str(v), k)
    row = re.sub(r'\d', ' ', row)
    
    return row


print(_render_row_state(bg.first_row, marker))

#  O | X | X
# ---|---|---
#    | O |
# ---|---|---   
#    | X |

#  1 | 2 | 3
# ---|---|---
#  4 | 5 | 6
# ---|---|---   
#  7 | 8 | 9