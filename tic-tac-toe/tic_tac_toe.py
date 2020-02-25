import re
import random

_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None
    

  
  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
 
    win= ((self.board[6] == self.board[7] ==  self.board[8]) or 
    (self.board[3] == self.board[4] ==  self.board[5]) or 
    (self.board[0] ==  self.board[1] ==  self.board[2] ) or 
    (self.board[6] ==  self.board[3] ==  self.board[0] ) or 
    (self.board[7] ==  self.board[4] ==  self.board[1] ) or 
    (self.board[8] ==  self.board[5] ==  self.board[2] ) or 
    (self.board[6] ==  self.board[4] ==  self.board[2] ) or 
    (self.board[8] ==  self.board[4] ==  self.board[0] ))

    if(self.turn== _MACHINE and win): self.winner == _PLAYER
    elif(self.turn== _PLAYER and win): self.winner == _MACHINE 
  
   
  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER
    

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
      ran = random.randrange(0,8)
        
      if self.board[ran] is  None:
        self.board[ran] = _MACHINE_SYMBOL
      else: self.machine_turn()
     
          
        

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    self.is_over()
    if self.winner==_MACHINE: print("the winner is MACHINE")
    elif self.winner== _PLAYER: print("the winner is PLAYER")
    
