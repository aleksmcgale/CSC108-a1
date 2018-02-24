EMPTY = '-'

def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.3, 0.5, 2)
    True
    >>> is_between(0, 2, 3)
    False
    """
    
    return min_value <= value <= max_value

    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.

def game_board_full(game_board):
    """(str)-> bool
    
    Return True if and only if the EMPTY character is not in game_board;
    otherwise return False.
    
    >>>game_board_full('----')
    False
    >>>game_board_full('XOXO')
    True
    """
    
    return not EMPTY in game_board
       

def get_board_size(game_board):
    '''(str) -> int
    
    Precondition: The value of the length of game_board is a perfect square.
    
    Return the square root of game_board to find the length of the game boards 
    sides.
    
    >>>get_board_size('XXXX')
    2
    >>>get_board_size('XXXXXXXXX')
    3
    '''
    
    return int(len(game_board) ** 0.5)


def make_empty_board(board_size):
    '''(int)-> str
    
    Precondition: 1 <= board_size <= 9
    
    Return the EMPTY character multiplied by the board_size.
    
    >>>make_empty_board(2)
    '----'
    >>>make_empty_board(3)
    '---------'
    '''
    
    return EMPTY * (board_size ** 2)
    
    
def get_str_index(row_index, column_index, board_size):
    ''' 
    (int, int, int) -> int
    
    Return the correlation between the row_index, column_index and board_size,
    thus calculating the str_index.
    
    >>>get_str_index(2, 1, 3)
    3
    >>>get_str_index(3, 3, 3)
    8
    '''
    
    return (row_index - 1) * board_size + (column_index - 1)

def make_move(player_symbol, row_index, column_index, board_game):
    '''
    (str, int, int, str) -> str
    
    Return player_symbol in a str_index, specified by the row_index and
    column_index. str_index must contain an EMPTY value on the board_game. 
    If string_index holds a player_symbol, return board_game.
    
    >>> make_move('X', 1, 1,'-')
    'X'
    >>>make_move('X', 1, 1, '----')
    'X---'
    '''
    board_size = get_board_size(board_game)
    str_index = get_str_index(row_index, column_index, board_size)
    if board_game[str_index] == EMPTY:
        return board_game[0:str_index] + player_symbol \
               + board_game[(str_index + 1):]
    
    # board_size is the value of the str_index that identifies the location of 
    # where the player_symbol will be added
   
def extract_line(game_board, move, board_game):
    '''(str, str, int) -> str
    
    Return string of characters in game_board specified by board_game and move.
    Parameter move refers to the direction of the extracted string, while
    board_game refers to the specific column or row in which the string begins.
            
    >>>extract_line('X-OX', 'across', 1)
    'X-'
    >>>extract_line('X-OX', 'down', 2)
    '-X'
    >>>extract_line('X-OX', 'down_diagonal',1)
    'XX'
    '''
    
    board_size = get_board_size(game_board)
    if move == 'across':
        lower = int((board_game - 1) * board_size)
        upper = int(board_game * board_size)
        return game_board[lower:upper]
    
    # lower and upper provide the boundaries for slicing the string
    
    elif move == 'down':
        lower = board_game - 1
        difference = int(board_size)
        return game_board[lower::difference]
    
    # lower provides the minimum boundary for the string; return next character
    # by increasing by difference, till the end of the string
    
    elif move == 'up_diagonal':
        lower = int(-(board_size))
        difference = int(-(board_size - 1))
        upper = int(-(board_size ** 2))
        return game_board[lower:upper:difference]
    
    # lower provides the minimum boundary for the string; return next character 
    # by increasing by difference, till upper
    
    else:
        difference = int(board_size + 1)
        return game_board[::difference]
    
    # return next character by increasing by difference