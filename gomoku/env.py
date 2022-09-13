from typing import List, Tuple

from gomoku.board import Board
from gomoku.action import Action


class GomokuEnv:
    def __init__(self, size: int, player_1_name: str, player_2_name: str):
        self.size = size
        self.player_black_name = player_1_name
        self.player_white_name = player_2_name

        self.history = []

        self.board = Board(size)
        
    def reset(self):
        self.history = []
        self.board = Board(self.size)

    def step(self, player_name: str, action: Action) -> Tuple[List[List[str]], float, bool, str]:
        if self.history:
            last_player, _ = self.history[-1]
            assert last_player != player_name  # cannot take a step consecutive

        # check_move()
        assert 0 <= action.x < self.board.n
        assert 0 <= action.y < self.board.n
        assert action.color in ['w', 'b']
        assert self.board[action.x][action.y] == '*'  # hardcoded

        self.board.update_board(action.x, action.y, action.color)

        
        reward = 0.0  # TODO: need update reward if done
        state = self.board.get_board()
        done, patterns = self.check_done(action.x, action.y, action.color)
        info = ','.join(patterns)
        return state, reward, done, info

    def check_done(self, x: int, y: int, color: str) -> Tuple[bool, str]:
        # check if done after place a stone with color at (x, y)
        board = self.board.get_board()
        def check_horizontal_line(board: List[List[str]], x: int, y: int, color: str):
            count = 0
            l = y
            while l >= 0 and board[x][l] == color:
                count += 1
                l -= 1
            
            r = y + 1  # already counted the (x, y) one
            while r <= len(board) - 1 and board[x][r] == color:
                count += 1
                if count > 5:
                    return False  # classic rule~
                r += 1

            if count == 5:
                return True
            
            return False

        def check_vertical_line(board: List[List[str]], x: int, y: int, color: str):
            count = 0
            u = x
            while u >= 0 and board[u][y] == color:
                count += 1
                u -= 1

            l = x + 1  # already counted the (x, y) one
            while l <= len(board) - 1 and board[l][y] == color:
                count += 1
                if count > 5:
                    return False  # classic rule~
                l += 1

            if count == 5:
                return True
            
            return False

        def check_left_diagonal_line(board: List[List[str]], x: int, y: int, color: str):
            count = 0
            ux, uy = x, y
            while ux >= 0 and uy >= 0 and board[ux][uy] == color:
                count += 1
                ux -= 1
                uy -= 1

            lx, ly = x + 1, y + 1
            while lx <= len(board) - 1 and ly <= len(board) - 1 and board[lx][ly] == color:
                count += 1
                if count > 5:
                    return False
                lx += 1
                ly += 1
            
            if count == 5:
                return True

            return False
        
        def check_right_diagonal_line(board: List[List[str]], x: int, y: int, color: str):
            count = 0
            ux, uy = x, y
            while ux >= 0  and uy <= len(board) - 1 and board[ux][uy] == color:
                count += 1
                ux -= 1
                uy += 1
            
            lx, ly = x + 1, y - 1
            while lx <= len(board) - 1 and ly >= 0 and board[lx][ly] == color:
                count += 1
                if count > 5:
                    return False
                lx += 1
                ly -= 1

            if count == 5:
                return True

            return False
        
        def check_draw(board: List[List[str]]):
            for row in board:
                if any([loc == '*' for loc in row]):
                    return False
            return True

        patterns = []
        done = False
        has_horizontal = check_horizontal_line(board, x, y, color)
        if has_horizontal:
            patterns.append('horizontal')
        has_vertical = check_vertical_line(board, x, y, color)
        if has_vertical:
            patterns.append('vertical')
        has_left_diagonal = check_left_diagonal_line(board, x, y, color)
        if has_left_diagonal:
            patterns.append('left_diagonal')
        has_right_diagonal = check_right_diagonal_line(board, x, y, color)
        if has_right_diagonal:
            patterns.append('right_diagonal')
        is_draw = check_draw(board)
        if is_draw:
            patterns.append('draw')

        if patterns:
            done = True
        return done, patterns

    def render(self):
        """
          0 1 2 3 5
        0 w   b b w
        1
        ...
        """
        rows = []

        column_row = [' '] + [str(i) for i in range(self.board.n)]
        rows.append(column_row)

        board_rows = []
        for i, row in enumerate(self.board.get_board()):
            row = [str(i)] + row
            board_rows.append(row)
        
        rows += board_rows
        output = ''
        for row in rows:
            output += ' '.join([char.center(2) for char in row]) + '\n'
        print(output)

