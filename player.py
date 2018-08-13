from move import Move
from board import Board


class Player:
  def __init__(self, name, symbol):
    self.name = name
    self.symbol = symbol

  def get_move(self, board: Board) -> Move:
    row_input = self.get_move_input('{}: which row? '.format(self.name), board.dimension - 1)
    column_input = self.get_move_input('{}: which column? '.format(self.name), board.dimension - 1)

    return Move(row_input, column_input, self.symbol)

  def get_move_input(self, prompt: str, maximum_input: int) -> None:
    try:
      move_input_raw = input(prompt)
      move_input_int = int(move_input_raw)

      if 0 <= move_input_int <= maximum_input:
        return move_input_int

      return self.get_move_input(prompt, maximum_input)
    except ValueError as e:
      return self.get_move_input(prompt, maximum_input)
