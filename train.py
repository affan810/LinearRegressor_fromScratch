import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn import datasets


from LinearRegression import LinearRegression
import plot
from AccuracyMetric import AccuracyMetric

'''Creating a random dataset, adding noise to check how much stress the model can take'''
X, Y = datasets.make_regression(
    n_samples= 100,
    n_features= 1,
    noise = 20,
    random_state = 6 
)

#Spliting and visualing the plot using plot.py 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state = 69)
fig  = plot.plot()
fig.displayPlot(X, Y)

#Creating object of LinearRegression class and fitting our trainig data to it
reg = LinearRegression(learningRate = 0.1)
reg.fit(X_train, Y_train)
predictions = reg.predict(X_test)

#Mean Squared Error of our predictions against the testing split of data
MeanSquaredError = AccuracyMetric.mse(Y_test, predictions)
print(MeanSquaredError)


#Prediction and Visualsation of Linear regression estimated Line 
Y_predictLine  = reg.predict(X)
fig.predictedLine(X_train, Y_train, X_test, Y_test, Y_predictLine)
