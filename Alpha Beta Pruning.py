import math

class Node:
    def __init__(self, move=None, value=None):
        self.move = move
        self.value = value
        self.children = []

    def is_terminal(self):
        # Define terminal condition based on game logic
        return not self.children

    def generate_children(self):
        # Generate possible moves or game states as children of this node
        # Return a list of child nodes or an empty list if there are no children
        return self.children

    def evaluate(self):
        # Evaluate the current game state (heuristic or actual evaluation)
        return self.value

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate(), None

    if maximizing_player:
        max_eval = -math.inf
        best_move = None
        for child in node.generate_children():
            eval, _ = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = child.move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for child in node.generate_children():
            eval, _ = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best_move = child.move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# Example usage:
# Define a simple tree structure for demonstration
root = Node(value=5)
root.children = [
    Node(move="A", value=3),
    Node(move="B", value=6),
    Node(move="C", value=9)
]
root.children[0].children = [
    Node(move="A1", value=2),
    Node(move="A2", value=4)
]
root.children[1].children = [
    Node(move="B1", value=7),
    Node(move="B2", value=8)
]

# Find the best move using alpha-beta pruning
best_score, best_move = alpha_beta_pruning(root, depth=3, alpha=-math.inf, beta=math.inf, maximizing_player=True)
print("Best move:", best_move, "with score:", best_score)
