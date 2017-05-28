# Depth-First Search simple example

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# Connected Component
# The implementation below uses the stack data-structure to build-up
# and return a set of vertices that are accessible within the subjects
# connected component
def dfs_google(graph, start):
    visited ,stack = set() , [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex])
    return visited



# The second implementation provides the same
# functionality as the first, however, this
# time we are using the more succinct recursive form
def dfs_Google_R(graph,start, visited= None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
            dfs_Google_R(graph,next,visited)
    return visited

# We are able to tweak both of the previous implementations to
# return all possible paths between a start and goal vertex
def dfs_Google_Path(graph, start,goal):
    stack = [(start,[start])]
    while stack:
        (vertex,path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next,path + [next]))

# The implementation below uses
# the recursive approach calling the
def dfs_Google_Path_R(graph,start, goal, path):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield dfs_Google_Path_R(graph,start,goal,path + [next])


# call the dfs function to find a letters path
print(dfs_google(graph,'A'))

# call the dfs function to find a letters path
# with recursion
print(dfs_Google_R(graph,'C'))

# function call that looks for the path to a letter
print(dfs_Google_Path(graph,'A','F'))

# this function uses the same path search but calls the function recursivly
print(dfs_Google_Path_R(graph , 'C' , 'F'))

