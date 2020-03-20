import numpy as np
import

class NeuralNetwork:
    def __init__(self,x,y):
        self.x = x
        self.weights1 = np.random.rand(self.x.shape[1],4)
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np.zeros(x.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        d_weights2 = np.dot(self.layer1,2*(self.y-self.output)*sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input, np.dot(2*(self.y-self.output)*sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(layer1))

        self.weights2 += d_weights2
        self.weights1 += d_weights1
