import random
from collections import deque

from board import Board
from player import Player
from adjudicator import Adjudicator
from view_screen import ViewScreen
from game_state import GameState


class TicTacToe:
  def __init__(self):
    self.view_screen = ViewScreen()
    self.adjudicator = Adjudicator()

  def start(self) -> None:
    player_list = [
      Player('Player 1', 'X'),
      Player('Player 2', 'O')
      ]

    random.shuffle(player_list)

    board = Board()
    game_state = GameState()

    while not game_state.game_over:
      self.view_screen.print_board(board)

      active_player = player_list[game_state.move_count % 2]

      move = active_player.get_move(board)

      if board.play_move(move):
        game_state.move_count += 1
        self.adjudicator.adjudicate(board, game_state, active_player)

    self.view_screen.print_board(board)
    self.view_screen.announce_outcome(game_state)
