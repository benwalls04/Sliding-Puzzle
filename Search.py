import heapq

class Search: 
  
  class Node: 
    def __init__(self, parent, state, path_cost, heuristic):
        self.parent = parent
        self.state = state
        self.path_cost = path_cost
        self.heuristic = heuristic
        self.actions = None
    
    def get_path(self): 
      curr = self
      path = []

      while curr.parent is not None:
        path.append(curr.state)
        curr = curr.parent

      return path[::-1]
    
  def __init__(self, start, goal, edges, heuristics):
    self.goal = goal
    self.start = start
    ## state space is a map from states -> list of (children, cost)
    self.edges = edges
    self.heuristics = heuristics

  def generate_actions(self, node):
    node.actions = self.edges[node.state]
    return node.actions
  
  def update_cost(self, pq, node, new_cost):
    for i, (cost, curr_node) in enumerate(pq):
      if curr_node.state == node.state:
        pq[i] = (new_cost, node)
        heapq.heapify(pq)  
        break

  def search(self, add_heuristic): 
    explored = {}
    curr = self.Node(None, self.start, 0, self.heuristics[self.start])
    frontier = [(0, curr)]

    while True: 
      (cost, curr) = heapq.heappop(frontier)

      if curr.state == self.goal: 
        return [curr.get_path(), len(explored)]
      
      explored[curr.state] = curr.path_cost
      print(curr.state)
      print(curr.heuristic)
      print("----------")
      
      self.generate_actions(curr)

      for action in curr.actions:
        (child, action_cost) = action

        child_cost = curr.path_cost + action_cost
        if child not in explored: 
          explored[child] = child_cost

          child_heuristic = 0
          if add_heuristic:
            child_heuristic = self.heuristics[child]

          child_node = self.Node(curr, child, child_cost, child_heuristic)
          heapq.heappush(frontier, (child_cost + child_heuristic, child_node))

        elif child_cost < explored[child]: 
          self.update_cost(frontier, child_node, child_cost)

      if len(frontier) == 0: 
        break

    return False
  
  def main(self): 
    valid_input = {"1", "2", "3"}
    print("Welcome to the searcher")
    while True:
      print("For uniform cost search type 1")
      print("For A* search type 2")
      user_input = input("To quit, type 3\n")
      while user_input not in valid_input:
        user_input = input("Please Enter 1 (UCS), 2 (A*), or 3 (Quit)")

      if user_input == "3":
        break

      A_star = user_input == "2"
      [path, n_expansions] = self.search(A_star)
      
      print(f"You have reached the goal after {n_expansions} expansions")
      print("You took the following path:")
      for item in path:
        print(f"\t{item}")

      user_input = None
      print("-------------")


      

    

  
  