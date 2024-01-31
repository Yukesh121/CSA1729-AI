import heapq
class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def manhattan_distance(state):
    distance = 0
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j] - 1, 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance
def generate_successors(node):
    successors = []
    i, j = get_blank_position(node.state)
    actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for action in actions:
        new_i, new_j = i + action[0], j + action[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in node.state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            successors.append(PuzzleNode(new_state, node, action, node.cost + 1, manhattan_distance(new_state)))
    return successors
def print_solution(solution_node):
    if solution_node is None:
        print("No solution found.")
    else:
        actions = []
        while solution_node.parent is not None:
            actions.append(solution_node.action)
            solution_node = solution_node.parent
        actions.reverse()
        print("Solution:")
        for action in actions:
            print(action)
def solve_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state, None, None, 0, manhattan_distance(initial_state))
    frontier = [initial_node]
    explored = set()
    while frontier:
        current_node = heapq.heappop(frontier)
        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            print("Goal state reached!")
            print_solution(current_node)
            return
        explored.add(tuple(map(tuple, current_node.state)))
        successors = generate_successors(current_node)
        for successor in successors:
            if tuple(map(tuple, successor.state)) not in explored:
                heapq.heappush(frontier, successor)
    print("No solution found.")
# Example usage:
initial_state = [
    [1, 2, 3],
    [4, 5, 0],
    [7, 8, 6]
]
solve_puzzle(initial_state)
