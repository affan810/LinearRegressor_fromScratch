import numpy as np 



class LinearRegression():
    '''Every Linear regresor instance is an object of this class and while initialition can contain learning rate(default 0.1), number of iterations 
       for gradient decent (1000).
       Every line is of the form y = mx + c. in order to build a linear regressor we need m (i.e slop) and c (i.e y intercept)'''


    def __init__(self, learningRate = 0.1, n_iterations = 1000):
        self.learningRate = learningRate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None



    '''Provided parameter X is array of x cordinates of our datapoints.
       initializing weights and bias as zero.
       
       for prediction, (we know y=mx+c, similarly y=mw+b where w is weight and b is bias)
       Multiplying all X with their respective weights and adding a common bias to all predictions
       we will enounter difference between the predicted and the dataset value of y, thus to correct adding the error with scaling it according
       to the learning rate
       repeat n_iterations time which is the predefined cap for gradient decent... making sure gradient stops even if zero is not found'''
    
    def fit(self, X, Y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0 

        for _ in range(self.n_iterations):
            y_predicted  = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T, (y_predicted-Y))
            db = (1/n_samples) * np.sum(y_predicted-Y)


            self.weights = self.weights - self.learningRate*dw
            self.bias = self.bias - self.learningRate*db


    '''Applying the weights and bias to testing data and predicting y. The slop and the intercept'''
    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted