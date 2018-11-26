from move import Move
from board import Board


class Player:
  def __init__(self, name, symbol, play_strategy):
    self.name = name
    self.symbol = symbol
    self.play_strategy = play_strategy

  def get_move(self, board: Board) -> Move:
    move = self.play_strategy.get_move(board)
    move.value = self.symbol

    return move
