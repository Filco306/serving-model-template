import logging
import numpy as np


class Model:
    """
        Mocking class of an ML model.
    """

    def __init__(self):
        """ Initialize model """
        logging.info("Initializing template model")

    def predict(self, x):
        """
            Returns a prediction uniformly at random

            Parameters:

            x : Can be anything. Seriously, it is a mock parameter.
        """
        return np.random.uniform(0, 1)

    def fit(self, X, y=None):
        """ Fit the model. """
        logging.info("Fitting useless model")
        return self
