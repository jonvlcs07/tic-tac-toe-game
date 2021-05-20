#!usr/bin/env python3
import re
import numpy as np
 
class Board_Game():

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


class Player():
    
    def __init__(self, marker, first_play = False):
        
        assert marker in ['X', 'O'], f'Marker not allowed'
        
        self.marker = marker

        self._first_play = first_play
        self.owned_positions = []
        self.adversary_positions = []
        self.avaliable_positions = [1, 2, 3,
                                    4, 5, 6,
                                    7, 8, 9]


    def __repr__(self):
        return "Player()"


    def __str__(self):
        return f"Player {self.marker}"


    def make_move(self, position):

        mark = self.marker
        return mark, position


    def ack_own_position(self, position):

        self.owned_positions.append(position)


    def look_adversary_position(self, position):

        self.adversary_position.append(position)


    def look_game_board(self, avaliable_positions):

        self.avaliable_positions = avaliable_positions


class Game():

    def __init__(self, players, board):
        self._players = players
        self._board = board
        self.winning_condition = [[1, 2, 3],
                                  [4, 5, 6], 
                                  [7, 8, 9], 
                                  [1, 4, 7],
                                  [2, 5, 8],
                                  [3, 6, 9],
                                  [1, 5, 9],
                                  [3, 5, 7]]   
        self.game_won = False


    def choose_first_player(self, first_player: int):
        """
        """

        self._players[first_player]._first_play = True
        self._first_player = first_player + 1
        self._player_time = first_player


    def _change_player_time(self):
        """
        """

        self._player_time = (self._player_time + 1) % 2


    def _check_wining_condition(self, player):
        """
        """

        for w in self.winning_condition:
            if set(w).issubset(player.owned_positions):
                print('Player ', player.marker, 'has won')

    
    def _play_game(self, position):
        """
        """
        
        _player = self._players[self._player_time]
        _move = _player.make_move(position)
        _mark = _player.marker    
        self._board.mark_board(_mark, position)
        print(move)



# Main Game

# Game beggining who plays first and markers attribution
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


player_1 = Player(marker_player_1)
marker_player_2 = [_ for _ in game_markers if _ != marker_player_1][0]
player_2 = Player(marker_player_2)


print(f'\nPlayer 1 marker: {player_1.marker}')
print(f'Player 2 marker: {player_2.marker}\n')

board = Board_Game()
game = Game([player_1, player_2], board)


print('Are you going to choose who plays first or should we chose randomly?')
_ = input('press R for randomly picking the first player:\n')

if _ in ['r', 'R']:
    idx = np.random.choice([0, 1])
    game.choose_first_player(idx) 
    print(f"\nPlayer {idx + 1} plays first")


else:
    _ = input('Press 1 if you want to Player 1 to start:\n')

    if _ == '1':
        game.choose_first_player(0) 
        print(f"Player 1 plays first")
    else:
        game.choose_first_player(1) 
        print(f"Player 2 plays first")


game._board.print_board()
game._board.print_board_coordinates()
move = int(input('Choose a position:\n'))
game._play_game(move)
game._board.print_board()

jogada = 0 
# for _ in range(10):
#     print('Vez do jogador', game._player_time + 1)
#     game._change_player_time()





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
