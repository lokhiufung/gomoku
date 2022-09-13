# Gomoku



## Rules
- placing a stone of their color on an empty intersection
- black play first
- first player to form an unbroken chain of five stones horizontally, vertically or diagonally
- a line of more than five stones of the same color created does not result in a win


## User requirements
- renederring a game board (a variable size square board)
- instructions for players at each step
- player can stop at anytime
- show progress of the game
- players can choose whether they play the next round at the end of each round


## OOP
- game board (done)
- stone (dropped)
- player (done; may drop it later)
- env (done)


## env.method
- check_end_game()
- check_valid_move()
- render() (done)
- reset() (done)
- step() (done)

## error handling
- InvalidMoveError
- InvalidPlayerError

## TODO
- player can only play with his own color
