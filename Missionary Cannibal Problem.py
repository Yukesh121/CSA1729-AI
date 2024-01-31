from collections import deque

# State representation: (left_bank_missionaries, left_bank_cannibals, boat_position)
# where boat_position is 0 if boat is on the left bank, 1 if on the right bank

def is_valid_state(state):
    missionaries, cannibals, boat_position = state
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:
        return False
    if 3 - missionaries > 0 and 3 - missionaries < 3 - cannibals:
        return False
    return True

def get_successor_states(state):
    successors = []
    missionaries, cannibals, boat_position = state
    
    # Boat moves left to right
    if boat_position == 0:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (missionaries - m, cannibals - c, 1)
                    if is_valid_state(new_state):
                        successors.append(new_state)
    # Boat moves right to left
    else:
        for m in range(3):
            for c in range(3):
                if 1 <= m + c <= 2:
                    new_state = (missionaries + m, cannibals + c, 0)
                    if is_valid_state(new_state):
                        successors.append(new_state)
    return successors

def bfs_search():
    start_state = (3, 3, 0)  # Start state: 3 missionaries, 3 cannibals, boat on left
    goal_state = (0, 0, 1)    # Goal state: 0 missionaries, 0 cannibals, boat on right
    
    visited = set()
    queue = deque([(start_state, [])])  # Initialize queue with start state and empty path
    
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path + [state]
        
        if state not in visited:
            visited.add(state)
            successors = get_successor_states(state)
            for successor in successors:
                queue.append((successor, path + [state]))
    return None

def print_solution(path):
    for i, state in enumerate(path):
        missionaries, cannibals, boat_position = state
        print(f"Step {i}: Left: {missionaries} missionaries, {cannibals} cannibals, Boat: {'Left' if boat_position == 0 else 'Right'}")
    print("Missionaries and Cannibals successfully crossed the river!")

# Example usage
if __name__ == "__main__":
    solution_path = bfs_search()
    if solution_path:
        print_solution(solution_path)
    else:
        print("No solution found.")
