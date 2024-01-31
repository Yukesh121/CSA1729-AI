import numpy as np
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
    def fit(self, X, y):
        self.root = self._grow_tree(X, y)
    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        n_classes = len(np.unique(y))
        if (self.max_depth is not None and depth >= self.max_depth) or n_classes == 1:
            return Node(value=np.argmax(np.bincount(y)))
        best_gini = np.inf
        best_feature = None
        best_threshold = None
        for feature in range(n_features):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_indices = np.where(X[:, feature] <= threshold)[0]
                right_indices = np.where(X[:, feature] > threshold)[0]
                if len(left_indices) == 0 or len(right_indices) == 0:
                    continue
                left_gini = self._gini(y[left_indices])
                right_gini = self._gini(y[right_indices])
                gini = (len(left_indices) * left_gini + len(right_indices) * right_gini) / n_samples
                if gini < best_gini:
                    best_gini = gini
                    best_feature = feature
                    best_threshold = threshold
        if best_gini == np.inf:
            return Node(value=np.argmax(np.bincount(y)))
        left_indices = np.where(X[:, best_feature] <= best_threshold)[0]
        right_indices = np.where(X[:, best_feature] > best_threshold)[0]
        left = self._grow_tree(X[left_indices], y[left_indices], depth + 1)
        right = self._grow_tree(X[right_indices], y[right_indices], depth + 1)
        return Node(feature=best_feature, threshold=best_threshold, left=left, right=right)
    def _gini(self, y):
        _, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        return 1 - np.sum(probabilities**2)
    def predict(self, X):
        return np.array([self._predict(x, self.root) for x in X])
    def _predict(self, x, node):
        if node.value is not None:
            return node.value
        if x[node.feature] <= node.threshold:
            return self._predict(x, node.left)
        return self._predict(x, node.right)
X = np.array([[2, 4], [5, 1], [3, 3], [7, 2]])
y = np.array([0, 1, 0, 1])
model = DecisionTree(max_depth=2)
model.fit(X, y)
print("Predictions:", model.predict(X))
