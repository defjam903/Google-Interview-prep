# Breath-First Search simple example
# An alternative algorithm called Breath-First search
# provides us with the ability to return
# the same results as DFS but with the added guarantee to return
# the shortest-path firs
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


#Connected Component
def bfs_Google(graph,start):
    visited , queue = set(),[start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
    return visited

# find the path to an item with breath first search
def bfs_Google_Path(graph,start,goal):
    queue = [(start,[start])]
    while queue:
        (vertex,path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                return  path + [next]
            else:
                queue.append((next,path + [next]))

# Knowing that the shortest path will be returned first from the
# BFS path generator method we can create a useful method which simply
# returns the shortest path found or None if no path exists.
def bfs_ShortestPath(graph,start,goal):
    try:
        return next (bfs_Google_Path(graph,start,goal))
    except:
        return None

# function call for BFS fining the shortest path
print(bfs_Google(graph,'C'))

# function to find the path to an item
print(bfs_Google_Path(graph,'A','F'))

# function to find the path from teh previous function
print(bfs_ShortestPath(graph,'A','F'))



