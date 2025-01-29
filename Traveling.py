import csv

class Traveling:

  def __init__(self):
    self.map = {}
    self.heuristics = {}

  def parse(self):
    with open('MapInfo.csv', 'r') as file:
      reader = list(csv.reader(file))

      header_row = reader[0]
      cities_map = {}
      heuristics = {}

      for i in range(1, len(reader)):
        row = reader[i]
        city = row[0]
        heuristics[city] = int(row[1])

        cities_map[city] = []
        for j in range(2, len(row)):
          if row[j] != '':
            cities_map[city].append((header_row[j], int(row[j])))

      self.cities_map = cities_map
      self.heuristics = heuristics
    
  def init_states(self):
    self.parse()
    
    goal = "Bucharest"
    start = input("Where would you like to start? ")
    while start not in self.cities_map: 
      start = input("Please enter a valid city: ")

    return [start, goal]

  def get_actions(self, curr_state): 
    return self.cities_map[curr_state]
  
  def get_heuristic(self, curr_state): 
    return self.heuristics[curr_state]
  
  def test(self, curr_state, goal_state):
    return curr_state == goal_state
  
  def pretty_print(self, curr_state):
    print(curr_state)


    


  

  