import numpy as np

class AccuracyMetric():

    def __init__(self, Y_test, predictions):
        self.Y_test = Y_test
        self.predictions = predictions
        
    '''Calculated the mean squared error'''
    def mse(Y_test, predictions):
        return np.mean((Y_test-predictions )**2)