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

        _valid_play = 0

        while _valid_play != 1:

            if marker not in ['X', 'O']:
                print('Wrong marker try again!')

            elif position not in self.positions or position not in self.avaliable_positions:
                position = int(input('Invalid move, choose another position\n'))

            else:    
                _valid_play = 1
                print("Valid play")
                self.markers[marker].append(position)
                self.avaliable_positions.remove(position)

        return position


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
        self.winner = False


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

        self.adversary_positions.append(position)


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
        self.play_count = 0
        self.game_winning_outcome = None


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
        self.play_count += 1


    def _check_winning_condition(self, player):
        """
        """

        for w in self.winning_condition:
            if set(w).issubset(player.owned_positions):
                player.winner = True
                print('Player', player.marker, 'has won')
                self.game_won = True
                self.game_winning_outcome = player.marker
                break

        if self.play_count == 8 and  not self.game_won:
            self.game_winning_outcome = "Draw"
            print('DRAW!!!')

    
    def _play_game(self, position):
        """
        """
        
        _player = self._players[self._player_time]
        _other_player = self._players[(self._player_time + 1) % 2]
        _move = _player.make_move(position)
        _mark = _player.marker    
        
        # Actions
        new_position = self._board.mark_board(_mark, position)

        _player.ack_own_position(new_position)
        _other_player.look_adversary_position(new_position)

        self._check_winning_condition(_player)



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

stop_game = False

while not stop_game:
    player = game._player_time + 1
    game._board.print_board_coordinates()
    game._board.print_board()
    move = int(input(f'Player {player} choose a position:\n'))
    game._play_game(move)
    game._change_player_time()
    if game.game_won == True or game.game_winning_outcome == 'Draw':
        stop_game = True 

game._board.print_board()


# jogada = 0 


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
