import argparse

from gomoku.player import Player
from gomoku.color_print import *
from gomoku.env import GomokuEnv, Action


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', default=5, type=int, required=False, help='size of the game board')
    return parser.parse_args()


def main():
    args = parse_args()

    assert args.size > 4, f'the board must be at least 4x4: {args.size}x{args.size}'
    welcome_string = f'Welcome to play Gomoku {args.size}x{args.size}!\nRules: whoever creates a line with 5 stones first wins! Black goes first!'
    print_system_message(welcome_string)
    print_system_message('Who want to play first?')
    player_1_name = input('Please enter the name of the first player: ')
    player_2_name = input('Please enter the name of the second player: ')
    player_1_name = player_1_name.replace(' ', '').lower()
    player_2_name = player_2_name.replace(' ', '').lower()

    players = {
        player_1_name: Player(name=player_1_name),
        player_2_name: Player(name=player_2_name)
    }

    env = GomokuEnv(size=args.size, player_1_name=player_1_name, player_2_name=player_2_name)
    episode = 1
    end_game = False
    while not end_game:
        done = False
        env.reset()
        
        player_name = player_1_name
        while not done:
            env.render()

            player_input = input(f"Player {player_name}'s move [x,y] (e.g '0,1') or quit [q]: ")
            player_input = player_input.replace(' ', '')  # remove unneccessary space
            inputs = player_input.split(',')
            try:
                if len(inputs) == 2:
                    x, y = inputs
                elif len(inputs) == 1 and inputs[0].lower() == 'q':
                    done = True
                    end_game = True
                    break
                else:
                    raise ValueError

                color = 'b' if player_name == player_1_name else 'w'

                action = Action(x=int(x), y=int(y), color=str(color))

                _, _, done, info = env.step(player_name=player_1_name, action=action)
                if not done:
                    if player_name == player_1_name:
                        player_name = player_2_name
                    else:
                        player_name = player_1_name
            except Exception:
                # catch any step() errors or inputs errors
                print_error_message('invalid move. please try again')

        if not end_game:
            env.render()
            if 'draw' not in info:
                print_system_message(f'{player_name} wins!!!!')
                players[player_name].score += 1
            else:
                print_system_message('draw')
            print_system_message(f"end of episode {episode} {player_1_name}'s score {players[player_1_name].score} {player_2_name}'s score {players[player_2_name].score}")
            episode += 1
        else:
            print_system_message(f'{player_name} gives up. end of the game.')


if __name__ == '__main__':
    main()