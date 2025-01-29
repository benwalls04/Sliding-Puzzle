import heapq
from Traveling import Traveling
from SlidingPuzzle import SlidingPuzzle

class Search: 
  
  class Node: 
    def __init__(self, parent, state, path_cost, heuristic):
        self.parent = parent
        self.state = state
        self.path_cost = path_cost
        self.heuristic = heuristic
        self.actions = None

    def __lt__(self, other):
      return self.state < other.state
    
    def get_path(self): 
      curr = self
      path = []

      while curr.parent is not None:
        path.append(curr.state)
        curr = curr.parent

      return path[::-1]
    
  def __init__(self, start, goal):
    self.goal = goal
    self.start = start
  
  def update_cost(self, pq, node, new_cost):
    for i, (cost, curr_node) in enumerate(pq):
      if curr_node.state == node.state:
        pq[i] = (new_cost, node)
        heapq.heapify(pq)  
        break

  def search(self, problem, add_heuristic): 
    explored = {}
    curr = self.Node(None, self.start, 0, problem.get_heuristic(self.start))
    frontier = [(0, curr)]

    while True: 
      (cost, curr) = heapq.heappop(frontier)

      if problem.test(curr.state, self.goal):
        return [curr.get_path(), len(explored)]
      
      explored[curr.state] = curr.path_cost

      curr.actions = problem.get_actions(curr.state)
      for action in curr.actions:
        (child_state, action_cost) = action

        child_cost = curr.path_cost + action_cost
        if child_state not in explored: 
          explored[child_state] = child_cost

          child_heuristic = 0
          if add_heuristic:
            child_heuristic = problem.get_heuristic(child_state)

          child_node = self.Node(curr, child_state, child_cost, child_heuristic)
          heapq.heappush(frontier, (child_cost + child_heuristic, child_node))

        elif child_cost < explored[child_state]: 
          self.update_cost(frontier, child_node, child_cost)

      if len(frontier) == 0: 
        break

    return [-1, -1]
  
if __name__=="__main__":
  valid_input = {"1", "2", "3"}
  print("Welcome to the searcher")
  while True:
    print("For the Traveling Problem type 1")
    print("For the Sliding Puzzle type 2")
    user_input = input("To quit, type 3\n")
    while user_input not in valid_input:
      user_input = input("Please Enter 1, 2, or 3")

    if user_input == "3":
      break

    problem = Traveling()
    if (user_input == "2"):
      problem = SlidingPuzzle()

    [start, goal] = problem.init_states()
    searcher = Search(start, goal)

    [path, n_expansions] = searcher.search(problem, False)
    print("Starting state: ")
    problem.pretty_print(start)

    if path == -1: 
      print(f"Unsolvable.. Try Again\n")
      continue
    
    print(f"With UCS, you reached the goal after {n_expansions} expansions")

    [path, n_expansions] = searcher.search(problem, True)
    print(f"With A*, you reached the goal after {n_expansions} expansions")
    print(f"You took the following path of length {len(path)}:")
    print("")
    for item in path:
      problem.pretty_print(item)
    print("-------------")

    user_input = None