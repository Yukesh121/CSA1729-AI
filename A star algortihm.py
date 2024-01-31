import heapq

class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state  # Current state of the node
        self.parent = parent  # Parent node
        self.action = action  # Action taken from parent to reach this node
        self.g = g  # Cost from start node to this node
        self.h = h  # Heuristic cost from this node to goal node

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def astar(start_state, goal_state, successors, heuristic):
    open_list = []
    closed_set = set()

    start_node = Node(state=start_state, g=0, h=heuristic(start_state, goal_state))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for action, successor_state, step_cost in successors(current_node.state):
            if successor_state in closed_set:
                continue

            g = current_node.g + step_cost
            h = heuristic(successor_state, goal_state)
            child_node = Node(state=successor_state, parent=current_node, action=action, g=g, h=h)

            heapq.heappush(open_list, child_node)

    return None  # No path found

# Example usage:
# Define successors function
def successors(state):
    successors = []
    x, y = state
    if x > 0:
        successors.append(('left', (x - 1, y), 1))
    if x < 2:
        successors.append(('right', (x + 1, y), 1))
    if y > 0:
        successors.append(('down', (x, y - 1), 1))
    if y < 2:
        successors.append(('up', (x, y + 1), 1))
    return successors

# Define heuristic function (Manhattan distance)
def manhattan_distance(state, goal_state):
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

# Define start and goal states
start_state = (0, 0)
goal_state = (2, 2)

# Find path using A* algorithm
path = astar(start_state, goal_state, successors, manhattan_distance)
if path:
    print("Path found:", path)
else:
    print("No path found.")
