import numpy as np

class FeedForwardNN:
    def __init__(self, layers, activation='sigmoid'):
        self.layers = layers
        self.activation = activation
        self.weights = []
        self.biases = []
        self.activations = []

        # Initialize weights and biases randomly
        for i in range(1, len(layers)):
            weight_matrix = np.random.randn(layers[i], layers[i-1])
            bias_vector = np.random.randn(layers[i], 1)
            self.weights.append(weight_matrix)
            self.biases.append(bias_vector)

    def activate(self, x):
        if self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-x))
        elif self.activation == 'relu':
            return np.maximum(0, x)
        elif self.activation == 'tanh':
            return np.tanh(x)
        else:
            raise ValueError("Activation function not supported")

    def derivative(self, x):
        if self.activation == 'sigmoid':
            return x * (1 - x)
        elif self.activation == 'relu':
            x[x <= 0] = 0
            x[x > 0] = 1
            return x
        elif self.activation == 'tanh':
            return 1 - x**2
        else:
            raise ValueError("Activation function not supported")

    def feedforward(self, x):
        self.activations = [x]
        for i in range(len(self.layers) - 1):
            z = np.dot(self.weights[i], self.activations[-1]) + self.biases[i]
            self.activations.append(self.activate(z))
        return self.activations[-1]

    def backpropagate(self, x, y, learning_rate):
        deltas = [None] * len(self.layers)
        deltas[-1] = (self.activations[-1] - y) * self.derivative(self.activations[-1])
        for i in range(len(self.layers) - 2, 0, -1):
            deltas[i] = np.dot(self.weights[i].T, deltas[i+1]) * self.derivative(self.activations[i])

        for i in range(len(self.layers) - 1):
            self.weights[i] -= learning_rate * np.dot(deltas[i+1], self.activations[i].T)
            self.biases[i] -= learning_rate * deltas[i+1]

    def train(self, X, y, epochs, learning_rate):
        for _ in range(epochs):
            for i in range(len(X)):
                output = self.feedforward(X[i].reshape(-1, 1))
                self.backpropagate(X[i].reshape(-1, 1), y[i].reshape(-1, 1), learning_rate)

    def predict(self, X):
        predictions = []
        for i in range(len(X)):
            predictions.append(self.feedforward(X[i].reshape(-1, 1)))
        return np.array(predictions)

# Example usage
if __name__ == "__main__":
    # Example dataset
    X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_train = np.array([[0], [1], [1], [0]])

    # Create and train feedforward neural network
    nn = FeedForwardNN(layers=[2, 4, 1], activation='sigmoid')
    nn.train(X_train, y_train, epochs=1000, learning_rate=0.1)

    # Make predictions
    predictions = nn.predict(X_train)
    print("Predictions:", predictions)
