import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)

class Perceptron:
    """
    Perceptron class to simulate a Neuron
    """

    # Constructor
    # 'dunder init'
    def __init__(self):
        self.weightVector = None
        self.bias = 0

    def initialize(self, nrOfFeatures):
        """Initialize w and b as zero"""

        # Create initial weight vector for each feature
        self.weightVector = np.zeros(nrOfFeatures)

        # Initialize bias
        self.bias = 0

    def train(self, X, y, epochs=100, learningRate=0.1):
        """
        Train the perceptron using the inputVector
        and target labels
        """
        # Initialize weights and bias
        nrOfFeatures = X.shape[1]
        self.initialize(nrOfFeatures)

        epochs = range(0, epochs)

        # for each epoch
        for epoch in epochs:
            logging.info(f"epoch : {epoch}")

            # For each inputVector
            for inputVector, label in zip(X, y):
                logging.debug(f"inputVector : {inputVector}")

                # Labeled output
                logging.debug(f"label : {label}")

                # Predict output
                prediction = self.predict(inputVector)
                logging.debug(f"prediction : {prediction}")

                # Determine error
                error = label - prediction
                logging.debug(f"error : {error}")

                # Update weight and bias
                deltaWeight = learningRate * error * inputVector
                logging.debug(f"deltaWeight : {deltaWeight}")

                deltaBias = learningRate * error
                logging.debug(f"learningRate : {learningRate}")
                logging.debug(f"deltaBias : {deltaBias}")

                # Update weights and bias
                self.weightVector += deltaWeight
                self.bias += deltaBias

    def predict(self, inputVector):
        """
        Determine output value by multiplying
        input vector with weight vector
        """
        activation = np.dot(inputVector, self.weightVector) + self.bias
        logging.debug(f"activation : {activation}")

        return np.where(activation > 0, 1, 0)
        # return 1 if activation > 0 else 0
