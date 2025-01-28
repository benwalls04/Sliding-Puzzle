from Search import Search
import random
 
def get_actions(state, dim):
    swipe_index = state.index(0)
    row, col = divmod(swipe_index, dim) 

    actions = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for horiz, vert in directions:
        new_row, new_col = row + horiz, col + vert

        if 0 <= new_row < dim and 0 <= new_col < dim:
            new_index = new_row * dim + new_col

            new_state = list(state)
            new_state[swipe_index], new_state[new_index] = new_state[new_index], new_state[swipe_index]

            actions.append(tuple(new_state))

    return actions

def dfs(curr, end, space, hidden): 
  if len(curr) == end - 1:
      cpy = tuple(curr)

      index = cpy.index(hidden)
      state = cpy[:index] + (0,) + cpy[index + 1:]
      space[tuple(state)] = ""
      return
  
  for i in range(1, end):
      if i not in curr:
          next = curr + [i]
          dfs(next, end, space, hidden)


class SlidingPuzzle: 

  @staticmethod
  def get_board(n):
    nums = list(range(1, n * n + 1))

    row = random.randint(0, n - 1)
    col = random.randint(0, n - 1)
    missing_num = random.choice(nums)
    nums.remove(missing_num)

    board = [[None for a in range(n)] for b in range(n)]
    board[row][col] = 0

    for r in range(n):
      for c in range(n):
        if r != row or c != col:
          num = random.choice(nums)
          board[r][c] = num
          nums.remove(num)

    return [board, missing_num]
  
  @staticmethod
  def get_goal(n, missing_num):
    missing_indx = missing_num - 1

    goal = [[(i * n + j + 1) for j in range(n)] for i in range(n)]
    goal[missing_indx // n][(missing_indx) % n] = 0
    return goal

  @staticmethod
  def print_board(board, n):
    print('-' * (4 * n + 1))
    for row in range(n):
      row_str = "| "
      for col in range(n): 
        entry = board[row][col]
        if entry > 0: 
          row_str += str(board[row][col]) + " | "
        else: 
          row_str += "  | "
      print(row_str)
      print('-' * (4 * n + 1))
  
  @staticmethod
  def get_heuristics(): 
    return

  if __name__=="__main__":

    user_input = input("Enter width of the board: ")
    while not user_input.isdigit():
      user_input = input("Pleae enter a number: ")
    dim = int(user_input)

    [start, hidden] = get_board(dim)
    goal = get_goal(dim, hidden)

    space = {}
    end_depth = dim * dim
    dfs([], end_depth + 1, space, hidden)
    
    for state in space.keys():
      actions = get_actions(state, dim)
      space[state] = actions

    searcher = Search(start, goal, space, {})
    path = searcher.search()
    num_expansions = len(path)
    



  