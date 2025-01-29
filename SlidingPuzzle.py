import random

class SlidingPuzzle: 
    
  def __init__(self):
      self.board_size = 0
      self.missing_num = 0

  def get_actions(self, curr_state):
      n = self.board_size
      swipe_index = curr_state.index(0)
      row, col = divmod(swipe_index, n)
      
      actions = []
      directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

      for horiz, vert in directions:
          new_row, new_col = row + horiz, col + vert
          if 0 <= new_row < n and 0 <= new_col < n:
              new_index = new_row * n + new_col
              new_state = list(curr_state)
              new_state[swipe_index], new_state[new_index] = new_state[new_index], new_state[swipe_index]
              actions.append(tuple([tuple(new_state), 1]))

      return actions

  def get_board(self):
      n = self.board_size
      nums = list(range(1, n * n + 1))
      missing_num = random.choice(nums)
      nums.remove(missing_num)

      board = [None] * (n * n)
      empty_index = random.randint(0, n * n - 1)
      board[empty_index] = 0

      for i in range(n * n):
          if board[i] is None:
              board[i] = nums.pop()
      
      return board, missing_num

  def init_states(self):
      user_input = input("Enter width of the board: ")
      while not user_input.isdigit():
          user_input = input("Please enter a number: ")
      n = int(user_input)
      self.board_size = n

      board, missing_num = self.get_board()
      self.missing_num = missing_num

      missing_indx = missing_num - 1
      goal = [(i + 1) for i in range(n * n)]
      goal[missing_indx] = 0
      
      self.pretty_print(board)

      return tuple(board), tuple(goal)

  def pretty_print(self, board):
      n = self.board_size
      print('-' * (4 * n + 1))
      for i in range(n):
          row = board[i * n:(i + 1) * n]
          row_str = "| " + " | ".join(str(entry) if entry > 0 else " " for entry in row) + " |"
          print(row_str)
          print('-' * (4 * n + 1))

  def get_heuristic(self, curr_state):
      return 0

  def test(self, curr_state, goal_state):
      return curr_state == goal_state
