# prepare-the-bunnies-escape
# find shortest path, optionally can remove one blocker
def get_neighbors(grid, current):
  potential_neighbors = [
    (current[0]-1, current[1]), #left
    (current[0]+1, current[1]), #right
    (current[0], current[1]+1), #down
    (current[0], current[1]-1), #up
  ]
  potential_neighbors = [neighbor for neighbor in potential_neighbors if neighbor[0]>=0 and neighbor[0]<len(grid) and neighbor[1]>=0 and neighbor[1]<len(grid[0])]
  zeros = [neighbor for neighbor in potential_neighbors if grid[neighbor[0]][neighbor[1]]==0]
  return zeros

# calculate distance via bfs from start to all passables
def bfs_distances(grid, source):
  distances = {source: 1}
  queue = []
  queue.append(source)
  while queue:
    current = queue.pop(0)
    for neighbor in get_neighbors(grid, current):
      if neighbor not in distances:
        distances[neighbor] = distances[current]+1
        queue.append(neighbor)
  return distances

def solution(grid):
  width = len(grid[0])
  height = len(grid)
  distances_from_start = bfs_distances(grid, (0,0))
  distances_from_end = bfs_distances(grid, (height-1,width-1))
  # print(distances_from_start)
  # print(distances_from_end)
  # result = distances_from_start[(width-1, height-1)] # without moving
  result = float("inf")

  ones = [(x,y) for x in range(height) for y in range(width) if grid[x][y] == 1]
  for x,y in ones:
    min_from_start = float('inf')
    min_from_end = float('inf')
    neighbors = get_neighbors(grid, (x,y))
    if len(neighbors)==0:
      continue
    for neighbor in neighbors:
      if neighbor in distances_from_start:
        min_from_start = min(distances_from_start[neighbor], min_from_start)
      if neighbor in distances_from_end:
        min_from_end = min(distances_from_end[neighbor], min_from_end)
    total_distance = min_from_start + min_from_end + 1
    if total_distance < result:
      result = total_distance

  return result


# grid = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
grid = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(grid))