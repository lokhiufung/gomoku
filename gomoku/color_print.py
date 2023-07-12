from enum import Enum

class Color(Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    WHITE = '\033[97m'  
    GREY = '\033[90m' 

def colorize(color, text):
    color_code = Color.RESET.value
    for supporting_color in Color:
        if supporting_color.name == color:
            color_code = supporting_color.value
    return color_code + text + supporting_color.RESET.value

def color_print(color, text):
    text = colorize(color, text)
    print(text)

def print_system_message(message):
    color_print('GREEN', message)

def print_error_message(message):
    color_print('RED', '[ERROR]: ' + message)

def print_game_board(game_board):
    color_print('YELLOW', game_board)

def print_player_prompt(prompt):
    color_print('CYAN', prompt)

    