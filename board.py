from move import Move


class Board:
  dimension = 3

  def __init__(self):
    self.rows = [[None for i in range(self.dimension)] for j in range(self.dimension)]

  def play_move(self, move: Move) -> bool:
    if self.rows[move.row][move.column] is not None:
      return False

    self.rows[move.row][move.column] = move.value

    return True

  def get_lines(self) -> list:
    return (self.rows
      + [[self.rows[row][column] for row in range(self.dimension)] for column in range(self.dimension)]
      + [[self.rows[i][i] for i in range(self.dimension)]]
      + [[self.rows[i][self.dimension - i - 1] for i in range(self.dimension)]]
      )
