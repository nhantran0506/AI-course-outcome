from collections import deque

def get_movements(position):
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    valid_movements = []
    for move in movements:
        new_position = (position[0] + move[0], position[1] + move[1])
        if 0 <= new_position[0] < 3 and 0 <= new_position[1] < 3:  # Ensure within grid
            valid_movements.append(new_position)
    return valid_movements

def bfs(initial, empty_tile_pos, final):
    queue = deque([((initial, empty_tile_pos), 0)])  # Add step count to queue elements
    visited = {tuple(map(tuple, initial))}
    
    while queue:
        (board, empty_tile_pos), steps = queue.popleft()
        if board == final:
            return True, steps
        for move in get_movements(empty_tile_pos):
            new_board = [row.copy() for row in board]
            new_board[empty_tile_pos[0]][empty_tile_pos[1]], new_board[move[0]][move[1]] = new_board[move[0]][move[1]], new_board[empty_tile_pos[0]][empty_tile_pos[1]]
            if tuple(map(tuple, new_board)) not in visited:
                queue.append(((new_board, move), steps + 1))  # Increment step count
                visited.add(tuple(map(tuple, new_board)))
    return False

initial = [[1, 2, 3],
            [5, 6, 0],
              [7, 8, 4]]
final = [[0, 1, 2], 
         [3, 4, 5],
           [6, 7, 8]]
empty_tile_pos = [1, 2]

solvable, steps = bfs(initial, empty_tile_pos, final)
if solvable:
    print(f"The puzzle is solvable in {steps} steps.")
else:
    print("The puzzle is not solvable.")