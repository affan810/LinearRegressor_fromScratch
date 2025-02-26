'''Python file to handle all the plotting of data'''

import matplotlib.pyplot as plt 

class plot():

    def __init__(self):
        self.X = None
        self.Y_predictedLine = None 

    '''takes parameter all X and Y values of the generated dataset
       and outputs a graph plotting all the points on a graph'''
    def displayPlot(self, X, Y):
        self.X = X
        fig = plt.figure(figsize=(8,6))
        plt.scatter(X[:, 0], Y, color = "b", marker= "o", s = 30)
        plt.show


    '''takes X_train, Y_train, X_test, Y_test, and Y_predicted
       outputs a graph with different colored point for training and testing data and the line predicted by the linear regressor'''
    def predictedLine(self, X_train, Y_train, X_test, Y_test, Y_predictedLine):
        cmap = plt.get_cmap('viridis')
        fig = plt.figure(figsize=(8,6))
        m1 = plt.scatter(X_train, Y_train, color=cmap(0.9), s=10)
        m2 = plt.scatter(X_test, Y_test, color=cmap(0.5), s=10)
        plt.plot(self.X, Y_predictedLine, color='black', linewidth=2, label='Prediction')
        plt.show()
