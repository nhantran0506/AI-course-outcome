def bfs(problem):
    # Implement BFS algorithm
    return solution

def dfs(problem):
    # Implement DFS algorithm
    return solution

def ucs(problem):
    # Implement UCS algorithm
    return solution

def greedy(problem):
    # Implement Greedy algorithm
    return solution

def a_star(problem):
    # Implement A* algorithm
    return solution

def run_algorithms(problem):
    results = {}
    results['BFS'] = bfs(problem)
    results['DFS'] = dfs(problem)
    results['UCS'] = ucs(problem)
    results['Greedy'] = greedy(problem)
    results['A*'] = a_star(problem)
    return results

# Test the program
problem = ...
results = run_algorithms(problem)
print(results)