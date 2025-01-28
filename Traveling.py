from Search import Search
import csv

class Traveling:

  @staticmethod
  def parse():
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

      return [cities_map, heuristics]

  if __name__ == "__main__": 
    [cities_map, heuristics] = parse()
    goal = "Bucharest"

    start = input("Where would you like to start? ")
    while start not in cities_map: 
      start = input("Please enter a valid city: ")

    searcher = Search(start, goal, cities_map, heuristics)
    path = searcher.main()
    num_expansions = len(path)

    ## FIXME: print states and actions might as well include costs as well 
    print(f"You have arrived in {goal} after {num_expansions} stops")
    print("You took the following path:")
    for city in path:
      print(f"\t{city}")
    


    


  

  