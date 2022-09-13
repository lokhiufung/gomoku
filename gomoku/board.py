from typing import List


class Board:
    def __init__(self, size: int):
        self.size = size
        self._n = self.size + 1  # reminder: there are size + 1 possible places for a stone in each row
        self.board = [['*' for _ in range(self._n)] for _ in range(self._n)]

    @property
    def n(self) -> int:
        return self._n

    def __getitem__(self, x) -> List[str]:
        return self.board[x]

    def update_board(self, x, y, color):
        self.board[x][y] = color

    def get_board(self) -> List[List[str]]:
        return self.board
