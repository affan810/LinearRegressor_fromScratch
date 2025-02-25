import numpy as np
from abc import ABC, abstractmethod

class AccuracyMetric():

    @abstractmethod
    def AccuracyMetric(Y_test: np.ndarray, predctions: np.ndarray) -> float:
        '''
        This is an abstract method that takes two numpy.ndarray Y_test and prediction, compares them by the given accuracy metric and returns a 
        float represting the respective accuracy. 
        '''
        pass

    def __init__(self, Y_test, predictions):
        self.Y_test = Y_test
        self.predictions = predictions
        
    '''Calculated the mean squared error'''
    def mse(Y_test, predictions):
        return np.mean((Y_test-predictions )**2)